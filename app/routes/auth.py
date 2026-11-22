import re
from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g
from app.models import db, User

auth_bp = Blueprint('auth', __name__)

def login_required(view):
    """Decorator to protect routes requiring an authenticated user."""
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Please sign in to access this page.", "warning")
            return redirect(url_for('auth.login', next=request.url))
        return view(**kwargs)
    return wrapped_view

def admin_required(view):
    """Decorator to protect routes requiring administrator privileges."""
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Administrator login required.", "warning")
            return redirect(url_for('auth.login', next=request.url))
        if not g.user.is_admin:
            flash("Access denied. Administrator privileges required.", "danger")
            return redirect(url_for('main.index'))
        return view(**kwargs)
    return wrapped_view

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """User registration handler with server-side validation."""
    if g.user:
        return redirect(url_for('user.dashboard'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        phone = request.form.get('phone', '').strip()
        city = request.form.get('city', '').strip()

        errors = []

        if not name or len(name) < 2:
            errors.append("Please enter your full name (minimum 2 characters).")

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email or not re.match(email_regex, email):
            errors.append("Please provide a valid email address.")

        if not password or len(password) < 6:
            errors.append("Password must be at least 6 characters long.")

        if password != confirm_password:
            errors.append("Passwords do not match.")

        if not errors:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                errors.append("An account with this email address already exists. Please log in.")

        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('auth/register.html', name=name, email=email, phone=phone, city=city)

        # Create new user
        user = User(
            name=name,
            email=email,
            phone=phone,
            city=city,
            role='user'
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        # Log user in automatically
        session.clear()
        session['user_id'] = user.id
        session['user_role'] = user.role
        session['user_name'] = user.name

        flash(f"Welcome to JusticeGram, {user.name}! Your account has been created successfully.", "success")
        return redirect(url_for('user.dashboard'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """User and administrator authentication handler."""
    if g.user:
        if g.user.is_admin:
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('user.dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        remember = request.form.get('remember')

        if not email or not password:
            flash("Please enter both email and password.", "danger")
            return render_template('auth/login.html', email=email)

        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Invalid email address or password. Please try again.", "danger")
            return render_template('auth/login.html', email=email)

        # Set session
        session.clear()
        session['user_id'] = user.id
        session['user_role'] = user.role
        session['user_name'] = user.name
        if remember:
            session.permanent = True

        flash(f"Welcome back, {user.name}!", "success")

        next_page = request.args.get('next')
        if next_page and not next_page.startswith('http'):
            return redirect(next_page)

        if user.is_admin:
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('user.dashboard'))

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    """Log out current user and clear session."""
    session.clear()
    flash("You have been signed out successfully.", "info")
    return redirect(url_for('main.index'))
