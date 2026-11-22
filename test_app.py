import unittest
import json
from app import create_app
from app.models import db, User, Lawyer, LegalAidResource, LegalQuery, Inquiry
from app.ai.preprocessor import clean_text, preprocess_for_model, is_query_ambiguous
from app.ai.classifier import ai_classifier
from app.ai.legal_knowledge import get_relevant_indian_laws, detect_subcategory

class JusticeGramTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        # Create demo admin user
        self.admin = User(name='Admin User', email='admin@test.com', role='admin')
        self.admin.set_password('AdminPass123!')
        db.session.add(self.admin)

        # Create demo regular student user
        self.user = User(name='Test Student', email='student@test.com', role='user', phone='9876543210', city='New Delhi')
        self.user.set_password('StudentPass123!')
        db.session.add(self.user)

        # Create demo lawyer (fictional demonstration profile)
        self.lawyer = Lawyer(
            name='Adv. Rahul Verma',
            qualification='LL.B, Faculty of Law, University of Delhi',
            specialization='Property and Real Estate',
            secondary_specialization='Civil Disputes',
            experience_years=11,
            city='New Delhi',
            state='Delhi NCR',
            languages_spoken='English, Hindi',
            bio='Specializes in tenant rights, illegal deposit deductions, and RERA disputes.',
            contact_email='adv.rahul.verma@demo-justicegram.org',
            is_pro_bono=True,
            is_verified=False,
            consultation_fee_type='Low Cost',
            consultation_fee_amount='₹400 / 30 mins'
        )
        db.session.add(self.lawyer)

        # Create demo legal aid resource
        self.aid = LegalAidResource(
            name='Test DLSA Clinic',
            organization_type='Legal Services Authority',
            category='All Categories',
            state='Delhi',
            eligibility_criteria='Open to all eligible citizens.',
            services_offered='Free legal advice.'
        )
        db.session.add(self.aid)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    # --- 1. NLP Preprocessor Tests ---
    def test_preprocessor_cleaning(self):
        raw = "   MY LANDLORD is NOT returning DEPOSIT!!  "
        cleaned = clean_text(raw)
        self.assertEqual(cleaned, "my landlord is not returning deposit")

    def test_ambiguity_detection(self):
        # Short / vague query
        ambiguous, reason = is_query_ambiguous("help")
        self.assertTrue(ambiguous)

        ambiguous, reason = is_query_ambiguous("i need help")
        self.assertTrue(ambiguous)

        # Specific query
        ambiguous, reason = is_query_ambiguous("My college has withheld my original 12th certificate and marksheet.")
        self.assertFalse(ambiguous)

    # --- 2. AI Classifier Tests & Statutory Retrieval ---
    def test_ai_classifier_property(self):
        query = "Landlord is refusing to refund security deposit after vacating flat."
        res = ai_classifier.classify(query)
        self.assertTrue(res['success'])
        self.assertEqual(res['category'], "Property and Real Estate")
        self.assertIn('important_documents', res)
        self.assertIn('suggested_next_steps', res)
        self.assertIn('relevant_laws', res)
        self.assertGreaterEqual(len(res['relevant_laws']), 1)
        self.assertIn('subcategory', res)
        self.assertIn('why_classified', res)

    def test_ai_classifier_cybercrime(self):
        query = "Lost money in UPI cyber fraud through unauthorized link click."
        res = ai_classifier.classify(query)
        self.assertTrue(res['success'])
        self.assertEqual(res['category'], "Cybercrime and Digital Issues")
        law_names = [l.get('law_name') or l.get('act_name', '') for l in res['relevant_laws']]
        self.assertTrue(any('Information Technology' in name for name in law_names))

    def test_ai_classifier_education(self):
        query = "University college is refusing to return my original 12th marksheet after completing degree."
        res = ai_classifier.classify(query)
        self.assertTrue(res['success'])
        self.assertEqual(res['category'], "Education-Related Legal Issues")

    def test_ai_classifier_manual_override(self):
        query = "Need help regarding a general issue."
        res = ai_classifier.classify(query, manual_category="Banking and Financial Issues")
        self.assertTrue(res['success'])
        self.assertEqual(res['category'], "Banking and Financial Issues")
        self.assertEqual(res['method_used'], "Manual User Selection")

    def test_ai_classifier_ambiguous(self):
        res = ai_classifier.classify("help please")
        self.assertTrue(res['success'])
        self.assertEqual(res['category'], "Other / Needs Clarification")
        self.assertTrue(res['is_ambiguous'])

    # --- 3. Authentication & Role Tests ---
    def test_user_registration(self):
        response = self.client.post('/auth/register', data={
            'name': 'New Student',
            'email': 'newstudent@college.edu',
            'password': 'Password123!',
            'confirm_password': 'Password123!',
            'phone': '9876500000',
            'city': 'Pune'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to JusticeGram", response.data)

        # Check DB
        new_u = User.query.filter_by(email='newstudent@college.edu').first()
        self.assertIsNotNone(new_u)
        self.assertEqual(new_u.role, 'user')

    def test_duplicate_registration_rejected(self):
        response = self.client.post('/auth/register', data={
            'name': 'Duplicate',
            'email': 'student@test.com',
            'password': 'Password123!',
            'confirm_password': 'Password123!'
        }, follow_redirects=True)
        self.assertIn(b"An account with this email address already exists", response.data)

    def test_user_login_and_logout(self):
        # Valid login
        resp = self.client.post('/auth/login', data={
            'email': 'student@test.com',
            'password': 'StudentPass123!'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Welcome back", resp.data)

        # Logout
        resp_logout = self.client.get('/auth/logout', follow_redirects=True)
        self.assertIn(b"signed out successfully", resp_logout.data)

    def test_admin_access_control(self):
        # Unauthenticated user visiting /admin/
        resp = self.client.get('/admin/', follow_redirects=True)
        self.assertIn(b"Administrator login required", resp.data)

        # Regular user logging in and visiting /admin/
        self.client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
        resp_forbidden = self.client.get('/admin/', follow_redirects=True)
        self.assertIn(b"Access denied. Administrator privileges required", resp_forbidden.data)

        # Admin user login and visiting /admin/
        self.client.get('/auth/logout')
        self.client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})
        resp_admin = self.client.get('/admin/', follow_redirects=True)
        self.assertEqual(resp_admin.status_code, 200)
        self.assertIn(b"System Administration", resp_admin.data)

    # --- 4. Route & Feature Tests ---
    def test_homepage(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Legal Help, Made Easier for Everyone", resp.data)

    def test_assistant_page_and_api(self):
        resp = self.client.get('/assistant')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"AI Legal Assistant", resp.data)

        # Test JSON classify API
        api_resp = self.client.post('/api/assistant/classify',
            data=json.dumps({'query_text': 'Mera landlord security deposit wapas nahi de raha'}),
            content_type='application/json'
        )
        self.assertEqual(api_resp.status_code, 200)
        data = json.loads(api_resp.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['classification']['category'], "Property and Real Estate")
        self.assertIn('lawyers', data)
        self.assertGreaterEqual(len(data['lawyers']), 1)
        self.assertIn('match_reasons', data['lawyers'][0])

    def test_lawyers_directory(self):
        resp = self.client.get('/lawyers/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Adv. Rahul Verma", resp.data)
        self.assertIn(b"Demonstration Notice", resp.data)

        # Test filter
        resp_filtered = self.client.get('/lawyers/?category=Property+and+Real+Estate')
        self.assertEqual(resp_filtered.status_code, 200)
        self.assertIn(b"Adv. Rahul Verma", resp_filtered.data)

    def test_legal_aid_directory(self):
        resp = self.client.get('/legal-aid/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Test DLSA Clinic", resp.data)

    def test_submit_consultation_inquiry(self):
        # Log in as user
        self.client.post('/auth/login', data={'email': 'student@test.com', 'password': 'StudentPass123!'})
        resp = self.client.post(f'/lawyers/{self.lawyer.id}/inquire', data={
            'subject': 'Rental issue assistance',
            'message': 'Need advice regarding security deposit return.',
            'phone': '9876543210',
            'legal_category': 'Property and Real Estate'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Your consultation inquiry has been submitted", resp.data)

        # Verify in DB
        inq = Inquiry.query.filter_by(user_id=self.user.id).first()
        self.assertIsNotNone(inq)
        self.assertEqual(inq.subject, 'Rental issue assistance')

    def test_admin_api_stats(self):
        # Log in as admin
        self.client.post('/auth/login', data={'email': 'admin@test.com', 'password': 'AdminPass123!'})
        resp = self.client.get('/admin/api/stats')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertIn('categories', data)
        self.assertEqual(len(data['categories']['labels']), 15)
        self.assertIn('lawyer_types', data)
        self.assertIn('inquiry_status', data)

if __name__ == '__main__':
    unittest.main()
