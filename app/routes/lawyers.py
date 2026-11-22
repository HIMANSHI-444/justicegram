from flask import Blueprint, render_template, request, flash, redirect, url_for, g, jsonify
from app.models import db, Lawyer, Inquiry, Bookmark
from app.routes.auth import login_required
from app.ai.legal_knowledge import LEGAL_CATEGORIES

lawyers_bp = Blueprint('lawyers', __name__)

@lawyers_bp.route('/')
def directory():
    """Searchable and filterable directory of legal practitioners."""
    # Read filter query parameters
    selected_category = request.args.get('category', '').strip()
    selected_city = request.args.get('city', '').strip()
    selected_language = request.args.get('language', '').strip()
    min_experience = request.args.get('experience', '').strip()
    pro_bono_only = request.args.get('pro_bono') == '1'
    verified_only = request.args.get('verified') == '1'
    search_keyword = request.args.get('q', '').strip()
    sort_by = request.args.get('sort', 'rating_desc')

    query = Lawyer.query

    if selected_category:
        query = query.filter(
            (Lawyer.specialization == selected_category) | 
            (Lawyer.secondary_specialization == selected_category)
        )

    if selected_city:
        query = query.filter(Lawyer.city.ilike(f"%{selected_city}%"))

    if selected_language:
        query = query.filter(Lawyer.languages_spoken.ilike(f"%{selected_language}%"))

    if min_experience and min_experience.isdigit():
        query = query.filter(Lawyer.experience_years >= int(min_experience))

    if pro_bono_only:
        query = query.filter(Lawyer.is_pro_bono.is_(True))

    if verified_only:
        query = query.filter(Lawyer.is_verified.is_(True))

    if search_keyword:
        query = query.filter(
            (Lawyer.name.ilike(f"%{search_keyword}%")) |
            (Lawyer.qualification.ilike(f"%{search_keyword}%")) |
            (Lawyer.bio.ilike(f"%{search_keyword}%"))
        )

    # Sorting
    if sort_by == 'exp_desc':
        query = query.order_by(Lawyer.experience_years.desc())
    elif sort_by == 'exp_asc':
        query = query.order_by(Lawyer.experience_years.asc())
    elif sort_by == 'name_asc':
        query = query.order_by(Lawyer.name.asc())
    else: # Default: rating descending, with pro bono prioritized
        query = query.order_by(Lawyer.is_pro_bono.desc(), Lawyer.rating.desc())

    lawyers = query.all()

    # Extract distinct cities and languages for dynamic filter dropdowns
    all_cities = sorted(list({l.city for l in Lawyer.query.with_entities(Lawyer.city).all() if l.city}))
    all_languages = sorted(list({
        lang.strip() 
        for row in Lawyer.query.with_entities(Lawyer.languages_spoken).all() 
        for lang in row[0].split(',') 
        if lang.strip()
    }))

    # Get user's bookmarked lawyer IDs if logged in
    bookmarked_ids = set()
    if g.user:
        bookmarked_ids = {
            b.item_id for b in Bookmark.query.filter_by(user_id=g.user.id, item_type='lawyer').all()
        }

    return render_template(
        'lawyers/directory.html',
        lawyers=lawyers,
        all_cities=all_cities,
        all_languages=all_languages,
        selected_category=selected_category,
        selected_city=selected_city,
        selected_language=selected_language,
        min_experience=min_experience,
        pro_bono_only=pro_bono_only,
        verified_only=verified_only,
        search_keyword=search_keyword,
        sort_by=sort_by,
        bookmarked_ids=bookmarked_ids,
        categories=LEGAL_CATEGORIES
    )

@lawyers_bp.route('/<int:lawyer_id>')
def detail(lawyer_id):
    """Detailed profile view for an individual legal practitioner."""
    lawyer = db.session.get(Lawyer, lawyer_id)
    if not lawyer:
        flash("Lawyer profile not found.", "warning")
        return redirect(url_for('lawyers.directory'))

    # Check if bookmarked
    is_bookmarked = False
    if g.user:
        is_bookmarked = Bookmark.query.filter_by(
            user_id=g.user.id, item_type='lawyer', item_id=lawyer.id
        ).first() is not None

    # Similar lawyers in the same specialization
    similar_lawyers = Lawyer.query.filter(
        Lawyer.specialization == lawyer.specialization,
        Lawyer.id != lawyer.id
    ).limit(3).all()

    return render_template(
        'lawyers/detail.html',
        lawyer=lawyer,
        is_bookmarked=is_bookmarked,
        similar_lawyers=similar_lawyers
    )

@lawyers_bp.route('/<int:lawyer_id>/inquire', methods=['POST'])
@login_required
def submit_inquiry(lawyer_id):
    """Submit a consultation inquiry to a lawyer."""
    lawyer = db.session.get(Lawyer, lawyer_id)
    if not lawyer:
        flash("Selected lawyer not found.", "danger")
        return redirect(url_for('lawyers.directory'))

    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()
    category = request.form.get('legal_category', lawyer.specialization).strip()
    user_phone = request.form.get('phone', g.user.phone or '').strip()
    preferred_time = request.form.get('preferred_contact_time', 'Morning (10am - 1pm)')

    if not subject or not message:
        flash("Please provide both a subject and details for your inquiry.", "warning")
        return redirect(url_for('lawyers.detail', lawyer_id=lawyer.id))

    inquiry = Inquiry(
        user_id=g.user.id,
        lawyer_id=lawyer.id,
        legal_category=category,
        subject=subject,
        message=message,
        user_phone=user_phone,
        preferred_contact_time=preferred_time,
        status='Pending'
    )
    db.session.add(inquiry)
    db.session.commit()

    flash(f"Your consultation inquiry has been submitted to Advocate {lawyer.name}. You can track it in your dashboard.", "success")
    return redirect(url_for('user.dashboard'))

@lawyers_bp.route('/<int:lawyer_id>/bookmark', methods=['POST'])
@login_required
def toggle_bookmark(lawyer_id):
    """Toggle bookmark for a lawyer profile."""
    lawyer = db.session.get(Lawyer, lawyer_id)
    if not lawyer:
        return jsonify({'success': False, 'error': 'Lawyer not found'}), 404

    existing = Bookmark.query.filter_by(
        user_id=g.user.id, item_type='lawyer', item_id=lawyer.id
    ).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        bookmarked = False
        message = "Removed from your saved profiles."
    else:
        new_bm = Bookmark(user_id=g.user.id, item_type='lawyer', item_id=lawyer.id)
        db.session.add(new_bm)
        db.session.commit()
        bookmarked = True
        message = "Saved to your dashboard bookmarks."

    if request.is_json:
        return jsonify({'success': True, 'bookmarked': bookmarked, 'message': message})
    flash(message, "info")
    return redirect(request.referrer or url_for('lawyers.detail', lawyer_id=lawyer.id))
