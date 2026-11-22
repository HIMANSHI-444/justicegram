from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import db, Lawyer, LegalAidResource, LegalQuery
from app.ai.legal_knowledge import LEGAL_CATEGORIES

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Landing page featuring hero section, interactive query prompt,
    how it works, categories, featured lawyers, and free legal aid.
    """
    # Fetch featured verified lawyers
    featured_lawyers = Lawyer.query.filter_by(is_verified=True).order_by(Lawyer.rating.desc()).limit(3).all()
    if not featured_lawyers:
        featured_lawyers = Lawyer.query.limit(3).all()

    # Fetch featured pro bono / student legal aid clinics
    featured_aid = LegalAidResource.query.filter(
        LegalAidResource.organization_type.in_(['Legal Services Authority', 'Student Legal Aid Clinic', 'Public Helpline'])
    ).limit(3).all()

    # System statistics for credibility indicators (attributable demo stats)
    stats = {
        'total_lawyers': Lawyer.query.count(),
        'total_aid_centers': LegalAidResource.query.count(),
        'queries_assisted': LegalQuery.query.count()
    }

    return render_template(
        'index.html',
        featured_lawyers=featured_lawyers,
        featured_aid=featured_aid,
        stats=stats,
        categories=LEGAL_CATEGORIES
    )

@main_bp.route('/about')
def about():
    """About JusticeGram and academic project background."""
    return render_template('about.html')

@main_bp.route('/how-it-works')
def how_it_works():
    """Detailed architectural explanation of the AI categorization & legal matching pipeline."""
    return render_template('how_it_works.html')

@main_bp.route('/faqs')
def faqs():
    """Frequently Asked Questions regarding legal queries, free aid, and lawyers."""
    return render_template('faqs.html')

@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact & feedback form."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if name and email and message:
            flash("Thank you for reaching out to the JusticeGram team. We will get back to you shortly.", "success")
            return redirect(url_for('main.contact'))
        flash("Please complete all required fields.", "warning")
    return render_template('contact.html')

@main_bp.route('/disclaimer')
def disclaimer():
    """Full legal disclaimer and informational advisory terms."""
    return render_template('disclaimer.html')
