from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from app.models import db, LegalQuery, Inquiry, Bookmark, Lawyer, LegalAidResource
from app.routes.auth import login_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
@login_required
def dashboard():
    """User personal dashboard displaying query history,
    submitted inquiries, saved bookmarks, and profile management.
    """
    # 1. Fetch user's query history
    user_queries = LegalQuery.query.filter_by(user_id=g.user.id).order_by(LegalQuery.created_at.desc()).all()

    # 2. Fetch user's consultation inquiries
    inquiries = Inquiry.query.filter_by(user_id=g.user.id).order_by(Inquiry.created_at.desc()).all()

    # 3. Fetch user's bookmarked lawyers and legal aid resources
    lawyer_bookmarks = Bookmark.query.filter_by(user_id=g.user.id, item_type='lawyer').all()
    lawyer_ids = [b.item_id for b in lawyer_bookmarks]
    saved_lawyers = Lawyer.query.filter(Lawyer.id.in_(lawyer_ids)).all() if lawyer_ids else []

    aid_bookmarks = Bookmark.query.filter_by(user_id=g.user.id, item_type='legal_aid').all()
    aid_ids = [b.item_id for b in aid_bookmarks]
    saved_aid = LegalAidResource.query.filter(LegalAidResource.id.in_(aid_ids)).all() if aid_ids else []

    stats = {
        'total_queries': len(user_queries),
        'total_inquiries': len(inquiries),
        'saved_lawyers_count': len(saved_lawyers),
        'saved_aid_count': len(saved_aid)
    }

    return render_template(
        'user/dashboard.html',
        stats=stats,
        queries=user_queries,
        inquiries=inquiries,
        saved_lawyers=saved_lawyers,
        saved_aid=saved_aid
    )

@user_bp.route('/profile/update', methods=['POST'])
@login_required
def update_profile():
    """Update user contact details."""
    name = request.form.get('name', '').strip()
    phone = request.form.get('phone', '').strip()
    city = request.form.get('city', '').strip()

    if not name:
        flash("Name cannot be empty.", "danger")
        return redirect(url_for('user.dashboard'))

    g.user.name = name
    g.user.phone = phone
    g.user.city = city
    db.session.commit()

    flash("Profile updated successfully.", "success")
    return redirect(url_for('user.dashboard'))

@user_bp.route('/password/change', methods=['POST'])
@login_required
def change_password():
    """Change account password."""
    current_password = request.form.get('current_password', '')
    new_password = request.form.get('new_password', '')
    confirm_password = request.form.get('confirm_password', '')

    if not g.user.check_password(current_password):
        flash("Current password is incorrect.", "danger")
        return redirect(url_for('user.dashboard'))

    if len(new_password) < 6:
        flash("New password must be at least 6 characters long.", "danger")
        return redirect(url_for('user.dashboard'))

    if new_password != confirm_password:
        flash("New passwords do not match.", "danger")
        return redirect(url_for('user.dashboard'))

    g.user.set_password(new_password)
    db.session.commit()

    flash("Password changed successfully.", "success")
    return redirect(url_for('user.dashboard'))
