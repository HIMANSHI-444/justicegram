from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, g
from collections import Counter
from app.models import db, User, Lawyer, LegalAidResource, LegalQuery, Inquiry
from app.routes.auth import admin_required
from app.ai.classifier import ai_classifier
from app.ai.train_model import train_and_evaluate
from app.ai.legal_knowledge import LEGAL_CATEGORIES

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
@admin_required
def dashboard():
    """Main administrative dashboard with Chart.js analytics and quick management actions."""
    total_users = User.query.count()
    total_lawyers = Lawyer.query.count()
    total_aid = LegalAidResource.query.count()
    total_queries = LegalQuery.query.count()
    total_inquiries = Inquiry.query.count()

    recent_queries = LegalQuery.query.order_by(LegalQuery.created_at.desc()).limit(6).all()
    recent_inquiries = Inquiry.query.order_by(Inquiry.created_at.desc()).limit(6).all()

    stats = {
        'total_users': total_users,
        'total_lawyers': total_lawyers,
        'total_aid': total_aid,
        'total_queries': total_queries,
        'total_inquiries': total_inquiries,
        'verified_lawyers': Lawyer.query.filter_by(is_verified=True).count(),
        'pro_bono_lawyers': Lawyer.query.filter_by(is_pro_bono=True).count()
    }

    return render_template(
        'admin/dashboard.html',
        stats=stats,
        recent_queries=recent_queries,
        recent_inquiries=recent_inquiries
    )

@admin_bp.route('/api/stats')
@admin_required
def api_stats():
    """Returns aggregated data for Chart.js dashboard charts."""
    # 1. Queries breakdown by category
    queries = LegalQuery.query.all()
    cat_counter = Counter([q.predicted_category for q in queries])
    
    # Ensure all 10 categories are represented
    category_labels = list(LEGAL_CATEGORIES.keys())
    category_counts = [cat_counter.get(cat, 0) for cat in category_labels]

    # 2. Lawyer pro bono breakdown
    pro_bono_count = Lawyer.query.filter_by(is_pro_bono=True).count()
    paid_count = Lawyer.query.filter_by(is_pro_bono=False).count()

    # 3. Inquiry status breakdown
    inquiries = Inquiry.query.all()
    status_counter = Counter([i.status for i in inquiries])
    status_labels = ['Pending', 'Contacted', 'Resolved', 'Closed']
    status_counts = [status_counter.get(s, 0) for s in status_labels]

    # 4. Confidence buckets
    conf_buckets = {'90-100%': 0, '70-89%': 0, '50-69%': 0, '<50%': 0}
    for q in queries:
        conf = q.confidence_score or 0
        if conf >= 90:
            conf_buckets['90-100%'] += 1
        elif conf >= 70:
            conf_buckets['70-89%'] += 1
        elif conf >= 50:
            conf_buckets['50-69%'] += 1
        else:
            conf_buckets['<50%'] += 1

    return jsonify({
        'categories': {
            'labels': category_labels,
            'data': category_counts
        },
        'lawyer_types': {
            'labels': ['Pro Bono / Free', 'Standard Fee'],
            'data': [pro_bono_count, paid_count]
        },
        'inquiry_status': {
            'labels': status_labels,
            'data': status_counts
        },
        'confidence_distribution': {
            'labels': list(conf_buckets.keys()),
            'data': list(conf_buckets.values())
        }
    })

# --- LAWYER CRUD ---
@admin_bp.route('/lawyers')
@admin_required
def lawyers_manage():
    """List lawyers for administration."""
    lawyers = Lawyer.query.order_by(Lawyer.created_at.desc()).all()
    return render_template('admin/lawyers_manage.html', lawyers=lawyers, categories=LEGAL_CATEGORIES)

@admin_bp.route('/lawyers/add', methods=['POST'])
@admin_required
def lawyer_add():
    """Add a new lawyer profile."""
    name = request.form.get('name')
    qualification = request.form.get('qualification')
    specialization = request.form.get('specialization')
    experience_years = int(request.form.get('experience_years', 1))
    city = request.form.get('city')
    state = request.form.get('state', 'Delhi NCR')
    languages = request.form.get('languages_spoken', 'English, Hindi')
    bio = request.form.get('bio')
    contact_email = request.form.get('contact_email')
    contact_phone = request.form.get('contact_phone')
    is_pro_bono = request.form.get('is_pro_bono') == 'on'
    is_verified = request.form.get('is_verified') == 'on'
    fee_type = request.form.get('consultation_fee_type', 'Standard')
    fee_amount = request.form.get('consultation_fee_amount', 'Standard')
    reg_no = request.form.get('bar_council_reg_number', '')

    lawyer = Lawyer(
        name=name,
        qualification=qualification,
        specialization=specialization,
        experience_years=experience_years,
        city=city,
        state=state,
        languages_spoken=languages,
        bio=bio,
        contact_email=contact_email,
        contact_phone=contact_phone,
        is_pro_bono=is_pro_bono,
        is_verified=is_verified,
        consultation_fee_type=fee_type,
        consultation_fee_amount=fee_amount,
        bar_council_reg_number=reg_no
    )
    db.session.add(lawyer)
    db.session.commit()

    flash(f"Lawyer Advocate {name} added successfully.", "success")
    return redirect(url_for('admin.lawyers_manage'))

