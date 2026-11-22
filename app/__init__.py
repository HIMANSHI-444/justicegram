import os
from flask import Flask, session, g, render_template
from app.config import config_by_name
from app.models import db, User
from app.ai.legal_knowledge import LEGAL_CATEGORIES

def create_app(config_name=None):
    """Flask application factory."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')

    base_dir = os.path.abspath(os.path.dirname(__file__)) # .../app
    root_dir = os.path.dirname(base_dir) # parent of app

    # Robust Template folder resolution
    template_candidates = [
        os.path.join(base_dir, 'templates'),
        os.path.join(root_dir, '..', 'frontend', 'templates'),
        os.path.join(root_dir, 'frontend', 'templates'),
        os.path.join(root_dir, 'templates'),
        'D:/JusticeGram/app/templates',
        'c:/Users/kalya/OneDrive/Desktop/ws/app/templates'
    ]
    template_folder = next((p for p in template_candidates if os.path.isdir(p)), os.path.join(base_dir, 'templates'))

    # Robust Static folder resolution
    static_candidates = [
        os.path.join(base_dir, 'static'),
        os.path.join(root_dir, '..', 'frontend', 'static'),
        os.path.join(root_dir, 'frontend', 'static'),
        os.path.join(root_dir, 'static'),
        'D:/JusticeGram/app/static',
        'c:/Users/kalya/OneDrive/Desktop/ws/app/static'
    ]
    static_folder = next((p for p in static_candidates if os.path.isdir(p)), os.path.join(base_dir, 'static'))

    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Initialize extensions
    db.init_app(app)

    # Load logged-in user into Flask 'g' context
    @app.before_request
    def load_logged_in_user():
        user_id = session.get('user_id')
        if user_id is None:
            g.user = None
        else:
            g.user = db.session.get(User, user_id)

    # Inject global context variables into templates
    @app.context_processor
    def inject_globals():
        return {
            'legal_categories': LEGAL_CATEGORIES,
            'current_user': g.user,
            'app_name': 'JusticeGram',
            'app_tagline': 'AI-Powered Legal Assistance Platform'
        }

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    # Register blueprints
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.assistant import assistant_bp
    from app.routes.lawyers import lawyers_bp
    from app.routes.legal_aid import legal_aid_bp
    from app.routes.user_dashboard import user_bp
    from app.routes.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(assistant_bp)
    app.register_blueprint(lawyers_bp, url_prefix='/lawyers')
    app.register_blueprint(legal_aid_bp, url_prefix='/legal-aid')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
