from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """User account model supporting regular users and administrators."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='user', nullable=False) # 'user' or 'admin'
    phone = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)
    updated_at = db.Column(db.DateTime, default=utc_now, onupdate=utc_now)

    # Relationships
    queries = db.relationship('LegalQuery', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    inquiries = db.relationship('Inquiry', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic', cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'city': self.city,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M') if self.created_at else None
        }


class Lawyer(db.Model):
    """Lawyer profile for directory and matching engine."""
    __tablename__ = 'lawyers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    qualification = db.Column(db.String(150), nullable=False) # e.g., 'B.A. LL.B (Hons), LL.M'
    specialization = db.Column(db.String(80), nullable=False, index=True) # Matches legal category
    secondary_specialization = db.Column(db.String(80), nullable=True)
    experience_years = db.Column(db.Integer, nullable=False, default=1)
    city = db.Column(db.String(80), nullable=False, index=True)
    state = db.Column(db.String(80), nullable=False)
    languages_spoken = db.Column(db.String(200), nullable=False) # Comma separated
    bio = db.Column(db.Text, nullable=False)
    contact_email = db.Column(db.String(120), nullable=False)
    contact_phone = db.Column(db.String(25), nullable=True)
    office_address = db.Column(db.String(255), nullable=True)
    consultation_fee_type = db.Column(db.String(50), default='Standard') # 'Free', 'Low Cost', 'Standard'
    consultation_fee_amount = db.Column(db.String(50), default='Standard Consultation')
    is_pro_bono = db.Column(db.Boolean, default=False, index=True)
    is_verified = db.Column(db.Boolean, default=False, index=True)
    bar_council_reg_number = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, default=4.8)
    created_at = db.Column(db.DateTime, default=utc_now)

    # Relationships
    inquiries = db.relationship('Inquiry', backref='lawyer', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'qualification': self.qualification,
            'specialization': self.specialization,
            'secondary_specialization': self.secondary_specialization,
            'experience_years': self.experience_years,
            'city': self.city,
            'state': self.state,
            'languages': [lang.strip() for lang in self.languages_spoken.split(',') if lang.strip()],
            'bio': self.bio,
            'contact_email': self.contact_email,
            'office_address': self.office_address,
            'consultation_fee_type': self.consultation_fee_type,
            'consultation_fee_amount': self.consultation_fee_amount,
            'is_pro_bono': self.is_pro_bono,
            'is_verified': self.is_verified,
            'rating': self.rating
        }


class LegalAidResource(db.Model):
    """Free and low-cost legal aid clinic, university legal cell, or helpline."""
    __tablename__ = 'legal_aid_resources'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(180), nullable=False)
    organization_type = db.Column(db.String(80), nullable=False, index=True) 
    # Types: 'Legal Services Authority', 'Student Legal Aid Clinic', 'Pro Bono NGO', 'Public Helpline'
    category = db.Column(db.String(100), nullable=False, default='All Categories', index=True)
    city = db.Column(db.String(80), nullable=True, index=True)
    state = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    helpline_number = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    eligibility_criteria = db.Column(db.Text, nullable=False)
    services_offered = db.Column(db.Text, nullable=False)
    is_free = db.Column(db.Boolean, default=True)
    source_attribution = db.Column(db.String(150), nullable=False, default='Public Legal Aid Directory')
    last_verified_date = db.Column(db.String(50), default='October 2026')
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'organization_type': self.organization_type,
            'category': self.category,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'helpline_number': self.helpline_number,
            'email': self.email,
            'website_url': self.website_url,
            'eligibility_criteria': self.eligibility_criteria,
            'services_offered': self.services_offered,
            'is_free': self.is_free,
            'source_attribution': self.source_attribution,
            'last_verified_date': self.last_verified_date
        }


class LegalQuery(db.Model):
    """User legal query logs and AI classification records."""
    __tablename__ = 'legal_queries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    query_text = db.Column(db.Text, nullable=False)
    predicted_category = db.Column(db.String(80), nullable=False, index=True)
    confidence_score = db.Column(db.Float, default=0.0) # Percentage e.g. 85.5
    is_ambiguous = db.Column(db.Boolean, default=False)
    user_feedback_accurate = db.Column(db.Boolean, nullable=True)
    session_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            'id': self.id,
            'query_text': self.query_text,
            'predicted_category': self.predicted_category,
            'confidence_score': round(self.confidence_score, 1),
            'is_ambiguous': self.is_ambiguous,
            'user_feedback_accurate': self.user_feedback_accurate,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M') if self.created_at else None
        }


class Inquiry(db.Model):
    """Consultation or inquiry message sent to a lawyer."""
    __tablename__ = 'inquiries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    lawyer_id = db.Column(db.Integer, db.ForeignKey('lawyers.id', ondelete='CASCADE'), nullable=False)
    legal_category = db.Column(db.String(80), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    user_phone = db.Column(db.String(25), nullable=True)
    preferred_contact_time = db.Column(db.String(50), default='Anytime')
    status = db.Column(db.String(30), default='Pending') # 'Pending', 'Contacted', 'Resolved'
    created_at = db.Column(db.DateTime, default=utc_now)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'lawyer_id': self.lawyer_id,
            'legal_category': self.legal_category,
            'subject': self.subject,
            'message': self.message,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M') if self.created_at else None
        }


class Bookmark(db.Model):
    """Saved lawyers or legal aid resources for users."""
    __tablename__ = 'bookmarks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    item_type = db.Column(db.String(20), nullable=False) # 'lawyer' or 'legal_aid'
    item_id = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=utc_now)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'item_type', 'item_id', name='unique_user_bookmark'),
    )
