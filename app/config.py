import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def find_data_dir():
    """Finds data directory whether running from root, backend, or report package."""
    candidates = [
        BASE_DIR / 'app' / 'data',
        BASE_DIR.parent / 'data',
        BASE_DIR / 'data',
        Path('D:/JusticeGram/app/data')
    ]
    for c in candidates:
        if c.exists() and (c / 'model_artifacts').exists():
            return c
    return BASE_DIR / 'app' / 'data'

RESOLVED_DATA_DIR = find_data_dir()

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'justicegram-academic-secret-key-2026')
    
    # Database - SQLite by default with easy migration path to MySQL/PostgreSQL
    # In Vercel serverless environment, local filesystem root is read-only so use /tmp
    _default_db = str(BASE_DIR / 'justicegram.db')
    if os.environ.get('VERCEL'):
        import shutil
        tmp_db = Path('/tmp/justicegram.db')
        seed_db = RESOLVED_DATA_DIR / 'default_justicegram.db'
        if not tmp_db.exists() and seed_db.exists():
            try:
                shutil.copyfile(seed_db, tmp_db)
            except Exception:
                pass
        _default_db = str(tmp_db)

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', f"sqlite:///{_default_db}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AI Model Artifacts Paths
    DATA_DIR = RESOLVED_DATA_DIR
    MODEL_DIR = RESOLVED_DATA_DIR / 'model_artifacts'
    SAMPLE_DATA_PATH = DATA_DIR / 'legal_queries_sample.csv'
    CLASSIFIER_MODEL_PATH = MODEL_DIR / 'model.joblib'
    VECTORIZER_PATH = MODEL_DIR / 'tfidf.joblib'

    # Admin seed defaults
    ADMIN_NAME = os.environ.get('ADMIN_NAME', 'JusticeGram Administrator')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@justicegram.org')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Admin@Justice2026!')

    # Optional External AI API Key (kept backend-only, never exposed to frontend)
    EXTERNAL_AI_API_KEY = os.environ.get('EXTERNAL_AI_API_KEY', None)

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