@admin_bp.route('/lawyers/<int:lawyer_id>/toggle-verify', methods=['POST'])
@admin_required
def lawyer_toggle_verify(lawyer_id):
    """Toggle verification badge for a lawyer."""
    lawyer = db.session.get(Lawyer, lawyer_id)
    if lawyer:
        lawyer.is_verified = not lawyer.is_verified
        db.session.commit()
        status_text = "Verified" if lawyer.is_verified else "Unverified"
        flash(f"Lawyer Advocate {lawyer.name} marked as {status_text}.", "info")
    return redirect(url_for('admin.lawyers_manage'))

@admin_bp.route('/lawyers/<int:lawyer_id>/delete', methods=['POST'])
@admin_required
def lawyer_delete(lawyer_id):
    """Delete a lawyer profile."""
    lawyer = db.session.get(Lawyer, lawyer_id)
    if lawyer:
        db.session.delete(lawyer)
        db.session.commit()
        flash(f"Lawyer profile deleted.", "info")
    return redirect(url_for('admin.lawyers_manage'))

# --- LEGAL AID CRUD ---
@admin_bp.route('/legal-aid')
@admin_required
def legal_aid_manage():
    """List legal aid centers for administration."""
    resources = LegalAidResource.query.order_by(LegalAidResource.created_at.desc()).all()
    return render_template('admin/legal_aid_manage.html', resources=resources, categories=LEGAL_CATEGORIES)

@admin_bp.route('/legal-aid/add', methods=['POST'])
@admin_required
def legal_aid_add():
    """Add a new legal aid resource."""
    name = request.form.get('name')
    org_type = request.form.get('organization_type')
    category = request.form.get('category', 'All Categories')
    city = request.form.get('city')
    state = request.form.get('state')
    helpline = request.form.get('helpline_number')
    phone = request.form.get('phone')
    email = request.form.get('email')
    website_url = request.form.get('website_url')
    eligibility = request.form.get('eligibility_criteria', 'Open to all eligible citizens under NALSA guidelines.')
    services = request.form.get('services_offered')

    res = LegalAidResource(
        name=name,
        organization_type=org_type,
        category=category,
        city=city,
        state=state,
        helpline_number=helpline,
        phone=phone,
        email=email,
        website_url=website_url,
        eligibility_criteria=eligibility,
        services_offered=services,
        is_free=True,
        source_attribution='Admin Curated Resource'
    )
    db.session.add(res)
    db.session.commit()

    flash(f"Legal aid resource '{name}' added successfully.", "success")
    return redirect(url_for('admin.legal_aid_manage'))

@admin_bp.route('/legal-aid/<int:res_id>/delete', methods=['POST'])
@admin_required
def legal_aid_delete(res_id):
    """Delete a legal aid resource."""
    res = db.session.get(LegalAidResource, res_id)
    if res:
        db.session.delete(res)
        db.session.commit()
        flash("Legal aid resource removed.", "info")
    return redirect(url_for('admin.legal_aid_manage'))

# --- QUERIES AUDIT & INQUIRIES ---
@admin_bp.route('/queries')
@admin_required
def queries_manage():
    """Audit log of user queries and classification performance."""
    queries = LegalQuery.query.order_by(LegalQuery.created_at.desc()).limit(100).all()
    return render_template('admin/queries_manage.html', queries=queries)

@admin_bp.route('/inquiries')
@admin_required
def inquiries_manage():
    """Manage consultation inquiries submitted by users."""
    inquiries = Inquiry.query.order_by(Inquiry.created_at.desc()).all()
    return render_template('admin/inquiries_manage.html', inquiries=inquiries)

@admin_bp.route('/inquiries/<int:inquiry_id>/status', methods=['POST'])
@admin_required
def update_inquiry_status(inquiry_id):
    """Update status of a consultation inquiry."""
    inquiry = db.session.get(Inquiry, inquiry_id)
    new_status = request.form.get('status')
    if inquiry and new_status in ['Pending', 'Contacted', 'Resolved', 'Closed']:
        inquiry.status = new_status
        db.session.commit()
        flash(f"Inquiry status updated to {new_status}.", "info")
    return redirect(url_for('admin.inquiries_manage'))

@admin_bp.route('/model/retrain', methods=['POST'])
@admin_required
def retrain_model():
    """Trigger retraining of the AI classifier model."""
    try:
        metrics = train_and_evaluate()
        # Reload artifacts into global singleton
        ai_classifier.load_artifacts()
        flash(f"AI Classifier retrained successfully! Test accuracy: {metrics['accuracy'] * 100:.1f}%.", "success")
    except Exception as e:
        flash(f"Retraining failed: {e}", "danger")
    return redirect(url_for('admin.dashboard'))
