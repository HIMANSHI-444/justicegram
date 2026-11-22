from flask import Blueprint, render_template, request, jsonify, g, flash, redirect, url_for
from app.models import db, Lawyer, LegalAidResource, LegalQuery
from app.ai.classifier import ai_classifier
from app.ai.legal_knowledge import LEGAL_CATEGORIES

assistant_bp = Blueprint('assistant', __name__)

SAMPLE_PROMPTS = [
    {
        "title": "Unreturned Security Deposit",
        "category": "Property and Real Estate",
        "prompt": "My landlord is refusing to return my security deposit of ₹30,000 even after I vacated the flat with 30 days prior notice, claiming imaginary wall painting charges."
    },
    {
        "title": "College Certificates Withheld",
        "category": "Education-Related Legal Issues",
        "prompt": "My private engineering college is withholding my original 10th and 12th marksheets after degree completion and demanding extra unapproved penalty fees."
    },
    {
        "title": "Unpaid Salary by Employer",
        "category": "Employment and Labour Law",
        "prompt": "My company has not paid my salary for the last 2 months and when I submitted my resignation, HR refused to provide my relieving letter or experience certificate."
    },
    {
        "title": "Online UPI Cyber Fraud",
        "category": "Cybercrime and Digital Issues",
        "prompt": "I lost ₹45,000 after receiving a fake electricity bill SMS. Money got debited instantly via UPI without sharing any OTP. How do I freeze the account?"
    },
    {
        "title": "Defective Online Product",
        "category": "Consumer Rights",
        "prompt": "I bought a brand new laptop from an e-commerce platform that arrived with a shattered screen. The seller rejected the replacement request claiming customer fault."
    },
    {
        "title": "Matrimonial Dowry Harassment",
        "category": "Women's Legal Support",
        "prompt": "My in-laws and husband are demanding ₹5 lakh cash as additional dowry and have locked me in the room, threatening to kick me out of the house."
    },
    {
        "title": "Recovery Agent Harassment",
        "category": "Banking and Financial Issues",
        "prompt": "Private bank loan recovery agents are calling my parents and relatives late at night, abusing them, and threatening to seize our household furniture."
    },
    {
        "title": "Copyright Infringement",
        "category": "Intellectual Property",
        "prompt": "A commercial YouTube channel downloaded my original tutorial video series without permission and re-uploaded it behind a paywall."
    }
]

def compute_lawyer_match_reasons(lawyer, category, user_city=None):
    """Generates transparent, contextual match reasons explaining why an advocate was matched."""
    reasons = []
    
    # Specialization match
    if lawyer.specialization == category:
        reasons.append(f"Primary Specialization: Matches '{category}'")
    elif lawyer.secondary_specialization == category:
        reasons.append(f"Secondary Specialization: Active practice in '{category}'")
    else:
        reasons.append(f"Allied Legal Experience in {lawyer.specialization}")

    # Pro bono / Fee structure
    if lawyer.is_pro_bono:
        reasons.append("Provides Free Pro Bono Consultations")
    elif lawyer.consultation_fee_type == "Low Cost":
        reasons.append(f"Subsidized Consultation ({lawyer.consultation_fee_amount})")

    # City / Jurisdiction
    if user_city and lawyer.city.lower() == user_city.lower():
        reasons.append(f"Local Court Practice in {lawyer.city}")
    else:
        reasons.append(f"Practices in {lawyer.city}, {lawyer.state}")

    # Experience & Rating
    if lawyer.experience_years >= 10:
        reasons.append(f"Senior Advocate ({lawyer.experience_years}+ years experience)")
    else:
        reasons.append(f"{lawyer.experience_years} years active legal practice")

    return reasons

