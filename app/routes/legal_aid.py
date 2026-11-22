from flask import Blueprint, render_template, request, g, jsonify, flash, redirect, url_for
from app.models import db, LegalAidResource, Bookmark
from app.routes.auth import login_required
from app.ai.legal_knowledge import LEGAL_CATEGORIES

legal_aid_bp = Blueprint('legal_aid', __name__)

@legal_aid_bp.route('/')
def directory():
    """Searchable directory of Free Legal Aid Authorities, University Legal Cells,
    Pro Bono NGOs, and National Public Helplines.
    """
    selected_type = request.args.get('type', '').strip()
    selected_category = request.args.get('category', '').strip()
    selected_state = request.args.get('state', '').strip()
    search_keyword = request.args.get('q', '').strip()

    query = LegalAidResource.query

    if selected_type:
        query = query.filter(LegalAidResource.organization_type == selected_type)

    if selected_category:
        query = query.filter(
            (LegalAidResource.category == selected_category) | 
            (LegalAidResource.category == 'All Categories')
        )

    if selected_state:
        query = query.filter(LegalAidResource.state.ilike(f"%{selected_state}%"))

    if search_keyword:
        query = query.filter(
            (LegalAidResource.name.ilike(f"%{search_keyword}%")) |
            (LegalAidResource.services_offered.ilike(f"%{search_keyword}%")) |
            (LegalAidResource.city.ilike(f"%{search_keyword}%"))
        )

    resources = query.order_by(LegalAidResource.is_free.desc(), LegalAidResource.organization_type.asc()).all()

    # Pre-extract national emergency helplines for a dedicated quick-access card section
    helplines = LegalAidResource.query.filter(
        LegalAidResource.organization_type == 'Public Helpline'
    ).all()

    # Dynamic filter options
    all_states = sorted(list({r.state for r in LegalAidResource.query.all() if r.state}))
    org_types = ['Legal Services Authority', 'Student Legal Aid Clinic', 'Pro Bono NGO', 'Public Helpline']

    # Bookmarked items for logged-in user
    bookmarked_ids = set()
    if g.user:
        bookmarked_ids = {
            b.item_id for b in Bookmark.query.filter_by(user_id=g.user.id, item_type='legal_aid').all()
        }

    return render_template(
        'legal_aid/directory.html',
        resources=resources,
        helplines=helplines,
        all_states=all_states,
        org_types=org_types,
        selected_type=selected_type,
        selected_category=selected_category,
        selected_state=selected_state,
        search_keyword=search_keyword,
        bookmarked_ids=bookmarked_ids,
        categories=LEGAL_CATEGORIES
    )

@legal_aid_bp.route('/<int:resource_id>/bookmark', methods=['POST'])
@login_required
def toggle_bookmark(resource_id):
    """Toggle bookmark for a legal aid resource."""
    resource = db.session.get(LegalAidResource, resource_id)
    if not resource:
        return jsonify({'success': False, 'error': 'Resource not found'}), 404

    existing = Bookmark.query.filter_by(
        user_id=g.user.id, item_type='legal_aid', item_id=resource.id
    ).first()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        bookmarked = False
        message = "Removed from your saved resources."
    else:
        new_bm = Bookmark(user_id=g.user.id, item_type='legal_aid', item_id=resource.id)
        db.session.add(new_bm)
        db.session.commit()
        bookmarked = True
        message = "Saved to your dashboard bookmarks."

    if request.is_json:
        return jsonify({'success': True, 'bookmarked': bookmarked, 'message': message})
    flash(message, "info")
    return redirect(request.referrer or url_for('legal_aid.directory'))
