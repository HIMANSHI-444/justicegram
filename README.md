# JusticeGram — AI-Powered Legal Assistance Platform

[![Academic BCA Mini-Project](https://img.shields.io/badge/Project-BCA%20Mini--Project-0d9488.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)
[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-1c2541.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)
[![Flask](https://img.shields.io/badge/Backend-Flask%203.1-0d9488.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)
[![scikit-learn](https://img.shields.io/badge/NLP-scikit--learn%20TF--IDF-f59e0b.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)
[![Bootstrap 5](https://img.shields.io/badge/Frontend-Bootstrap%205.3-7952b3.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)
[![Status: Functional & Tested](https://img.shields.io/badge/Tests-15%20Passed-10b981.svg)](file:///c:/Users/kalya/OneDrive/Desktop/ws)

**JusticeGram** is an AI-powered legal assistance and legal literacy platform developed as a college BCA mini-project. It assists college students, youth, and ordinary citizens in understanding which broad legal category their problem belongs to (in simple English or conversational Hinglish), discovering relevant lawyers, locating free student legal aid clinics and District Legal Services Authorities (DLSA), and initiating consultation inquiries.

---

## 1. Project Objectives

- **Demystify Legal Jargon:** Enable citizens to describe real-world grievances without needing prior knowledge of law sections or court procedures.
- **Support Hinglish & Natural Language:** Accept queries in everyday Indian conversational English and Hinglish (e.g., *"makan malik security deposit wapas nahi kar raha"*, *"college degree certificate withhold kar raha hai"*).
- **Safe & Realistic AI Classification:** Detect broad legal categories across 10 defined domains, provide confidence ratings, and detect ambiguous or vague inputs to ask clarifying questions instead of guessing.
- **Actionable Checklists:** Provide curated lists of essential documents to preserve and immediate procedural steps to undertake.
- **Pro Bono & Free Legal Aid Discovery:** Searchable directory of National Legal Services Authorities (NALSA/DLSA), university legal aid cells, pro bono advocates, and 24x7 public emergency helplines (1930 Cybercrime, 1915 Consumer, 1091 Women in Distress, 15100 NALSA).
- **Ethical Integrity:** Maintain clear, prominent disclaimers that the platform provides legal literacy and resource navigation, not formal legal representation or guaranteed court outcomes.

---

## 2. Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, Modern JavaScript (ES6), Bootstrap 5.3, Bootstrap Icons (v1.11) |
| **Styling & Theme** | Custom Legal Tech Palette (Deep Navy `#0a1128`, Clean White, Subtle Teal `#0d9488`, Amber Gold) |
| **Backend** | Python 3 with Flask (Modular Application Factory Architecture & Blueprints) |
| **Database** | SQLite via Flask-SQLAlchemy ORM (with direct migration path to MySQL/PostgreSQL) |
| **AI / Machine Learning** | scikit-learn (`TfidfVectorizer` + Multinomial `LogisticRegression` with class balancing) |
| **Fallback Heuristics** | Domain keyword matcher with regex word-boundary boundaries and ambiguity detector |
| **Authentication** | Flask Sessions with Werkzeug PBKDF2 secure password hashing & Role-Based Access Control |
| **Data Visualizations** | Chart.js 4.4 for Administrator analytics dashboard |
| **Testing** | Python `unittest` suite (15 automated unit & integration tests) |

---

## 3. Supported Legal Categories

JusticeGram classifies natural language descriptions into 10 structured domains:

1. **Family Law:** Marital separation, mutual divorce, child custody, alimony, maintenance, and inheritance.
2. **Property and Tenancy:** Security deposit recovery, wrongful eviction, PG disputes, builder possession delays (RERA), and land boundary encroachment.
3. **Criminal Law:** FIR refusal, bail applications, physical assault, theft, criminal intimidation, and cheating (Section 420).
4. **Consumer Rights:** Defective e-commerce products, cancelled flight refunds, fake goods, and e-Daakhil filing.
5. **Employment and Labour:** Unpaid salaries, termination without notice, withheld relieving/experience letters, and PF non-deposit.
6. **Cybercrime:** UPI financial fraud, phishing scams, WhatsApp extortion, loan app harassment, and unauthorized debit freezing (Helpline 1930).
7. **Education-Related Issues:** Original certificate retention by colleges, unfair fee forfeiture, scholarship delays, and anti-ragging complaints.
8. **Civil Disputes:** Money recovery suits, bounced cheques (Negotiable Instruments Act Section 138), breach of contract, and defamation.
9. **Women's Legal Support:** Domestic violence protection orders, dowry harassment, workplace sexual harassment (PoSH Act), and Mahila Thana assistance.
10. **Other / Needs Clarification:** Triggered when inputs are overly brief, multi-faceted, or vague, presenting guided clarifying prompts.

---

## 4. Project Directory Structure

```text
ws/
├── app/
│   ├── __init__.py                 # Flask application factory, error handlers, and blueprint loader
│   ├── config.py                   # Environment configuration (Dev, Test, Prod)
│   ├── models.py                   # SQLAlchemy Models: User, Lawyer, LegalAidResource, LegalQuery, Inquiry, Bookmark
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py                 # Landing page, about, how-it-works, FAQs, contact, disclaimer
│   │   ├── auth.py                 # Register, login, logout, password hashing, session RBAC
│   │   ├── assistant.py            # AI Legal Assistant, classification API, provider matching, feedback
│   │   ├── lawyers.py              # Lawyer directory, search, multi-filters, detail, consultation inquiry
│   │   ├── legal_aid.py            # Free Legal Aid directory, university cells, public helplines
│   │   ├── user_dashboard.py       # Protected user dashboard: query history, sent inquiries, bookmarks
│   │   └── admin.py                # Admin dashboard, Chart.js stats API, CRUD for lawyers and legal aid
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── preprocessor.py         # Text cleaning, Hinglish stopword filtering, ambiguity detector
│   │   ├── classifier.py           # Production AI inference engine (TF-IDF + Logistic Regression + heuristics)
│   │   ├── legal_knowledge.py      # Curated knowledge base for 10 legal categories, guidance, doc checklists
│   │   └── train_model.py          # Training and holdout evaluation script
│   ├── data/
│   │   ├── legal_queries_sample.csv # Synthetic labeled legal dataset across 10 categories
│   │   └── model_artifacts/        # Serialized tfidf.joblib and model.joblib artifacts
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css           # Custom styling (deep navy, teal accents, sleek typography, cards, badges)
│   │   └── js/
│   │       ├── main.js             # Bootstrap tooltips, alert auto-dismiss, bookmark toggle
│   │       ├── assistant.js        # Dynamic prompt filling, loading spinner, character counter, AI feedback
│   │       └── admin_charts.js     # Chart.js initialization for category distribution and lawyer types
│   └── templates/
│       ├── base.html               # Master layout with navbar, alerts, disclaimers, and footer
│       ├── index.html              # Landing page (hero, search box, workflow, categories, featured cards, FAQs)
│       ├── assistant.html          # AI Legal Assistant interface, prompt pills, result cards, next steps
│       ├── about.html              # Academic BCA mini-project description & evaluation notes
│       ├── how_it_works.html       # Technical walkthrough of NLP preprocessing & classification
│       ├── faqs.html               # Frequently asked legal questions & helpline guides
│       ├── contact.html            # Contact & partnership inquiry form
│       ├── disclaimer.html         # Comprehensive legal and AI advisory terms
│       ├── auth/                   # Login and registration templates
│       ├── user/                   # User dashboard template
│       ├── admin/                  # Admin dashboard, lawyer CRUD, legal aid CRUD, query audit logs
│       ├── lawyers/                # Lawyer directory and detailed profile templates
│       ├── legal_aid/              # Free Legal Aid and public helpline directory
│       └── errors/                 # Custom 404 and 500 error pages
├── seed_data.py                    # Seeding script for demo accounts, advocates, clinics, and sample logs
├── test_app.py                     # 15 automated unit & integration tests
├── run.py                          # Local server launcher
├── requirements.txt                # Python package dependencies
├── .env.example                    # Environment variable configuration template
└── README.md                       # Comprehensive documentation & BCA viva presentation guide
```

---

## 5. Quick Start & Local Execution

### Prerequisites
- Python 3.10+ (Tested on Python 3.13)
- Windows, macOS, or Linux

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Seed the Database
Populates the SQLite database with initial administrator accounts, test student credentials, realistic advocate profiles, free legal aid authorities, and sample query records:
```bash
python seed_data.py
```

### Step 3: Run the Application
```bash
python run.py
```
Open your web browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## 6. Default Demonstration Accounts

The database comes pre-seeded with two demonstration accounts for evaluation:

| Role | Email Address | Password | Permissions |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin@justicegram.org` | `Admin@Justice2026!` | Access to `/admin`, Chart.js metrics, lawyer CRUD, verification toggle, legal aid CRUD, query audit logs, model retraining |
| **Student / Citizen** | `student@college.edu` | `Student@2026!` | Access to `/dashboard`, query history, sent consultation requests, saved bookmarks, profile updates |

*Note: You can also register a brand new student user at any time via the `/auth/register` interface.*

---

## 7. AI Model: Training, Evaluation & Dataset Customization

### How the Model Works
1. **Preprocessing (`app/ai/preprocessor.py`):** Normalizes text, cleans punctuation, and removes domain stopwords and Hinglish fillers while preserving legal keywords.
2. **Feature Extraction:** `TfidfVectorizer` generates sublinear TF-IDF features with unigram and bigram coverage (`ngram_range=(1, 2)`).
3. **Classification:** Multinomial `LogisticRegression` with `class_weight='balanced'` assigns probabilities across the 10 legal categories.
4. **Safety Guard:** If input is brief or ambiguous (e.g., *"help me please"*), the ambiguity detector routes to `Other / Needs Clarification` and asks targeted clarifying questions.

### Retraining the Model
To retrain the model locally or after editing `app/data/legal_queries_sample.csv`:
```bash
python app/ai/train_model.py
```
Or click the **"Retrain AI Classifier"** button directly on the **Administrator Dashboard** (`/admin`).

### Replacing the Sample Dataset
1. Open `app/data/legal_queries_sample.csv`.
2. Add your own labeled rows with the columns `query,category`.
3. Run `python app/ai/train_model.py`. The script will output the classification report (precision, recall, F1-score) and regenerate `model.joblib` and `tfidf.joblib`.

---

## 8. Automated Test Suite

A comprehensive test suite of 15 automated test cases verifies authentication, role-based access control, NLP preprocessing, classifier accuracy, inquiry submissions, and route responses:

```bash
python test_app.py
```

**Test Coverage Summary:**
- NLP preprocessing & punctuation cleaning: **PASSED**
- Ambiguity detection on brief and vague queries: **PASSED**
- Classification of tenancy disputes: **PASSED**
- Classification of cybercrime transactions: **PASSED**
- User registration and duplicate email protection: **PASSED**
- Password hashing & login/logout session flow: **PASSED**
- Administrator route protection & RBAC checks: **PASSED**
- Directory filters (category, city, pro bono): **PASSED**
- Consultation inquiry submission & database persistence: **PASSED**
- Chart.js aggregated statistics endpoint: **PASSED**

---

## 9. Sample Scenarios for Live Demonstration

When presenting JusticeGram for college viva or evaluation, try submitting these sample prompts:

| Scenario | Sample Prompt Input | Expected AI Category |
| :--- | :--- | :--- |
| **PG Security Deposit** | *"Mera landlord security deposit wapas nahi de raha hai, 45 din ho gaye vacate kiye hue."* | **Property and Tenancy** (85-92%) |
| **College Certificate Retention** | *"College is refusing to return my original 10th and 12th marksheets after graduation and demanding penalty fees."* | **Education-Related Issues** (90-95%) |
| **Unpaid Salary & Termination** | *"Company terminated me overnight without notice and has not paid my salary for 2 months."* | **Employment and Labour** (85-90%) |
| **UPI Cyber Fraud** | *"Money debited from bank account through a fake electricity bill SMS via UPI transfer."* | **Cybercrime** (90-95%) |
| **Defective Product Return** | *"Bought a laptop on ecommerce sale, arrived with broken screen and seller rejected replacement."* | **Consumer Rights** (85-90%) |
| **Ambiguous / Vague Query** | *"Need lawyer for problem"* | **Other / Needs Clarification** (Flags clarifying questions) |

---

## 10. College Viva Q&A Guide

**Q1: Why did you choose TF-IDF + Logistic Regression instead of calling an external commercial API like ChatGPT or Claude?**  
*Answer:* As an academic project, relying solely on an external paid API creates external dependencies, latency, rate limits, and ongoing API token costs. TF-IDF paired with Logistic Regression runs completely offline, deterministically, fast (< 15ms), and provides transparent evaluation metrics (precision, recall, F1-score) suitable for offline deployment and privacy.

**Q2: How does the application handle Hinglish?**  
*Answer:* The preprocessing pipeline standardizes common Hindi transliterations in Roman script (e.g., *thaney, kiraya, naukri, dahej, makan malik, chori*) and includes Hinglish conversational stop words in `app/ai/preprocessor.py` so the model focuses on substantive dispute keywords.

**Q3: How is database security handled?**  
*Answer:* Passwords are never stored in plaintext; they are hashed using Werkzeug's PBKDF2 with SHA-256 and salted. Sensitive administrative routes are protected using a custom `@admin_required` decorator.

**Q4: How can this be scaled to MySQL in production?**  
*Answer:* The application uses Flask-SQLAlchemy with declarative models. To migrate to MySQL, simply install `mysqlclient` or `pymysql` and update `DATABASE_URI` in `.env` to `mysql+pymysql://user:password@localhost/justicegram_db`.

---

## 11. Academic Legal Disclaimer

JusticeGram is developed strictly for educational, academic demonstration, and legal literacy purposes. It is not a law firm, does not provide formal legal counsel, and does not establish an advocate-client relationship. In cases of immediate danger or emergency, citizens must contact the official national police helpline (**112**) or the relevant statutory authority.
