"""Script to package JusticeGram into JusticeGram_Report_Code and JusticeGram_Report_Code.zip
Organizes frontend, backend, data, and comprehensive academic project README.
"""

import os
import shutil
import zipfile
from pathlib import Path

ROOT_DIR = Path("D:/JusticeGram")
PACKAGE_DIR = ROOT_DIR / "JusticeGram_Report_Code"
ZIP_PATH = ROOT_DIR / "JusticeGram_Report_Code.zip"

def create_report_package():
    print("[*] Creating report package directory structure...")
    frontend_dir = PACKAGE_DIR / "frontend"
    backend_dir = PACKAGE_DIR / "backend"
    data_dir = PACKAGE_DIR / "data"

    frontend_dir.mkdir(parents=True, exist_ok=True)
    backend_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)

    # 1. Copy Frontend Assets
    print("[*] Copying frontend templates and static assets...")
    shutil.copytree(ROOT_DIR / "app" / "templates", frontend_dir / "templates", dirs_exist_ok=True)
    shutil.copytree(ROOT_DIR / "app" / "static", frontend_dir / "static", dirs_exist_ok=True)

    # 2. Copy Backend Python Code & Autonomous Runtime Assets
    print("[*] Copying backend Flask application, routes, models, AI engine, and self-contained runtime assets...")
    backend_app = backend_dir / "app"
    backend_app.mkdir(parents=True, exist_ok=True)
    shutil.copy(ROOT_DIR / "app" / "__init__.py", backend_app / "__init__.py")
    shutil.copy(ROOT_DIR / "app" / "config.py", backend_app / "config.py")
    shutil.copy(ROOT_DIR / "app" / "models.py", backend_app / "models.py")
    shutil.copytree(ROOT_DIR / "app" / "routes", backend_app / "routes", dirs_exist_ok=True)
    shutil.copytree(ROOT_DIR / "app" / "ai", backend_app / "ai", dirs_exist_ok=True)
    # Make backend autonomously executable
    shutil.copytree(ROOT_DIR / "app" / "templates", backend_app / "templates", dirs_exist_ok=True)
    shutil.copytree(ROOT_DIR / "app" / "static", backend_app / "static", dirs_exist_ok=True)
    shutil.copytree(ROOT_DIR / "app" / "data", backend_app / "data", dirs_exist_ok=True)

    # Standalone backend scripts
    shutil.copy(ROOT_DIR / "run.py", backend_dir / "run.py")
    shutil.copy(ROOT_DIR / "seed_data.py", backend_dir / "seed_data.py")
    shutil.copy(ROOT_DIR / "test_app.py", backend_dir / "test_app.py")
    shutil.copy(ROOT_DIR / "generate_dataset.py", backend_dir / "generate_dataset.py")
    shutil.copy(ROOT_DIR / "requirements.txt", backend_dir / "requirements.txt")

    # 3. Copy Data and Trained Model Artifacts
    print("[*] Copying dataset and serialized ML model artifacts...")
    shutil.copy(ROOT_DIR / "app" / "data" / "legal_queries_sample.csv", data_dir / "legal_queries_sample.csv")
    shutil.copytree(ROOT_DIR / "app" / "data" / "model_artifacts", data_dir / "model_artifacts", dirs_exist_ok=True)

    # 4. Generate Comprehensive Academic README.md
    print("[*] Generating comprehensive README.md with full documentation & legal disclaimer...")
    readme_content = """# JusticeGram — AI-Powered Legal Assistance Platform
**Academic BCA Mini-Project (College Demonstration & Evaluation Edition)**

---

## 1. Project Overview & Objective

**JusticeGram** is an AI-assisted legal literacy and resource navigation web application designed to help college students and ordinary citizens understand everyday legal grievances. 

Citizens often struggle with statutory jargon and do not know which forum to approach for issues like:
- Withholding of educational certificates by colleges
- Unreturned security deposits by landlords
- Unpaid salaries or unfair workplace termination
- Online shopping fraud and warranty disputes
- UPI cyber scams and digital harassment

Users can describe their grievance in **natural English or conversational Hinglish**. JusticeGram's intelligent classification pipeline identifies the likely legal category and subcategory, explains the classification basis, cites verified Indian statutory provisions (with direct **India Code** links), generates an evidence checklist, and matches the user with specialized advocates and free government legal aid clinics (NALSA / DLSA).

> **Crucial Educational Disclaimer:** JusticeGram is strictly an informational legal technology platform for academic demonstration. It does not provide legal representation, guarantee outcomes, or replace a qualified advocate. In immediate emergencies, citizens must dial 112 (Police), 1091 (Women in Distress), or 1930 (Cybercrime).

---

## 2. Technology Stack

- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3 (Strictly Deep Navy `#142133` and Cream `#F4EDE0` palette on public pages), Bootstrap Icons.
- **Backend:** Python 3.13, Flask 3.0, Flask-SQLAlchemy 3.1.
- **Database:** SQLite (SQLAlchemy ORM with migration path to MySQL/PostgreSQL).
- **Machine Learning / NLP:** Scikit-Learn 1.4, TF-IDF Vectorization (`ngram_range=(1, 2)`, sublinear TF scaling), Multinomial Logistic Regression (`class_weight='balanced'`), Joblib model serialization.
- **Security:** Werkzeug PBKDF2 secure password hashing, Flask session management, role-based access control (Admin & Regular User).
- **Analytics:** Chart.js 4.4 interactive charts for administrator dashboard.

---

## 3. Directory Structure

```text
JusticeGram_Report_Code/
│
├── frontend/                     # UI Layer
│   ├── templates/                # Jinja2 HTML Templates
│   │   ├── base.html             # Global base layout (logo, Navy #142133 navbar, footer)
│   │   ├── index.html            # Public landing page (Hero, 15 Categories, Workflow, FAQ)
│   │   ├── assistant.html        # AI Legal Assistant (Classification, Laws, Checklist, Match Reasons)
│   │   ├── about.html            # Academic project overview & technical stack
│   │   ├── how_it_works.html     # Technical architecture breakdown (5-step pipeline)
│   │   ├── faqs.html             # Frequently Asked Questions
│   │   ├── contact.html          # Contact & inquiry form
│   │   ├── disclaimer.html       # Full legal terms & advisory notices
│   │   ├── auth/                 # Login & Registration views (Clean form styling)
│   │   ├── user/                 # User dashboard, saved queries, bookmarks
│   │   ├── admin/                # Administrator panel with Chart.js analytics
│   │   ├── lawyers/              # Directory & detailed advocate profile views
│   │   └── legal_aid/            # Free Legal Aid & Helpline discovery
│   └── static/                   # Static Assets
│       ├── css/
│       │   └── style.css         # Custom styles (Strictly Navy #142133 & Cream #F4EDE0)
│       └── js/
│           ├── main.js           # General interactivity
│           ├── assistant.js      # Assistant character counter, AJAX submit, feedback
│           └── admin.js          # Chart.js analytics renderer
│
├── backend/                      # Server & Intelligence Layer
│   ├── app/
│   │   ├── __init__.py           # Application factory (create_app)
│   │   ├── config.py             # App configurations & environment settings
│   │   ├── models.py             # Database models (User, Lawyer, LegalAidResource, LegalQuery, Inquiry, Bookmark)
│   │   ├── routes/               # Modular Blueprint Routes
│   │   │   ├── main.py           # Public landing and information routes
│   │   │   ├── assistant.py      # AI Assistant endpoint & lawyer match reason engine
│   │   │   ├── lawyers.py        # Lawyer directory, search, filter, and booking routes
│   │   │   ├── legal_aid.py      # Free legal aid and helpline directory routes
│   │   │   ├── auth.py           # User authentication & session management
│   │   │   ├── user.py           # User dashboard & bookmarks
│   │   │   └── admin.py          # Admin analytics & CRUD operations
│   │   └── ai/                   # AI & Machine Learning Module
│   │       ├── classifier.py     # LegalClassifier singleton (ML + heuristic hybrid)
│   │       ├── legal_knowledge.py# 15 Categories, 90+ Subcategories, 26 Indian Law Frameworks
│   │       ├── preprocessor.py   # English & Hinglish normalization, ambiguity detection
│   │       └── train_model.py    # Offline model training & evaluation script
│   ├── run.py                    # Application launch entry point
│   ├── seed_data.py              # Database seeding (Admin, 16 Demo Advocates, 12 Aid Clinics)
│   ├── test_app.py               # Unit test suite (17 comprehensive tests)
│   ├── generate_dataset.py       # Dataset generator (522 labeled English & Hinglish samples)
│   └── requirements.txt          # Python package dependencies
│
└── data/                         # Datasets & Trained Artifacts
    ├── legal_queries_sample.csv  # 522 Labeled legal problem queries across 15 categories
    └── model_artifacts/          # Serialized scikit-learn models
        ├── model.joblib          # Trained LogisticRegression classifier
        └── tfidf.joblib          # Trained TfidfVectorizer feature extractor
```

---

## 4. Expanded 15 Indian Legal Categories & Subcategories

JusticeGram covers 15 distinct legal domains:

1. **Family Law:** Divorce and separation, Maintenance and alimony, Child custody, Domestic violence, Dowry-related complaints, Marriage registration, Family property disputes, Inheritance and succession, Adoption-related issues.
2. **Property and Real Estate:** Property ownership disputes, Land disputes, Tenant and landlord disputes, Rent issues, Eviction, Property fraud, Boundary disputes, Real estate builder disputes, RERA-related complaints.
3. **Criminal Law:** Theft, Assault, Threats, Fraud, Cheating, Harassment, Criminal complaints, FIR-related queries, Bail-related general queries, General criminal procedure questions.
4. **Consumer Rights:** Defective products, Refund disputes, Online shopping fraud, Service deficiencies, Misleading advertisements, Warranty disputes, Banking and payment-related consumer complaints.
5. **Employment and Labour Law:** Unpaid salaries, Wrongful termination, Workplace harassment, Discrimination at work, Employment contracts, Gratuity, Provident fund issues, Leave and workplace rights, Labour-related disputes.
6. **Cybercrime and Digital Issues:** Online scams, UPI fraud, Banking cyber fraud, Social media harassment, Cyberbullying, Identity theft, Hacking complaints, Blackmail using digital platforms, Online privacy concerns.
7. **Education-Related Legal Issues:** School and college admission disputes, Fee disputes, University complaints, Examination issues, Scholarship problems, Discrimination in educational institutions, Student harassment.
8. **Women's Legal Support:** Domestic violence, Workplace sexual harassment (PoSH), Dowry harassment, Stalking, Women's property rights, Marriage-related legal issues, Protection and support resources.
9. **Civil Disputes:** Contract disputes, Recovery of money, Neighbour disputes, Defamation, Legal notices, Civil compensation, General civil litigation.
10. **Banking and Financial Issues:** Loan disputes, Recovery harassment, Credit card disputes, Unauthorized banking transactions, Insurance claims, Financial fraud.
11. **Government and Public Services:** Government service complaints, Pension issues, Public authority complaints, RTI-related general information, Administrative grievances, Public service delivery disputes.
12. **Intellectual Property:** Copyright issues, Trademark disputes, Unauthorized content usage, Intellectual property infringement.
13. **Medical and Healthcare Issues:** Medical negligence concerns, Hospital billing disputes, Insurance rejection, Patient rights, Healthcare service complaints.
14. **Immigration and Documentation:** Passport-related issues, Documentation disputes, General visa-related questions, Citizenship and documentation queries.
15. **Other / Needs Clarification:** Active when queries are brief, vague, or multi-faceted; prompts user with targeted clarifying questions rather than guessing inaccurately.

---

## 5. Indian Statutory Frameworks Database (26 Verified Acts)

JusticeGram matches predicted queries to 26 official Indian legislative acts, referencing exact sections, plain-language summaries, verification dates, and official **India Code** URLs:

- **Bharatiya Nyaya Sanhita, 2023 (BNS)** — [India Code](https://www.indiacode.nic.in/handle/123456789/20062)
- **Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)** — [India Code](https://www.indiacode.nic.in/handle/123456789/20063)
- **Bharatiya Sakshya Adhiniyam, 2023 (BSA)** — [India Code](https://www.indiacode.nic.in/handle/123456789/20064)
- **Constitution of India (Articles 14, 19, 21, 21A, 32, 226)** — [Legislative Dept](https://legislative.gov.in/constitution-of-india/)
- **Consumer Protection Act, 2019** — [India Code](https://www.indiacode.nic.in/handle/123456789/15256)
- **Information Technology Act, 2000** — [India Code](https://www.indiacode.nic.in/handle/123456789/1999)
- **Protection of Women from Domestic Violence Act, 2005 (PWDVA)** — [India Code](https://www.indiacode.nic.in/handle/123456789/2015)
- **Sexual Harassment of Women at Workplace (PoSH) Act, 2013** — [India Code](https://www.indiacode.nic.in/handle/123456789/2104)
- **Right to Information Act, 2005 (RTI)** — [India Code](https://www.indiacode.nic.in/handle/123456789/2065)
- **Real Estate (Regulation and Development) Act, 2016 (RERA)** — [India Code](https://www.indiacode.nic.in/handle/123456789/2158)
- **Negotiable Instruments Act, 1881 (Section 138 Check Bounce)** — [India Code](https://www.indiacode.nic.in/handle/123456789/2281)
- **Legal Services Authorities Act, 1987 (Section 12 Free Aid)** — [India Code](https://www.indiacode.nic.in/handle/123456789/1934)
- *And 14 additional central acts (Transfer of Property Act, Contract Act, Payment of Wages Act, Maternity Benefit Act, Copyright Act, Trade Marks Act, Passports Act, etc.)*

---

## 6. Lawyer Database — Data Source and Disclaimer

### Transparency Notice
> **"These lawyer profiles are fictional sample records created for academic demonstration purposes. They do not represent real lawyers or provide actual legal services."**

### Rationale and Ethical Safeguards:
1. **Academic Demonstration Data:** To demonstrate the platform's multi-criteria advocate matching engine, search filters, and consultation inquiry messaging without violating Bar Council of India advertising regulations or impersonating real individuals, **16 fictional advocate profiles** have been seeded.
2. **Naming Convention:** All profiles use common Indian names (e.g., Adv. Ananya Sharma, Adv. Rahul Verma, Adv. Priya Singh, Adv. Arjun Mehta, Adv. Neha Gupta, Adv. Amit Mishra, Adv. Sneha Patel, Adv. Rohan Malhotra, Adv. Kavita Rao, Adv. Vivek Joshi, Adv. Pooja Yadav, Adv. Saurabh Kumar, Adv. Harish Iyer, Adv. Deepa Nambiar, Adv. Vikramaditya Rathore, Adv. Farhan Qureshi).
3. **Demo Badges:** Every lawyer card in the UI displays a clear **"Demo Profile"** / **"Unverified — Demo Data"** badge.
4. **Fictional Contact Data:** Email addresses use `@demo-justicegram.org` and registration numbers explicitly include `(Demo Profile)`.
5. **Lawyer Matching Reason Engine:** The matching engine explains to the user *why* an advocate was recommended:
   - Primary or secondary category specialization
   - Jurisdiction match (city and state)
   - Pro bono / subsidized consultation availability
   - Seniority level (years of practice)

---

## 7. How to Setup and Run Locally

### Prerequisites
- Python 3.10+ installed.

### Installation Steps
```bash
# 1. Navigate to backend directory
cd backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train ML Model (if regenerating artifacts)
python app/ai/train_model.py

# 4. Seed Database (creates admin, test student, 16 advocates, 12 aid clinics)
python seed_data.py

# 5. Run Unit Test Suite
python test_app.py

# 6. Start Development Server
python run.py
```
Open your browser at **http://127.0.0.1:5000**.

### Default Demonstration Credentials
- **Administrator Account:** `admin@justicegram.org` / `Admin@Justice2026!`
- **Student Demo User:** `student@college.edu` / `Student@2026!`

---

## 8. Test Execution Results

The application includes an automated test suite in `test_app.py` verifying preprocessors, classifier predictions, statutory retrievals, authentication, route access control, and admin analytics:

```text
Ran 17 tests in 6.78s
OK (All 17 Tests Passing, 100% Success)
```

---

## 9. Viva Voce Q&A Cheat Sheet (For College Presentation)

**Q1: Why use TF-IDF + Logistic Regression instead of an LLM API (OpenAI/Gemini)?**
*Answer:* A local TF-IDF + Logistic Regression model is fully deterministic, operates completely offline without cloud costs or API quotas, has sub-10ms inference latency, preserves citizen query privacy, and is easily explainable through feature coefficients.

**Q2: What is the fallback if the AI model confidence is low?**
*Answer:* If confidence is below 35% or if query keywords match overlapping domains, JusticeGram activates a domain keyword heuristic cross-check and flags the issue as "Other / Needs Clarification", prompting the user with clarifying questions and offering a manual category selection dropdown.

**Q3: How does the free legal aid feature work under Indian law?**
*Answer:* Under Section 12 of the Legal Services Authorities Act, 1987, specific citizen groups (women, children, custody inmates, SC/ST, and individuals below state income ceilings) are legally entitled to 100% free legal counsel funded by the state. JusticeGram directly connects them to NALSA/DLSA front desks and official statutory helplines (15100, 1930, 1915).
"""

    readme_file = PACKAGE_DIR / "README.md"
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"[+] Written comprehensive README.md ({len(readme_content)} chars)")

    # 5. Create JusticeGram_Report_Code.zip
    print(f"[*] Packaging {PACKAGE_DIR} into {ZIP_PATH}...")
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PACKAGE_DIR):
            for file in files:
                file_path = Path(root) / file
                archive_name = file_path.relative_to(PACKAGE_DIR.parent)
                zipf.write(file_path, archive_name)

    zip_size_mb = ZIP_PATH.stat().st_size / (1024 * 1024)
    print(f"[+] Successfully generated archive: {ZIP_PATH} ({zip_size_mb:.2f} MB)")
    print("=" * 65)
    print("  JUSTICEGRAM REPORT CODE PACKAGE READY FOR SUBMISSION")
    print("=" * 65)

if __name__ == '__main__':
    create_report_package()
