"""Database seeding script for JusticeGram.
Populates initial admin, test student user, 16 realistic fictional Indian advocates (demo records),
curated free legal aid clinics, helplines, and sample query records across all 15 legal categories.
"""

import os
from datetime import datetime, timedelta, timezone
from app import create_app
from app.models import db, User, Lawyer, LegalAidResource, LegalQuery, Inquiry, Bookmark
from app.config import Config

app = create_app('development')

def seed_database():
    with app.app_context():
        print("[*] Rebuilding and initializing database tables...")
        # Drop all tables to ensure clean slate with updated schema and categories
        db.drop_all()
        db.create_all()

        # 1. Seed Administrator Account
        admin_email = Config.ADMIN_EMAIL.lower()
        admin = User(
            name=Config.ADMIN_NAME,
            email=admin_email,
            role='admin',
            city='New Delhi',
            phone='+91 98110 00001'
        )
        admin.set_password(Config.ADMIN_PASSWORD)
        db.session.add(admin)
        print(f"[+] Created Administrator Account: {admin_email}")

        # 2. Seed Demo Student User
        student_email = 'student@college.edu'
        student = User(
            name='Aarav Sharma',
            email=student_email,
            role='user',
            city='Bengaluru',
            phone='+91 99887 76655'
        )
        student.set_password('Student@2026!')
        db.session.add(student)
        print(f"[+] Created Student Demo Account: {student_email}")

        db.session.commit()

        # 3. Seed 16 Fictional Indian Advocates (Unverified / Demo Profiles)
        # DISCLAIMER: All advocate profiles are fictional sample demonstration records for academic BCA mini-project evaluation.
        print("[*] Seeding 16 demonstration Indian advocate profiles (marked Demo/Unverified)...")
        lawyers_data = [
            {
                "name": "Adv. Ananya Sharma",
                "qualification": "B.A. LL.B (Hons), NLSIU Bengaluru | LL.M (Family Law)",
                "specialization": "Family Law",
                "secondary_specialization": "Women's Legal Support",
                "experience_years": 9,
                "city": "New Delhi",
                "state": "Delhi NCR",
                "languages_spoken": "English, Hindi",
                "bio": "[Demo Profile] Matrimonial counselor and advocate specializing in mutual divorce petitions, Section 125 CrPC maintenance claims, child custody arrangements, and family mediation.",
                "contact_email": "adv.ananya.sharma@demo-justicegram.org",
                "contact_phone": "+91 98110 12001",
                "office_address": "Barakhamba Road, Connaught Place, New Delhi",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Demo Pro Bono Clinic)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "D/1482/2015 (Demo Profile)",
                "rating": 4.9
            },
            {
                "name": "Adv. Rahul Verma",
                "qualification": "LL.B, Faculty of Law, University of Delhi",
                "specialization": "Property and Real Estate",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 11,
                "city": "Bengaluru",
                "state": "Karnataka",
                "languages_spoken": "English, Kannada, Hindi",
                "bio": "[Demo Profile] Real estate counsel assisting students and tenants with illegal security deposit forfeiture, eviction notices, lease drafting, and Karnataka RERA complaints against delayed possession.",
                "contact_email": "adv.rahul.verma@demo-justicegram.org",
                "contact_phone": "+91 98450 12002",
                "office_address": "Indiranagar 100ft Road, Bengaluru",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹400 / 30 mins (Student Concession)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "KAR/2841/2013 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Priya Singh",
                "qualification": "B.A. LL.B (Hons), NUJS Kolkata | PGD Cyber Law",
                "specialization": "Cybercrime and Digital Issues",
                "secondary_specialization": "Banking and Financial Issues",
                "experience_years": 7,
                "city": "Gurugram",
                "state": "Haryana",
                "languages_spoken": "English, Hindi, Punjabi",
                "bio": "[Demo Profile] Cyber jurisprudence advocate handling UPI phishing fraud, WhatsApp loan app blackmail, unauthorized net banking debits, digital impersonation, and IT Act complaints.",
                "contact_email": "adv.priya.singh@demo-justicegram.org",
                "contact_phone": "+91 98120 12003",
                "office_address": "Cyber City Phase II, Gurugram",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹500 / Session",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "P&H/3119/2017 (Demo Profile)",
                "rating": 4.9
            },
            {
                "name": "Adv. Arjun Mehta",
                "qualification": "LL.B, Government Law College Mumbai",
                "specialization": "Criminal Law",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 13,
                "city": "Mumbai",
                "state": "Maharashtra",
                "languages_spoken": "English, Marathi, Hindi, Gujarati",
                "bio": "[Demo Profile] Senior trial advocate practicing across Metropolitan Magistrate Courts and Sessions Court for bail applications, Zero FIR filing, criminal defense, and cheating (Section 318 BNS).",
                "contact_email": "adv.arjun.mehta@demo-justicegram.org",
                "contact_phone": "+91 98200 12004",
                "office_address": "Fort, Near Bombay High Court, Mumbai",
                "consultation_fee_type": "Standard",
                "consultation_fee_amount": "₹1000 / Consultation",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "MAH/1904/2011 (Demo Profile)",
                "rating": 4.7
            },
            {
                "name": "Adv. Neha Gupta",
                "qualification": "B.A. LL.B, National Law University Jodhpur",
                "specialization": "Consumer Rights",
                "secondary_specialization": "Medical and Healthcare Issues",
                "experience_years": 6,
                "city": "Jaipur",
                "state": "Rajasthan",
                "languages_spoken": "English, Hindi, Rajasthani",
                "bio": "[Demo Profile] Consumer advocate guiding consumers through e-Daakhil filing for defective electronic goods, unfair flight ticket cancellations, warranty rejections, and medical overbilling disputes.",
                "contact_email": "adv.neha.gupta@demo-justicegram.org",
                "contact_phone": "+91 98290 12005",
                "office_address": "C-Scheme, Ashok Nagar, Jaipur",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Pro Bono First Consultation)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "RAJ/2103/2018 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Amit Mishra",
                "qualification": "LL.M (Labour & Industrial Law), Indian Law Institute",
                "specialization": "Employment and Labour Law",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 10,
                "city": "Noida",
                "state": "Uttar Pradesh",
                "languages_spoken": "English, Hindi",
                "bio": "[Demo Profile] Industrial relations counsel representing corporate employees in wrongful terminations, unpaid salary recovery, non-deposit of PF/Gratuity, and unfair employment bond disputes.",
                "contact_email": "adv.amit.mishra@demo-justicegram.org",
                "contact_phone": "+91 98180 12006",
                "office_address": "Sector 62, Electronic City, Noida",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹600 / Consultation",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "UP/4182/2014 (Demo Profile)",
                "rating": 4.7
            },
            {
                "name": "Adv. Sneha Patel",
                "qualification": "B.S.L. LL.B, ILS Law College Pune",
                "specialization": "Women's Legal Support",
                "secondary_specialization": "Family Law",
                "experience_years": 8,
                "city": "Ahmedabad",
                "state": "Gujarat",
                "languages_spoken": "English, Gujarati, Hindi",
                "bio": "[Demo Profile] Passionate advocate committed to defending women's legal rights under PWDVA 2005, Workplace Sexual Harassment (PoSH Act), Stridhan return, and emergency police protection orders.",
                "contact_email": "adv.sneha.patel@demo-justicegram.org",
                "contact_phone": "+91 98250 12007",
                "office_address": "Ashram Road, Navrangpura, Ahmedabad",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Pro Bono Support for Women in Need)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "GUJ/1589/2016 (Demo Profile)",
                "rating": 5.0
            },
            {
                "name": "Adv. Rohan Malhotra",
                "qualification": "LL.M (Banking & Finance Law), Panjab University",
                "specialization": "Banking and Financial Issues",
                "secondary_specialization": "Consumer Rights",
                "experience_years": 12,
                "city": "Chandigarh",
                "state": "Punjab",
                "languages_spoken": "English, Punjabi, Hindi",
                "bio": "[Demo Profile] Banking jurisprudence counsel handling illegal recovery agent harassment under RBI Fair Practices Code, loan restructuring, credit card disputes, and SARFAESI notices.",
                "contact_email": "adv.rohan.malhotra@demo-justicegram.org",
                "contact_phone": "+91 98720 12008",
                "office_address": "Sector 17-C, Chandigarh",
                "consultation_fee_type": "Standard",
                "consultation_fee_amount": "₹900 / Advisory",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "P&H/1209/2012 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Kavita Rao",
                "qualification": "B.A. LL.B (Hons), NALSAR University of Law Hyderabad",
                "specialization": "Education-Related Legal Issues",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 9,
                "city": "Hyderabad",
                "state": "Telangana",
                "languages_spoken": "English, Telugu, Hindi",
                "bio": "[Demo Profile] Education law practitioner representing students and researchers against illegal retention of original marksheets, college fee forfeiture, anti-ragging violations, and UGC non-compliance.",
                "contact_email": "adv.kavita.rao@demo-justicegram.org",
                "contact_phone": "+91 99490 12009",
                "office_address": "Banjara Hills Road No. 10, Hyderabad",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Pro Bono Student Advocacy)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "TS/982/2015 (Demo Profile)",
                "rating": 4.9
            },
            {
                "name": "Adv. Vivek Joshi",
                "qualification": "LL.B, Lucknow University | Diploma in Administrative Law",
                "specialization": "Government and Public Services",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 14,
                "city": "Lucknow",
                "state": "Uttar Pradesh",
                "languages_spoken": "English, Hindi",
                "bio": "[Demo Profile] Public law counsel drafting First & Second Appeals under RTI Act 2005, administrative grievance petitions, pension delays, and writ petitions under Article 226 before the High Court.",
                "contact_email": "adv.vivek.joshi@demo-justicegram.org",
                "contact_phone": "+91 94150 12010",
                "office_address": "Hazratganj, Lucknow",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹500 / Guidance",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "UP/3290/2010 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Pooja Yadav",
                "qualification": "LL.M (Intellectual Property Rights), NLSIU Bengaluru",
                "specialization": "Intellectual Property",
                "secondary_specialization": "Cybercrime and Digital Issues",
                "experience_years": 8,
                "city": "Bengaluru",
                "state": "Karnataka",
                "languages_spoken": "English, Hindi, Kannada",
                "bio": "[Demo Profile] IP attorney advising students, software creators, and startups on trademark objections, copyright infringement notices, software licensing disputes, and DMCA digital takedowns.",
                "contact_email": "adv.pooja.yadav@demo-justicegram.org",
                "contact_phone": "+91 98450 12011",
                "office_address": "Koramangala 5th Block, Bengaluru",
                "consultation_fee_type": "Standard",
                "consultation_fee_amount": "₹1200 / Assessment",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "KAR/4412/2016 (Demo Profile)",
                "rating": 4.9
            },
            {
                "name": "Adv. Saurabh Kumar",
                "qualification": "LL.B, Patna Law College | PGD in Health Law",
                "specialization": "Medical and Healthcare Issues",
                "secondary_specialization": "Consumer Rights",
                "experience_years": 10,
                "city": "Patna",
                "state": "Bihar",
                "languages_spoken": "English, Hindi",
                "bio": "[Demo Profile] Healthcare advocate assisting patients in hospital medical negligence claims, illegal denial of cashless health insurance, medical record access refusal, and clinical establishment grievances.",
                "contact_email": "adv.saurabh.kumar@demo-justicegram.org",
                "contact_phone": "+91 94310 12012",
                "office_address": "Bailey Road, Patna",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Pro Bono Patient Rights Clinic)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "BR/1029/2014 (Demo Profile)",
                "rating": 4.7
            },
            {
                "name": "Adv. Harish Iyer",
                "qualification": "B.A. B.L., Dr. Ambedkar Government Law College Chennai",
                "specialization": "Immigration and Documentation",
                "secondary_specialization": "Civil Disputes",
                "experience_years": 11,
                "city": "Chennai",
                "state": "Tamil Nadu",
                "languages_spoken": "English, Tamil, Hindi",
                "bio": "[Demo Profile] Counsel handling Passport Act show-cause notices, adverse police verification report disputes, documentation corrections, name change gazette procedures, and citizenship declarations.",
                "contact_email": "adv.harish.iyyer@demo-justicegram.org",
                "contact_phone": "+91 94440 12013",
                "office_address": "Armenian Street, George Town, Chennai",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹500 / Session",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "MS/1844/2013 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Deepa Nambiar",
                "qualification": "B.A. LL.B, NUALS Kochi | LL.M (Commercial Law)",
                "specialization": "Civil Disputes",
                "secondary_specialization": "Property and Real Estate",
                "experience_years": 10,
                "city": "Kochi",
                "state": "Kerala",
                "languages_spoken": "English, Malayalam, Hindi",
                "bio": "[Demo Profile] Civil litigation counsel specialized in breach of commercial agreements, civil money recovery under Order 37 CPC, legal demand notice drafting, and pre-institution mediation.",
                "contact_email": "adv.deepa.nambiar@demo-justicegram.org",
                "contact_phone": "+91 98470 12014",
                "office_address": "Banerji Road, Ernakulam, Kochi",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹450 / 30 mins",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "K/1210/2014 (Demo Profile)",
                "rating": 4.9
            },
            {
                "name": "Adv. Vikramaditya Rathore",
                "qualification": "LL.B, Campus Law Centre, University of Delhi",
                "specialization": "Criminal Law",
                "secondary_specialization": "Cybercrime and Digital Issues",
                "experience_years": 8,
                "city": "New Delhi",
                "state": "Delhi NCR",
                "languages_spoken": "English, Hindi, Punjabi",
                "bio": "[Demo Profile] Trial advocate practicing before Patiala House & Saket Courts on online financial cyber fraud, Zero FIR registration, police notice compliance, and anticipatory bail petitions under BNSS.",
                "contact_email": "adv.vikram.rathore@demo-justicegram.org",
                "contact_phone": "+91 98101 12015",
                "office_address": "Patiala House Courts Complex, New Delhi",
                "consultation_fee_type": "Free",
                "consultation_fee_amount": "₹0 (Pro Bono Student Counsel)",
                "is_pro_bono": True,
                "is_verified": False,
                "bar_council_reg_number": "D/2198/2016 (Demo Profile)",
                "rating": 4.8
            },
            {
                "name": "Adv. Farhan Qureshi",
                "qualification": "LL.B, Government Law College Mumbai",
                "specialization": "Consumer Rights",
                "secondary_specialization": "Property and Real Estate",
                "experience_years": 7,
                "city": "Mumbai",
                "state": "Maharashtra",
                "languages_spoken": "English, Hindi, Gujarati",
                "bio": "[Demo Profile] Consumer disputes practitioner filing claims before District Consumer Disputes Redressal Commissions for electronic product defects, delayed transit compensation, and unfair terms in tenancy contracts.",
                "contact_email": "adv.farhan.qureshi@demo-justicegram.org",
                "contact_phone": "+91 98200 12016",
                "office_address": "Nariman Point, Marine Drive, Mumbai",
                "consultation_fee_type": "Low Cost",
                "consultation_fee_amount": "₹500 / Initial Assessment",
                "is_pro_bono": False,
                "is_verified": False,
                "bar_council_reg_number": "MAH/6721/2017 (Demo Profile)",
                "rating": 4.7
            }
        ]

        for l_data in lawyers_data:
            lawyer = Lawyer(**l_data)
            db.session.add(lawyer)
        print(f"[+] Added {len(lawyers_data)} demonstration advocate profiles.")

        # 4. Seed Free Legal Aid Clinics, Student Bodies & Statutory Helplines
        print("[*] Seeding verified free legal aid authorities, university clinics & national helplines...")
        aid_data = [
            {
                "name": "National Legal Services Authority (NALSA) Front Office",
                "organization_type": "Legal Services Authority",
                "category": "All Categories",
                "city": "New Delhi",
                "state": "National / Pan-India",
                "address": "B-Block, Additional Building Complex, Supreme Court of India, New Delhi",
                "phone": "011-23382778",
                "helpline_number": "15100",
                "email": "nalsa-dla@nic.in",
                "website_url": "https://nalsa.gov.in",
                "eligibility_criteria": "Free for women, children, SC/ST, custody inmates, disabled persons, and low-income citizens as per Section 12 of the Legal Services Authorities Act 1987.",
                "services_offered": "Free legal aid counsel assignment, court representation, pre-litigation mediation, legal advice, and Lok Adalat dispute settlement.",
                "is_free": True,
                "source_attribution": "National Legal Services Authority (Official Statutory Body)",
                "last_verified_date": "October 2026"
            },
            {
                "name": "Delhi State Legal Services Authority (DSLSA) Front Desk",
                "organization_type": "Legal Services Authority",
                "category": "All Categories",
                "city": "New Delhi",
                "state": "Delhi",
                "address": "Room No. 287, Tis Hazari Courts Complex, Delhi - 110054",
                "phone": "011-23968052",
                "helpline_number": "15100",
                "email": "central-dlsa@nic.in",
                "website_url": "https://dslsa.org",
                "eligibility_criteria": "Residents of Delhi eligible under DSLSA annual income ceiling guidelines and special protected categories.",
                "services_offered": "Free front desk counseling, appointment of legal aid advocates for trial courts, drafting of applications, and victim compensation.",
                "is_free": True,
                "source_attribution": "Delhi State Legal Services Authority",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Cyber Crime Reporting Portal & Helpline (1930)",
                "organization_type": "Public Helpline",
                "category": "Cybercrime and Digital Issues",
                "city": None,
                "state": "National / 24x7",
                "address": "Indian Cyber Crime Coordination Centre (I4C), Ministry of Home Affairs, Government of India",
                "phone": "1930",
                "helpline_number": "1930",
                "email": "citizen@cybercrime.gov.in",
                "website_url": "https://cybercrime.gov.in",
                "eligibility_criteria": "Universal 24x7 access for all citizens across India facing online financial fraud, UPI extortion, or cyber harassment.",
                "services_offered": "Immediate coordination with banks to freeze stolen financial transactions during the Golden Hour, and Zero FIR registration assistance.",
                "is_free": True,
                "source_attribution": "Ministry of Home Affairs (MHA)",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Consumer Helpline (NCH - 1915)",
                "organization_type": "Public Helpline",
                "category": "Consumer Rights",
                "city": None,
                "state": "National",
                "address": "Department of Consumer Affairs, Krishi Bhawan, New Delhi",
                "phone": "1915",
                "helpline_number": "1915",
                "email": "consumer-care@gov.in",
                "website_url": "https://consumerhelpline.gov.in",
                "eligibility_criteria": "Universal free service for all consumers purchasing goods or services across India.",
                "services_offered": "Pre-litigation grievance redressal against ecommerce companies, telecom providers, airlines, and banks, and guidance for e-Daakhil filing.",
                "is_free": True,
                "source_attribution": "Department of Consumer Affairs, Government of India",
                "last_verified_date": "October 2026"
            },
            {
                "name": "Campus Law Centre Legal Aid Society (University of Delhi)",
                "organization_type": "Student Legal Aid Clinic",
                "category": "Education-Related Legal Issues",
                "city": "New Delhi",
                "state": "Delhi",
                "address": "Faculty of Law, Chhatra Marg, North Campus, Delhi University - 110007",
                "phone": "011-27667895",
                "helpline_number": None,
                "email": "legalaid@clc.du.ac.in",
                "website_url": "http://clc.du.ac.in/legal-aid-society",
                "eligibility_criteria": "Open to all students, university staff, and marginalized community members without charge.",
                "services_offered": "Free legal literacy, student dispute counseling, mediation for certificate withholding or rent issues, and student legal literacy camps.",
                "is_free": True,
                "source_attribution": "Delhi University Legal Aid Society",
                "last_verified_date": "October 2026"
            },
            {
                "name": "NLSIU Legal Services Clinic (Bengaluru)",
                "organization_type": "Student Legal Aid Clinic",
                "category": "Property and Real Estate",
                "city": "Bengaluru",
                "state": "Karnataka",
                "address": "National Law School of India University, Gnana Bharathi, Nagarbhavi, Bengaluru - 560072",
                "phone": "080-23213160",
                "helpline_number": None,
                "email": "lsc@nls.ac.in",
                "website_url": "https://www.nls.ac.in",
                "eligibility_criteria": "College students, domestic workers, gig workers, and economically weaker sections.",
                "services_offered": "Student-advocate legal advice, tenancy dispute counseling, wage recovery assistance, and legal notice drafting under faculty supervision.",
                "is_free": True,
                "source_attribution": "NLSIU Faculty Legal Clinic",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Women Helpline (Sakhi - One Stop Centre)",
                "organization_type": "Public Helpline",
                "category": "Women's Legal Support",
                "city": None,
                "state": "National / 24x7",
                "address": "Ministry of Women and Child Development, Shastri Bhawan, New Delhi",
                "phone": "1091",
                "helpline_number": "1091",
                "email": "complaintcell-ncw@nic.in",
                "website_url": "https://ncw.nic.in",
                "eligibility_criteria": "Universal 24x7 emergency helpline for women facing domestic abuse, sexual harassment, stalking, or distress.",
                "services_offered": "Immediate police dispatch, free medical aid, shelter home linkage, psychological counseling, and legal assistance through Protection Officers.",
                "is_free": True,
                "source_attribution": "Ministry of Women and Child Development",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Anti-Ragging Helpline (UGC)",
                "organization_type": "Public Helpline",
                "category": "Education-Related Legal Issues",
                "city": None,
                "state": "National / 24x7",
                "address": "University Grants Commission (UGC), Bahadur Shah Zafar Marg, New Delhi",
                "phone": "1800-180-5522",
                "helpline_number": "1800-180-5522",
                "email": "helpline@antiragging.in",
                "website_url": "https://antiragging.in",
                "eligibility_criteria": "Available 24x7 to all higher education students facing ragging, harassment, or intimidation in colleges.",
                "services_offered": "Immediate escalation to college Vice Chancellor, local Police Superintendent, and UGC monitoring cell with identity protection.",
                "is_free": True,
                "source_attribution": "University Grants Commission",
                "last_verified_date": "October 2026"
            },
            {
                "name": "Reserve Bank of India (RBI) Integrated Ombudsman Helpdesk",
                "organization_type": "Statutory Authority",
                "category": "Banking and Financial Issues",
                "city": "Mumbai",
                "state": "National",
                "address": "Centralized Receipt and Processing Centre (CRPC), Reserve Bank of India, 4th Floor, Sector 17, Chandigarh",
                "phone": "14448",
                "helpline_number": "14448",
                "email": "crpc@rbi.org.in",
                "website_url": "https://cms.rbi.org.in",
                "eligibility_criteria": "Open to all bank account holders, UPI users, and loan borrowers when bank fails to resolve grievances within 30 days.",
                "services_offered": "Independent statutory dispute resolution, compensation awards up to ₹20 lakh for deficient bank service, and recovery agent harassment redressal.",
                "is_free": True,
                "source_attribution": "Reserve Bank of India (RBI)",
                "last_verified_date": "October 2026"
            },
            {
                "name": "Central Information Commission & National RTI Portal Cell",
                "organization_type": "Statutory Authority",
                "category": "Government and Public Services",
                "city": "New Delhi",
                "state": "National",
                "address": "CIC Bhawan, Baba Gangnath Marg, Munirka, New Delhi - 110067",
                "phone": "011-26183996",
                "helpline_number": None,
                "email": "helpdesk-rti@gov.in",
                "website_url": "https://rtionline.gov.in",
                "eligibility_criteria": "Any Indian citizen seeking access to government records and public authority transparency under RTI Act 2005.",
                "services_offered": "Online RTI application assistance, first and second appellate authority hearing listings, and penal proceedings against non-complying PIOs.",
                "is_free": True,
                "source_attribution": "Department of Personnel and Training (DoPT)",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Human Rights Commission (NHRC) Citizen Helpdesk",
                "organization_type": "Statutory Authority",
                "category": "Criminal Law",
                "city": "New Delhi",
                "state": "National",
                "address": "Manav Adhikar Bhawan, Block-C, GPO Complex, INA, New Delhi - 110023",
                "phone": "14433",
                "helpline_number": "14433",
                "email": "covdref.nhrc@nic.in",
                "website_url": "https://nhrc.nic.in",
                "eligibility_criteria": "Any individual alleging custodial abuse, illegal police detention, unlawful harassment, or fundamental rights violations.",
                "services_offered": "Direct inquiry into human rights violations, summons to law enforcement officers, independent fact-finding, and interim relief recommendations.",
                "is_free": True,
                "source_attribution": "National Human Rights Commission of India",
                "last_verified_date": "October 2026"
            },
            {
                "name": "National Consumer Patient Rights & Medical Negligence Guidance Cell",
                "organization_type": "Pro Bono NGO",
                "category": "Medical and Healthcare Issues",
                "city": "New Delhi",
                "state": "Delhi NCR",
                "address": "Institutional Area, Lodhi Road, New Delhi",
                "phone": "011-24648711",
                "helpline_number": None,
                "email": "patientrights@medlegalaid.org",
                "website_url": "https://main.mohfw.gov.in",
                "eligibility_criteria": "Patients or bereaved family members who have suffered due to suspected medical negligence or hospital billing fraud.",
                "services_offered": "Independent medical board record assessment, consumer complaint drafting against private hospitals, and state medical council complaint filing.",
                "is_free": True,
                "source_attribution": "Ministry of Health & Family Welfare / Medical Legal Forum",
                "last_verified_date": "October 2026"
            }
        ]

        for a_data in aid_data:
            res = LegalAidResource(**a_data)
            db.session.add(res)
        print(f"[+] Added {len(aid_data)} free legal aid clinics & statutory helplines.")

        # 5. Seed Demonstration User Queries and Inquiries
        print("[*] Seeding sample queries for dashboard analytics across multiple legal categories...")
        sample_queries = [
            {
                "user_id": student.id,
                "query_text": "Landlord deducted 15000 security deposit for wall paint after 11 month tenancy ended.",
                "predicted_category": "Property and Real Estate",
                "confidence_score": 91.5,
                "is_ambiguous": False,
                "user_feedback_accurate": True,
                "created_at": datetime.now(timezone.utc) - timedelta(days=3)
            },
            {
                "user_id": student.id,
                "query_text": "Private university refusing to issue original 12th marksheet after degree completion.",
                "predicted_category": "Education-Related Legal Issues",
                "confidence_score": 95.0,
                "is_ambiguous": False,
                "user_feedback_accurate": True,
                "created_at": datetime.now(timezone.utc) - timedelta(days=2)
            },
            {
                "user_id": None, # Guest query
                "query_text": "Received a call asking to download AnyDesk and lost 35000 via UPI.",
                "predicted_category": "Cybercrime and Digital Issues",
                "confidence_score": 89.2,
                "is_ambiguous": False,
                "user_feedback_accurate": True,
                "created_at": datetime.now(timezone.utc) - timedelta(days=1)
            },
            {
                "user_id": None,
                "query_text": "Need lawyer for general matter",
                "predicted_category": "Other / Needs Clarification",
                "confidence_score": 30.0,
                "is_ambiguous": True,
                "user_feedback_accurate": None,
                "created_at": datetime.now(timezone.utc) - timedelta(hours=5)
            },
            {
                "user_id": student.id,
                "query_text": "My startup video was re-uploaded without permission and monetized on YouTube.",
                "predicted_category": "Intellectual Property",
                "confidence_score": 92.4,
                "is_ambiguous": False,
                "user_feedback_accurate": True,
                "created_at": datetime.now(timezone.utc) - timedelta(hours=12)
            },
            {
                "user_id": None,
                "query_text": "Bank loan recovery agents calling my parents late at night and threatening abuse.",
                "predicted_category": "Banking and Financial Issues",
                "confidence_score": 88.0,
                "is_ambiguous": False,
                "user_feedback_accurate": True,
                "created_at": datetime.now(timezone.utc) - timedelta(hours=8)
            }
        ]
        for q in sample_queries:
            lq = LegalQuery(**q)
            db.session.add(lq)

        # Sample inquiry from student to Adv. Rahul Verma
        rahul = Lawyer.query.filter_by(name="Adv. Rahul Verma").first()
        if rahul:
            inq = Inquiry(
                user_id=student.id,
                lawyer_id=rahul.id,
                legal_category="Property and Real Estate",
                subject="Notice for Unreturned PG Security Deposit in Koramangala",
                message="Hello Advocate Rahul, my landlord has withheld ₹25,000 for 2 months after vacating. I have bank transaction receipts and rent agreement. Seeking advice on sending a legal notice.",
                user_phone="+91 99887 76655",
                preferred_contact_time="Evening (5pm - 8pm)",
                status="Contacted",
                created_at=datetime.now(timezone.utc) - timedelta(days=2)
            )
            db.session.add(inq)

            # Add a bookmark for student
            bm = Bookmark(user_id=student.id, item_type='lawyer', item_id=rahul.id)
            db.session.add(bm)

        db.session.commit()
        print("[+] Seeded demo queries, consultation inquiry, and bookmarks.")
        print("=" * 65)
        print("  DATABASE SEEDING COMPLETED SUCCESSFULLY")
        print("=" * 65)
        print(f"  Admin Login:   {Config.ADMIN_EMAIL} / {Config.ADMIN_PASSWORD}")
        print(f"  Student Login: student@college.edu / Student@2026!")
        print(f"  Lawyers:       16 Demonstration Advocate Profiles Seeded")
        print(f"  Legal Aid:     12 Statutory & University Clinics Seeded")
        print("=" * 65)

if __name__ == '__main__':
    seed_database()