@assistant_bp.route('/assistant', methods=['GET', 'POST'])
def assistant():
    """Main AI Legal Assistant page supporting direct search, prompt selection,
    manual category override, and structured categorization results.
    """
    initial_query = request.args.get('q', '').strip()
    selected_manual_cat = request.args.get('category', '').strip() or request.form.get('manual_category', '').strip()
    result = None
    matched_lawyers = []
    matched_aid = []
    query_record_id = None
    user_city = g.user.city if g.user and g.user.city else None

    if request.method == 'POST' or initial_query:
        query_text = request.form.get('query_text', initial_query).strip()

        if query_text:
            # 1. Run AI Classifier Pipeline with optional manual category override
            manual_cat_param = selected_manual_cat if selected_manual_cat in LEGAL_CATEGORIES else None
            result = ai_classifier.classify(query_text, manual_category=manual_cat_param)

            if result.get('success'):
                category = result.get('category')

                # 2. Save query log to database
                user_id = g.user.id if g.user else None
                query_record = LegalQuery(
                    user_id=user_id,
                    query_text=query_text,
                    predicted_category=category,
                    confidence_score=result.get('confidence', 0.0),
                    is_ambiguous=result.get('is_ambiguous', False)
                )
                db.session.add(query_record)
                db.session.commit()
                query_record_id = query_record.id

                # 3. Retrieve matching lawyers
                lawyer_query = Lawyer.query
                if category and category != "Other / Needs Clarification":
                    lawyer_query = lawyer_query.filter(
                        (Lawyer.specialization == category) | (Lawyer.secondary_specialization == category)
                    )
                # Prioritize pro bono and rating
                raw_lawyers = lawyer_query.order_by(
                    Lawyer.is_pro_bono.desc(),
                    Lawyer.rating.desc()
                ).limit(4).all()

                # Fallback if no specific category match
                if not raw_lawyers:
                    raw_lawyers = Lawyer.query.order_by(
                        Lawyer.is_pro_bono.desc(),
                        Lawyer.rating.desc()
                    ).limit(4).all()

                # Attach match reasons to lawyer objects
                matched_lawyers = []
                for l in raw_lawyers:
                    l.match_reasons = compute_lawyer_match_reasons(l, category, user_city)
                    matched_lawyers.append(l)

                # 4. Retrieve matching legal aid clinics and helplines
                aid_query = LegalAidResource.query
                if category and category != "Other / Needs Clarification":
                    aid_query = aid_query.filter(
                        (LegalAidResource.category == category) | (LegalAidResource.category == 'All Categories')
                    )
                matched_aid = aid_query.order_by(LegalAidResource.is_free.desc()).limit(3).all()
                if not matched_aid:
                    matched_aid = LegalAidResource.query.limit(3).all()

            else:
                flash(result.get('error', 'Unable to process query.'), 'warning')

    return render_template(
        'assistant.html',
        sample_prompts=SAMPLE_PROMPTS,
        initial_query=initial_query,
        selected_manual_cat=selected_manual_cat,
        result=result,
        matched_lawyers=matched_lawyers,
        matched_aid=matched_aid,
        query_record_id=query_record_id,
        categories=list(LEGAL_CATEGORIES.keys())
    )

@assistant_bp.route('/api/assistant/classify', methods=['POST'])
def api_classify():
    """Asynchronous JSON API endpoint for live UI submission with match explanations."""
    data = request.get_json() or {}
    query_text = data.get('query_text', '').strip()
    manual_category = data.get('manual_category', '').strip() or None
    user_city = g.user.city if g.user and g.user.city else None

    if not query_text:
        return jsonify({'success': False, 'error': 'Please enter a description of your problem.'}), 400

    if manual_category and manual_category not in LEGAL_CATEGORIES:
        manual_category = None

    result = ai_classifier.classify(query_text, manual_category=manual_category)
    if not result.get('success'):
        return jsonify(result), 400

    category = result.get('category')

    # Save to database
    user_id = g.user.id if g.user else None
    query_record = LegalQuery(
        user_id=user_id,
        query_text=query_text,
        predicted_category=category,
        confidence_score=result.get('confidence', 0.0),
        is_ambiguous=result.get('is_ambiguous', False)
    )
    db.session.add(query_record)
    db.session.commit()

    # Find matching lawyers
    lawyers = Lawyer.query.filter(
        (Lawyer.specialization == category) | (Lawyer.secondary_specialization == category)
    ).order_by(Lawyer.is_pro_bono.desc(), Lawyer.rating.desc()).limit(3).all()

    if not lawyers:
        lawyers = Lawyer.query.limit(3).all()

    lawyers_data = []
    for l in lawyers:
        l_dict = l.to_dict()
        l_dict['match_reasons'] = compute_lawyer_match_reasons(l, category, user_city)
        lawyers_data.append(l_dict)

    # Find matching legal aid
    aid_resources = LegalAidResource.query.filter(
        (LegalAidResource.category == category) | (LegalAidResource.category == 'All Categories')
    ).limit(3).all()

    return jsonify({
        'success': True,
        'query_id': query_record.id,
        'classification': result,
        'lawyers': lawyers_data,
        'legal_aid': [a.to_dict() for a in aid_resources]
    })

@assistant_bp.route('/api/assistant/feedback', methods=['POST'])
def api_feedback():
    """Endpoint for users to mark whether an AI classification was helpful."""
    data = request.get_json() or {}
    query_id = data.get('query_id')
    accurate = data.get('accurate')

    if query_id and accurate is not None:
        query = db.session.get(LegalQuery, query_id)
        if query:
            query.user_feedback_accurate = bool(accurate)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Thank you for your feedback!'})

    return jsonify({'success': False, 'error': 'Invalid request'}), 400
