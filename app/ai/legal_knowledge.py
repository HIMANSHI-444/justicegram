"""Curated knowledge base for the expanded 15 Indian legal categories in JusticeGram.
Provides plain-language legal guidance, subcategory breakdowns, essential document checklists,
suggested next steps, official public helpline references, and attributable Indian law frameworks.
"""

# ==============================================================================
# 1. EXPANDED LEGAL CATEGORIES WITH SUBCATEGORIES
# ==============================================================================

LEGAL_CATEGORIES = {
    "Family Law": {
        "title": "Family Law",
        "icon": "bi-people-fill",
        "description": "Deals with familial relationships, marriage, divorce, alimony, child custody, domestic disputes, inheritance, and adoption under personal and secular laws.",
        "subcategories": [
            "Divorce and separation",
            "Maintenance and alimony",
            "Child custody",
            "Domestic violence",
            "Dowry-related complaints",
            "Marriage registration",
            "Family property disputes",
            "Inheritance and succession",
            "Adoption-related issues"
        ],
        "keywords": [
            "marriage", "divorce", "custody", "alimony", "maintenance", "talaq", "shaadi", 
            "child custody", "visitation", "adoption", "guardianship", "ancestral property", 
            "paternity", "hindu marriage act", "special marriage act", "family dispute", "khandani",
            "restitution of conjugal rights", "judicial separation", "nikahnama", "talaq-e-hasan",
            "stridhan", "child support", "parental alienation", "succession certificate"
        ],
        "guidance": "Family disputes involve sensitive personal rights. Indian Family Courts mandate pre-litigation counseling and mediation to promote amicable settlement before contested proceedings. Relief such as interim maintenance and child visitation can be requested promptly.",
        "important_documents": [
            "Marriage Certificate / Nikahnama / Arya Samaj Registration Certificate",
            "Proof of residence of both parties (Aadhaar / Voter ID / Passport)",
            "Birth certificates of minor children (for custody or school fee maintenance claims)",
            "Financial statements, recent salary slips, ITRs, and bank accounts of both spouses",
            "Any prior settlement agreements, mutual compromise deeds, or police complaints"
        ],
        "suggested_next_steps": [
            "Participate in mediation through the Family Court Counseling Centre or District Legal Services Authority (DLSA).",
            "Preserve financial records and certified copies of marriage documents in a secure location.",
            "Consult a specialized family law advocate or DLSA panel counsel before signing unilateral agreements.",
            "Avoid discussing sensitive matrimonial conflicts or minor children on social media."
        ],
        "official_resources": [
            {"name": "National Legal Services Authority (NALSA) Family Aid", "helpline": "15100", "url": "https://nalsa.gov.in"},
            {"name": "Department of Justice - Family Courts Portal", "url": "https://doj.gov.in/family-court/"}
        ],
        "clarifying_prompts": [
            "Is the dispute regarding mutual divorce, contested separation, maintenance, or child custody?",
            "Are both parties open to family mediation, or is there an urgent need for interim maintenance?"
        ]
    },

    "Property and Real Estate": {
        "title": "Property and Real Estate",
        "icon": "bi-house-door-fill",
        "description": "Covers tenant-landlord disputes, unreturned security deposits, wrongful eviction, builder delays (RERA), title disputes, land encroachment, and property fraud.",
        "subcategories": [
            "Property ownership disputes",
            "Land disputes",
            "Tenant and landlord disputes",
            "Rent issues",
            "Eviction",
            "Property fraud",
            "Boundary disputes",
            "Real estate builder disputes",
            "RERA-related complaints"
        ],
        "keywords": [
            "landlord", "tenant", "rent", "deposit", "eviction", "kiraya", "flat", "pg", 
            "security deposit", "broker", "registry", "encroachment", "lease", "rera", 
            "builder", "possession", "stamp duty", "sale deed", "property tax", "kabza",
            "zameen", "khata", "patta", "mutation", "allotment letter", "occupancy certificate",
            "illegal lockout", "subletting", "conveyance deed", "builder delay"
        ],
        "guidance": "Property and tenancy disputes are governed by state Rent Control Acts, Model Tenancy legislation, and RERA. Documented rent agreements, stamped receipts, and written notices sent via registered post carry primary evidentiary value.",
        "important_documents": [
            "Registered or signed Rent / Lease Agreement or Builder-Buyer Allotment Letter",
            "Bank transaction statements showing rent transfers or security deposit payments",
            "Written notices served via registered post, speed post, or documented email communication",
            "Photographs / video inventory of property condition at move-in and move-out",
            "Encumbrance Certificate (EC), Khata / Patta extract, and approved building plan"
        ],
        "suggested_next_steps": [
            "Send a formal written legal notice to the landlord/builder via registered speed post giving 15-30 days to resolve.",
            "If a builder has failed to deliver possession on time, lodge an online complaint on your State RERA portal.",
            "For unlawful lockouts or utility disconnection, approach the local Rent Controller / Civil Court for immediate injunction.",
            "Avoid physical confrontations or taking law into your own hands; document every interaction."
        ],
        "official_resources": [
            {"name": "Real Estate Regulatory Authority (RERA) Portal", "url": "https://mohua.gov.in"},
            {"name": "District Rent Authority / DLSA Clinic", "helpline": "15100"}
        ],
        "clarifying_prompts": [
            "Do you hold a registered or signed tenancy agreement or builder allotment letter?",
            "Is the grievance regarding an unreturned deposit, wrongful eviction notice, or delayed flat possession?"
        ]
    },

    "Criminal Law": {
        "title": "Criminal Law",
        "icon": "bi-shield-slash-fill",
        "description": "Deals with criminal offenses under Bharatiya Nyaya Sanhita (BNS) and special criminal statutes, including theft, assault, cheating, criminal intimidation, FIRs, and bail.",
        "subcategories": [
            "Theft",
            "Assault",
            "Threats",
            "Fraud",
            "Cheating",
            "Harassment",
            "Criminal complaints",
            "FIR-related queries",
            "Bail-related general queries",
            "General criminal procedure questions"
        ],
        "keywords": [
            "fir", "police", "arrest", "theft", "assault", "bail", "cheating", "fraud", 
            "chori", "police station", "thaney", "marpeet", "threat", "420", "complaint", 
            "bailable", "non-bailable", "warrant", "crpc", "ipc", "bns", "bnss",
            "anticipatory bail", "regular bail", "remand", "zero fir", "cognizable",
            "extortion", "dhamki", "criminal intimidation", "charge sheet"
        ],
        "guidance": "In criminal cases, immediate recording of the complaint and preservation of digital and forensic evidence is crucial. Citizens have the statutory right to register a Zero FIR at any police station irrespective of jurisdiction.",
        "important_documents": [
            "Copy of the First Information Report (FIR) or Non-Cognizable Report (NCR)",
            "Medico-Legal Case (MLC) examination report in cases of physical injury or assault",
            "CCTV footage, audio/video recordings, phone call logs, and eyewitness contact details",
            "Written complaints addressed to the Station House Officer (SHO) or Superintendent of Police (SP)",
            "Proof of identity and residential address"
        ],
        "suggested_next_steps": [
            "If facing apprehension of arrest in a false complaint, immediately seek legal counsel regarding Anticipatory Bail under BNSS.",
            "Obtain a certified free copy of the registered FIR from the police station as guaranteed by law.",
            "If police refuse to register an FIR for a cognizable offense, send the complaint in writing to the Superintendent of Police under Section 175 BNSS.",
            "Access free defense counsel through DLSA if unable to afford a private criminal defense advocate."
        ],
        "official_resources": [
            {"name": "Emergency Police Response Support System (ERSS)", "helpline": "112"},
            {"name": "Free Legal Aid for Under-trials & Accused (NALSA)", "helpline": "15100", "url": "https://nalsa.gov.in"}
        ],
        "clarifying_prompts": [
            "Has an FIR or formal police complaint already been lodged by either party?",
            "Are you seeking to initiate a criminal complaint, or do you require defense representation / bail?"
        ]
    },

    "Consumer Rights": {
        "title": "Consumer Rights",
        "icon": "bi-cart-check-fill",
        "description": "Protects buyers against defective products, deficiency in services, misleading advertisements, ecommerce fraud, unfair trade practices, and warranty refusals.",
        "subcategories": [
            "Defective products",
            "Refund disputes",
            "Online shopping fraud",
            "Service deficiencies",
            "Misleading advertisements",
            "Warranty disputes",
            "Banking and payment-related consumer complaints"
        ],
        "keywords": [
            "consumer", "defective", "warranty", "guarantee", "refund", "flipkart", "amazon", 
            "ecommerce", "service deficiency", "fake product", "damaged", "return policy", 
            "overcharging", "bill", "invoice", "consumer forum", "graahak", "dhoka",
            "consumer protection act", "edaakhil", "national consumer helpline", "expired goods",
            "airline refund", "telecom deficiency", "false claims"
        ],
        "guidance": "Under the Consumer Protection Act 2019, consumers can file grievances online through the e-Daakhil portal without mandatory lawyer representation. Preserving the tax invoice, warranty card, and rejection emails is essential.",
        "important_documents": [
            "Original retail tax invoice / purchase receipt / order confirmation email",
            "Warranty card, guarantee terms, and product packaging photographs",
            "Unboxing video, damage photographs, or inspection report from authorized service center",
            "Customer service chat logs, support ticket numbers, and formal rejection emails",
            "Bank transaction statement proving debited payment"
        ],
        "suggested_next_steps": [
            "Call the National Consumer Helpline at 1915 or lodge an online complaint at consumerhelpline.gov.in.",
            "Serve a formal written legal notice giving the merchant/manufacturer 15 days to refund or replace.",
            "File an online consumer complaint via the e-Daakhil portal before the District Consumer Commission.",
            "Keep all damaged items and original packaging safe as physical evidence."
        ],
        "official_resources": [
            {"name": "National Consumer Helpline (NCH)", "helpline": "1915", "url": "https://consumerhelpline.gov.in"},
            {"name": "e-Daakhil Consumer Commission Portal", "url": "https://edaakhil.nic.in"}
        ],
        "clarifying_prompts": [
            "Do you possess the original purchase invoice and written communication with the seller?",
            "Is the issue a physical defective item, non-delivery of an online order, or deficient paid service?"
        ]
    },

    "Employment and Labour Law": {
        "title": "Employment and Labour Law",
        "icon": "bi-briefcase-fill",
        "description": "Addresses unpaid salaries, illegal termination, withheld relieving letters, workplace harassment, wage discrimination, gratuity, and provident fund non-deposit.",
        "subcategories": [
            "Unpaid salaries",
            "Wrongful termination",
            "Workplace harassment",
            "Discrimination at work",
            "Employment contracts",
            "Gratuity",
            "Provident fund issues",
            "Leave and workplace rights",
            "Labour-related disputes"
        ],
        "keywords": [
            "salary", "employer", "boss", "job", "company", "unpaid", "termination", "fired", 
            "offer letter", "experience letter", "relieving", "severance", "pf", "provident fund", 
            "gratuity", "harassment at work", "naukri", "vetan", "layoff", "notice period",
            "full and final settlement", "epfo", "labour court", "contract breach", "unlawful deduction",
            "resignation acceptance", "maternity benefit", "overtime"
        ],
        "guidance": "Employment contracts must comply with statutory labour laws. Employers cannot unlawfully withhold earned wages, legitimate PF deposits, or statutory relieving letters upon an employee serving their contractual notice period.",
        "important_documents": [
            "Offer letter, appointment letter, and signed employment agreement",
            "Monthly salary slips for the past 6-12 months and bank statements showing credit entries",
            "Resignation letter, proof of delivery, and HR acknowledgment emails",
            "Full and Final (FnF) settlement calculation sheet or written demand emails",
            "EPFO UAN passbook statement showing provident fund contribution records"
        ],
        "suggested_next_steps": [
            "Send a formal demand email to the HR Head and Management detailing the outstanding amounts and contract terms.",
            "File an online grievance on the EPFiGMS portal if PF contributions were deducted but not deposited.",
            "Lodge a complaint before the regional Labour Commissioner / Conciliation Officer.",
            "Consult a labour advocate before signing unilateral release or non-disparagement waivers."
        ],
        "official_resources": [
            {"name": "Ministry of Labour & Employment SAMADHAN Portal", "url": "https://samadhan.labour.gov.in"},
            {"name": "EPFO Grievance Management System (EPFiGMS)", "url": "https://epfigms.gov.in"}
        ],
        "clarifying_prompts": [
            "Do you have your appointment letter, recent salary slips, and resignation/termination emails?",
            "Is the primary dispute regarding withheld salary, relieving documents, or unremitted PF contributions?"
        ]
    },

    "Cybercrime and Digital Issues": {
        "title": "Cybercrime and Digital Issues",
        "icon": "bi-laptop-fill",
        "description": "Covers online financial fraud, unauthorized UPI transfers, identity theft, cyberstalking, social media account hacking, deepfakes, and digital extortion.",
        "subcategories": [
            "Online scams",
            "UPI fraud",
            "Banking cyber fraud",
            "Social media harassment",
            "Cyberbullying",
            "Identity theft",
            "Hacking complaints",
            "Blackmail using digital platforms",
            "Online privacy concerns"
        ],
        "keywords": [
            "cyber", "scam", "upi", "otp", "phishing", "fraud", "hacked", "account frozen", 
            "instagram hacked", "whatsapp scam", "online fraud", "deepfake", "morphing", 
            "loan app", "extortion", "cyber bullying", "sim swap", "paisa cut gaya",
            "fake profile", "blackmail", "apks", "telegram task scam", "qr code scam",
            "crypto fraud", "1930 helpline", "cybercrime portal"
        ],
        "guidance": "In cyber financial fraud, time is critical. Calling the National Cybercrime Helpline 1930 within the 'Golden Hour' (first 2-3 hours) allows law enforcement to trace and freeze fraudulent transactions before withdrawal.",
        "important_documents": [
            "Bank transaction statement displaying the UTR (Unique Transaction Reference) number",
            "Screenshots of suspect chat messages, payment receipts, fake web links, and phone numbers",
            "URLs of fake social media profiles, impersonating pages, or fraudulent mobile apps",
            "Call recording logs or SMS headers received from the fraudsters",
            "Formal acknowledgment receipt generated from cybercrime.gov.in"
        ],
        "suggested_next_steps": [
            "Immediately dial 1930 to report financial fraud and initiate an account freeze in transit.",
            "Contact your bank's 24x7 helpline to block compromised debit cards, net banking, and UPI IDs.",
            "Register a formal cyber incident report at cybercrime.gov.in and download the acknowledgment PDF.",
            "Do not delete chat histories, SMS alerts, or call logs; they are critical digital evidence under Bharatiya Sakshya Adhiniyam."
        ],
        "official_resources": [
            {"name": "National Cyber Crime Helpline (MHA)", "helpline": "1930", "url": "https://cybercrime.gov.in"},
            {"name": "Indian Computer Emergency Response Team (CERT-In)", "url": "https://cert-in.org.in"}
        ],
        "clarifying_prompts": [
            "Did the incident occur within the last 24 hours involving unauthorized money debit via UPI or net banking?",
            "Is the issue financial fraud, social media account hijacking, or non-consensual image sharing / blackmail?"
        ]
    },

    "Education-Related Legal Issues": {
        "title": "Education-Related Legal Issues",
        "icon": "bi-mortarboard-fill",
        "description": "Focuses on college retention of original certificates, arbitrary fee forfeiture, university exam grievances, scholarship delays, and anti-ragging complaints.",
        "subcategories": [
            "School and college admission disputes",
            "Fee disputes",
            "University complaints",
            "Examination issues",
            "Scholarship problems",
            "Discrimination in educational institutions",
            "Student harassment"
        ],
        "keywords": [
            "college", "university", "school", "degree", "marksheet", "original certificates", 
            "fees refund", "ragging", "ugc", "aicte", "scholarship", "detained", "exam", 
            "hall ticket", "admission cancelled", "attendance", "hostel", "placement fake",
            "provisional degree", "migration certificate", "fee forfeiture", "ugc e-samadhan",
            "anti ragging helpline", "affiliating university"
        ],
        "guidance": "University Grants Commission (UGC) public notifications strictly prohibit colleges and universities from retaining original academic certificates as collateral or denying proportional fee refunds on timely admission cancellation.",
        "important_documents": [
            "Fee payment receipts, admission confirmation letter, and prospectus copy",
            "Formal written applications sent to the Dean / Principal requesting release of certificates or refund",
            "Copy of UGC / AICTE Fee Refund and Certificate Retention Guidelines",
            "Postal receipts or email delivery confirmations of representations submitted to the institution",
            "Student identity card and enrollment registration number"
        ],
        "suggested_next_steps": [
            "Submit a formal written letter to the Head of Institution citing UGC Public Notice No. F. 1-3/2007 (CPP-II).",
            "Lodge an online student grievance on the UGC e-Samadhan portal (samadhan.ugc.ac.in).",
            "For any ragging or harassment incident, immediately dial the 24x7 Anti-Ragging Toll-Free Helpline 1800-180-5522.",
            "Approach the University Student Grievance Redressal Committee (SGRC) or the District Consumer Commission."
        ],
        "official_resources": [
            {"name": "National Anti-Ragging Helpline", "helpline": "1800-180-5522", "url": "https://antiragging.in"},
            {"name": "UGC e-Samadhan Student Grievance Portal", "url": "https://samadhan.ugc.ac.in"}
        ],
        "clarifying_prompts": [
            "Is the educational institution withholding original marks sheets, or refusing a proportional fee refund?",
            "Have you already submitted a formal written representation to the college principal or university registrar?"
        ]
    },

    "Women's Legal Support": {
        "title": "Women's Legal Support",
        "icon": "bi-gender-female",
        "description": "Specialized legal protections for women facing domestic violence, workplace sexual harassment (PoSH), dowry cruelty, cyber harassment, and matrimonial desertion.",
        "subcategories": [
            "Domestic violence",
            "Workplace sexual harassment",
            "Dowry harassment",
            "Stalking",
            "Women's property rights",
            "Marriage-related legal issues",
            "Protection and support resources"
        ],
        "keywords": [
            "domestic violence", "dowry", "dahej", "posh", "stalking", "harassment", 
            "section 498a", "women helpline", "protection officer", "maintenance for wife", 
            "molestation", "stridhan", "cruelty", "mahila thana", "ncw", "bns 85",
            "shared household", "restraining order", "sakhi centre", "sexual harassment at workplace",
            "internal complaints committee", "icc"
        ],
        "guidance": "Under the Protection of Women from Domestic Violence Act (PWDVA), aggrieved women have a statutory right to reside in the shared household regardless of ownership. District Protection Officers provide free legal and shelter coordination.",
        "important_documents": [
            "Detailed written chronological statement of abuse incidents, dates, and locations",
            "Medical examination records, MLCs, or treatment prescriptions of any physical injuries",
            "Photographs, WhatsApp chats, call recordings, emails, or eyewitness statements",
            "List of Stridhan items and jewelry with purchase bills or marriage gift inventories",
            "Copies of any prior complaints filed at the Mahila Police Station or Women's Commission"
        ],
        "suggested_next_steps": [
            "In case of immediate physical danger, dial 112 or the National Women Helpline at 1091.",
            "Contact your local District Protection Officer to register a Domestic Incident Report (DIR).",
            "Lodge an online complaint with the National Commission for Women (NCW) at ncw.nic.in.",
            "Access free shelter, legal representation, and psychological counseling through DLSA One Stop Centres (Sakhi)."
        ],
        "official_resources": [
            {"name": "National Women Helpline (Sakhi / WCD)", "helpline": "1091"},
            {"name": "National Commission for Women 24x7 Helpline", "helpline": "7827170170", "url": "https://ncw.nic.in"},
            {"name": "National Emergency Police Helpline", "helpline": "112"}
        ],
        "clarifying_prompts": [
            "Are you in safe surroundings right now, or do you need emergency helpline intervention?",
            "Is the issue domestic abuse, workplace harassment (PoSH), or online stalking/harassment?"
        ]
    },

    "Civil Disputes": {
        "title": "Civil Disputes",
        "icon": "bi-file-earmark-ruled-fill",
        "description": "Covers monetary recovery, breach of contract, promissory notes, dishonoured cheques, defamation, neighbour disputes, and civil damages.",
        "subcategories": [
            "Contract disputes",
            "Recovery of money",
            "Neighbour disputes",
            "Defamation",
            "Legal notices",
            "Civil compensation",
            "General civil litigation"
        ],
        "keywords": [
            "money recovery", "contract", "breach", "promissory note", "cheque bounce", 
            "section 138", "defamation", "damages", "civil suit", "agreement", "debt", 
            "udhaar", "loan return", "partition", "injunction", "stay order", "specific performance",
            "summary suit", "order 37", "negotiable instruments act", "legal notice reply"
        ],
        "guidance": "Civil claims require written proof of consideration, signed agreements, and strict adherence to limitation periods (typically 3 years for debt recovery). For cheque bounces, a statutory notice must be served within 30 days of the bank memo.",
        "important_documents": [
            "Signed contracts, agreements, promissory notes, or Memorandums of Understanding (MoU)",
            "Bank dishonour memos and copies of returned cheques (in Section 138 matters)",
            "Bank statements, payment receipts, or ledger accounts verifying the monetary transaction",
            "Copies of legal notices issued, postal receipts, and registered delivery tracking slips",
            "Written correspondence, emails, or WhatsApp admissions of liability"
        ],
        "suggested_next_steps": [
            "Send a registered legal notice via speed post through an advocate demanding repayment within 15 days.",
            "Examine whether the monetary claim falls within the 3-year statutory limitation period.",
            "Explore pre-institution mediation at the District Court Mediation Centre before formal filing.",
            "Consider filing a Summary Suit under Order XXXVII of CPC for expedited recovery of documented debts."
        ],
        "official_resources": [
            {"name": "e-Courts Services Portal", "url": "https://services.ecourts.gov.in"},
            {"name": "District Legal Services Authority (DLSA)", "helpline": "15100"}
        ],
        "clarifying_prompts": [
            "Do you hold a signed written agreement, loan receipt, or dishonoured bank cheque?",
            "When did the default or breach take place, and what is the exact financial claim involved?"
        ]
    },

    "Banking and Financial Issues": {
        "title": "Banking and Financial Issues",
        "icon": "bi-cash-coin",
        "description": "Deals with loan disputes, debt recovery agent harassment, credit card overcharges, unauthorized banking deductions, insurance claim rejections, and financial fraud.",
        "subcategories": [
            "Loan disputes",
            "Recovery harassment",
            "Credit card disputes",
            "Unauthorized banking transactions",
            "Insurance claims",
            "Financial fraud"
        ],
        "keywords": [
            "bank", "loan", "emi", "recovery agent", "harassment", "cibil", "credit card", 
            "unauthorized debit", "insurance claim", "rejected", "rbi", "banking ombudsman", 
            "interest rate", "foreclosure", "guarantor", "drt", "sarfaesi", "settlement",
            "hidden charges", "health insurance claim", "claim repudiation"
        ],
        "guidance": "RBI guidelines strictly prohibit recovery agents from using abusive language, threatening borrowers, or contacting relatives. Banks must reverse unauthorized electronic transactions if reported promptly under RBI customer liability rules.",
        "important_documents": [
            "Loan agreement, sanction letter, and repayment schedule",
            "Bank account statements showing disputed charges, EMIs, or unauthorized debits",
            "Record of threatening calls, text messages, or visits by recovery agents",
            "Insurance policy schedule, claim submission documents, and formal repudiation letter",
            "Copies of written complaints submitted to the Bank Branch Manager / Nodal Officer"
        ],
        "suggested_next_steps": [
            "Lodge a written complaint with the Principal Nodal Officer of the bank or insurance company.",
            "If the bank fails to resolve the issue within 30 days, file an online complaint with the RBI Banking Ombudsman (cms.rbi.org.in).",
            "For recovery agent threats or harassment, lodge a police complaint under BNS for criminal intimidation.",
            "For wrongful insurance rejection, approach the Insurance Ombudsman (cioins.co.in)."
        ],
        "official_resources": [
            {"name": "RBI Integrated Ombudsman Scheme Portal", "url": "https://cms.rbi.org.in"},
            {"name": "Council for Insurance Ombudsmen", "url": "https://www.cioins.co.in"}
        ],
        "clarifying_prompts": [
            "Is the issue unauthorized debits by the bank, recovery agent harassment, or an insurance claim rejection?",
            "Have you already submitted a formal written grievance to the bank's Grievance Redressal Officer?"
        ]
    },

    "Government and Public Services": {
        "title": "Government and Public Services",
        "icon": "bi-building-check",
        "description": "Encompasses complaints against municipal authorities, pension delays, public service deficiencies, Right to Information (RTI) applications, and administrative grievances.",
        "subcategories": [
            "Government service complaints",
            "Pension issues",
            "Public authority complaints",
            "RTI-related general information",
            "Administrative grievances",
            "Public service delivery disputes"
        ],
        "keywords": [
            "government", "rti", "pension", "municipality", "corporation", "cpgrams", 
            "public grievance", "delay", "bribe", "officer", "ration card", "aadhaar", 
            "voter id", "administrative", "central government", "state government", 
            "public authority", "first appeal", "public service guarantee"
        ],
        "guidance": "Under the Right to Information Act 2005, every citizen can seek information from public authorities within a statutory 30-day timeline. The Central and State CPGRAMS portals allow direct escalation of administrative delays.",
        "important_documents": [
            "Copy of original application, registration number, or RTI request submitted",
            "Postal receipts, online acknowledgment receipt, or speed post tracking slips",
            "Pension Payment Order (PPO) copy, service records, and retirement documentation",
            "Previous correspondence, rejection notices, or inspection endorsements from public offices",
            "Identity proof of the applicant (Aadhaar / Voter ID)"
        ],
        "suggested_next_steps": [
            "File a formal RTI application online via rtionline.gov.in seeking status and official file notings.",
            "Lodge an administrative grievance on the Government of India CPGRAMS portal (pgportal.gov.in).",
            "If an RTI request receives no reply within 30 days, file a First Appeal before the First Appellate Authority.",
            "For state municipal service delays, utilize your State Public Service Guarantee / Samadhan portal."
        ],
        "official_resources": [
            {"name": "CPGRAMS Central Public Grievance Portal", "url": "https://pgportal.gov.in"},
            {"name": "RTI Online National Portal", "url": "https://rtionline.gov.in"}
        ],
        "clarifying_prompts": [
            "Is your grievance related to pension release, delayed municipal documentation, or an RTI request?",
            "Which department or public authority is responsible for the matter (Central, State, or Municipal)?"
        ]
    },

    "Intellectual Property": {
        "title": "Intellectual Property",
        "icon": "bi-lightbulb-fill",
        "description": "Protects creative and commercial assets, including copyright infringement, unauthorized digital content copying, trademark disputes, brand counterfeiting, and design theft.",
        "subcategories": [
            "Copyright issues",
            "Trademark disputes",
            "Unauthorized content usage",
            "Intellectual property infringement"
        ],
        "keywords": [
            "copyright", "trademark", "patent", "ipr", "infringement", "piracy", 
            "stolen content", "logo copy", "brand name", "counterfeit", "intellectual property", 
            "dmca", "takedown", "cease and desist", "plagiarism", "design infringement"
        ],
        "guidance": "Copyright automatically subsists upon the creation of original work, though registration provides prima facie proof in court. Registered trademarks protect brand names against unauthorized use and consumer confusion.",
        "important_documents": [
            "Proof of creation date (original source code, raw photography files, design project files)",
            "Trademark Registration Certificate or pending TM Application number",
            "URL links, screenshots, or physical samples proving the unauthorized infringing usage",
            "Prior commercial use evidence (invoices, client contracts, marketing material)",
            "Cease-and-desist notices previously served to the infringing party"
        ],
        "suggested_next_steps": [
            "Document and timestamp all instances of infringement with screenshots and archiving tools.",
            "Serve a Cease and Desist legal notice demanding immediate withdrawal of infringing materials.",
            "File a DMCA / digital copyright takedown notice with hosting platforms, YouTube, or Google.",
            "Consult an IPR attorney regarding filing an infringement suit seeking interim injunction and damages."
        ],
        "official_resources": [
            {"name": "Controller General of Patents, Designs & Trademarks", "url": "https://ipindia.gov.in"},
            {"name": "Copyright Office of India", "url": "https://copyright.gov.in"}
        ],
        "clarifying_prompts": [
            "Is the issue unauthorized copying of creative digital content (copyright) or unauthorized use of a brand name/logo (trademark)?",
            "Have you formally registered the copyright or trademark with the Indian Intellectual Property Office?"
        ]
    },

    "Medical and Healthcare Issues": {
        "title": "Medical and Healthcare Issues",
        "icon": "bi-hospital-fill",
        "description": "Covers medical negligence concerns, inflated hospital billing, arbitrary cashless insurance refusal, patient rights violations, and clinical healthcare grievances.",
        "subcategories": [
            "Medical negligence concerns",
            "Hospital billing disputes",
            "Insurance rejection",
            "Patient rights",
            "Healthcare service complaints"
        ],
        "keywords": [
            "medical negligence", "hospital", "doctor", "surgery error", "overcharging", 
            "wrong diagnosis", "patient rights", "medical council", "nmc", "death in hospital", 
            "cashless insurance denied", "discharge summary", "pharmacy error", "tpa dispute"
        ],
        "guidance": "Doctors and hospitals owe a duty of reasonable care. Negligence requires proving deviation from accepted medical standards. Patients have a legal right to receive complete certified medical records and itemized billing under the Charter of Patient Rights.",
        "important_documents": [
            "Complete indoor hospital case records, nursing charts, and detailed discharge summary",
            "Diagnostic test results, MRI/CT scans, pathology reports, and prescription slips",
            "Itemized hospital bills, pharmacy receipts, and payment transaction proofs",
            "Expert medical second opinions detailing standard protocol deviation",
            "Insurance TPA pre-authorization letters and formal rejection notices"
        ],
        "suggested_next_steps": [
            "Submit a written application to the hospital superintendent requesting certified copies of complete indoor case records.",
            "Obtain an independent expert medical opinion from a qualified specialist regarding standard of care.",
            "Lodge a disciplinary complaint before the State Medical Council / National Medical Commission (NMC).",
            "File a consumer complaint before the Consumer Commission for service deficiency and compensation."
        ],
        "official_resources": [
            {"name": "National Medical Commission (NMC) Grievance Desk", "url": "https://www.nmc.org.in"},
            {"name": "National Consumer Helpline (Medical Billing / Insurance)", "helpline": "1915"}
        ],
        "clarifying_prompts": [
            "Do you have certified copies of the discharge summary, operation notes, and itemized billing?",
            "Is the primary grievance diagnostic/surgical negligence, or unfair hospital overcharging / insurance denial?"
        ]
    },

    "Immigration and Documentation": {
        "title": "Immigration and Documentation",
        "icon": "bi-pass-fill",
        "description": "Addresses passport delays, police verification adverse reports, visa document disputes, citizenship documentation, and birth/death certificate corrections.",
        "subcategories": [
            "Passport-related issues",
            "Documentation disputes",
            "General visa-related questions",
            "Citizenship and documentation queries"
        ],
        "keywords": [
            "passport", "visa", "police verification", "adverse report", "rpo", "embassy", 
            "citizenship", "oci", "pao", "birth certificate", "name correction", "deportation", 
            "travel ban", "look out circular", "loc", "tatkaal passport", "immigration"
        ],
        "guidance": "Holding a passport is recognized as a facet of personal liberty under Article 21 of the Constitution. Adverse police verification reports must specify the exact pending criminal proceedings or legal grounds for impounding.",
        "important_documents": [
            "Passport Application Form receipt, File Number, and appointment slip",
            "Show-cause notice received from the Regional Passport Office (RPO)",
            "Certified court orders in case of pending minor criminal complaints or NOC for travel",
            "Original birth certificate, educational marksheets, and identity proofs",
            "Correspondence exchanged with the RPO or Ministry of External Affairs"
        ],
        "suggested_next_steps": [
            "Book an online grievance inquiry appointment at your Regional Passport Office (RPO).",
            "If an adverse police report was filed due to a pending criminal case, apply for a Court NOC under Section 6(2)(f) of the Passports Act.",
            "Lodge an online grievance on the MADAD consular portal or mPassport Seva grievance cell.",
            "If a passport is arbitrarily impounded without opportunity to be heard, consult counsel regarding a Writ Petition before the High Court."
        ],
        "official_resources": [
            {"name": "Passport Seva Kendra Grievance Portal", "helpline": "1800-258-1800", "url": "https://www.passportindia.gov.in"},
            {"name": "MADAD Consular Services Portal", "url": "https://madad.gov.in"}
        ],
        "clarifying_prompts": [
            "Have you received a formal show-cause letter from the Regional Passport Office?",
            "Is the delay due to an adverse police verification report, court case intimation, or name/date correction?"
        ]
    },

    "Other / Needs Clarification": {
        "title": "Other / Needs Clarification",
        "icon": "bi-question-circle-fill",
        "description": "Triggered when query description is brief, ambiguous, multi-faceted, or outside standard automated categorizations.",
        "subcategories": [
            "General legal inquiry",
            "Multi-faceted issue requiring clarification",
            "Unspecified dispute"
        ],
        "keywords": [],
        "guidance": "Your problem description requires additional specific details to accurately determine the legal forum and applicable statutes. Sharing details such as dates, parties involved, contracts, or specific remedies helps categorize your issue effectively.",
        "important_documents": [
            "Any letters, agreements, notices, or communications received",
            "Proof of identity of the parties involved",
            "Financial statements, receipts, or transaction records"
        ],
        "suggested_next_steps": [
            "Provide additional details describing who is involved and what outcome you are seeking.",
            "Use the manual category selection below to explore the legal domain that best fits your situation.",
            "Visit a university legal aid clinic or local DLSA front desk for free in-person guidance."
        ],
        "official_resources": [
            {"name": "National Legal Services Authority (NALSA)", "helpline": "15100", "url": "https://nalsa.gov.in"},
            {"name": "e-Courts Public Services Portal", "url": "https://services.ecourts.gov.in"}
        ],
        "clarifying_prompts": [
            "Who is the other party involved (e.g., landlord, employer, seller, family member, police, bank)?",
            "What specific remedy are you seeking (e.g., refund, certificate release, safety protection, bail, dispute resolution)?"
        ]
    }
}


# ==============================================================================
# 2. MODULAR INDIAN LAW REFERENCES DATABASE
# ==============================================================================
# Curated, attributable legal frameworks mapped to categories and issues.
# Follows strict accuracy: official sources, plain-language summaries, verifiable links.

INDIAN_LAW_FRAMEWORKS = [
    {
        "law_name": "Bharatiya Nyaya Sanhita, 2023 (BNS)",
        "category": "Criminal Law",
        "related_issue": "Substantive criminal offenses, theft, cheating, assault, fraud, threats",
        "description": "The primary criminal code of India replacing the Indian Penal Code (IPC). Defines criminal offenses including theft, physical assault, criminal breach of trust, cheating, criminal intimidation, and offenses against the human body and property.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/20062",
        "source_name": "India Code, Ministry of Law and Justice, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Bharatiya Nagarik Suraksha Sanhita, 2023 (BNSS)",
        "category": "Criminal Law",
        "related_issue": "Criminal procedure, FIR, Zero FIR, arrest, bail, investigation, trial",
        "description": "Governs the procedure for criminal investigation, registration of FIRs (including Zero FIR and electronic FIR), arrests, remand, anticipatory bail, regular bail, and court trials, replacing the Code of Criminal Procedure (CrPC).",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/20063",
        "source_name": "India Code, Ministry of Law and Justice, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Bharatiya Sakshya Adhiniyam, 2023 (BSA)",
        "category": "Criminal Law",
        "related_issue": "Evidence rules, digital and electronic records admissibility",
        "description": "Consolidates rules of evidence in Indian courts, replacing the Indian Evidence Act 1872. Contains specific provisions recognizing electronic and digital records, emails, server logs, and digital messages as primary documentary evidence.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/20064",
        "source_name": "India Code, Ministry of Law and Justice, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Constitution of India (Articles 14, 19, 21, 21A, 32, 226)",
        "category": "Government and Public Services",
        "related_issue": "Fundamental rights, equality before law, personal liberty, right to education, writ remedies",
        "description": "The supreme legal document of India guaranteeing fundamental rights: Article 14 (Equality), Article 19 (Freedoms), Article 21 (Right to Life & Personal Liberty), and Article 21A (Right to Education). Enables citizens to seek writ remedies before High Courts and Supreme Court against arbitrary state actions.",
        "jurisdiction": "Constitutional Law of India",
        "official_reference_link": "https://legislative.gov.in/constitution-of-india/",
        "source_name": "Legislative Department, Ministry of Law and Justice, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Source"
    },
    {
        "law_name": "Consumer Protection Act, 2019",
        "category": "Consumer Rights",
        "related_issue": "Defective goods, service deficiency, unfair trade practices, misleading ads, ecommerce refund disputes",
        "description": "Establishes a three-tier Consumer Dispute Redressal Commission (District, State, National) and the Central Consumer Protection Authority (CCPA). Protects consumer rights against defective products, unfair contracts, online shopping fraud, and deficient services without mandatory advocate representation.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/15256",
        "source_name": "Department of Consumer Affairs, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Information Technology Act, 2000 (as amended)",
        "category": "Cybercrime and Digital Issues",
        "related_issue": "Cyber fraud, unauthorized access, identity theft, cyberstalking, hacking, online extortion",
        "description": "The principal legislation governing electronic commerce and cyber offenses in India. Details penalties for unauthorized hacking (Section 66), identity theft (Section 66C), cheating by personation (Section 66D), non-consensual image sharing (Section 66E), and intermediary liability.",
        "jurisdiction": "Central Legislation (Applies throughout India and extra-territorially)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1999",
        "source_name": "Ministry of Electronics & Information Technology (MeitY)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Protection of Women from Domestic Violence Act, 2005 (PWDVA)",
        "category": "Women's Legal Support",
        "related_issue": "Domestic abuse, shared household residence, protection orders, maintenance",
        "description": "Civil protection law providing immediate relief to women facing physical, emotional, verbal, sexual, or economic domestic violence. Guarantees rights to stay in the shared household, protection orders, monetary maintenance, and assistance from Protection Officers and One Stop Crisis Centres.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2019",
        "source_name": "Ministry of Women and Child Development, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Dowry Prohibition Act, 1961",
        "category": "Women's Legal Support",
        "related_issue": "Dowry demands, giving or taking of dowry, matrimonial cruelty",
        "description": "Prohibits the demanding, giving, or taking of dowry in connection with marriage. Outlaws dowry harassment and mandates that gifts given at the time of marriage (Stridhan) belong exclusively to the woman.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1529",
        "source_name": "India Code, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Hindu Marriage Act, 1955",
        "category": "Family Law",
        "related_issue": "Divorce, judicial separation, restitution of conjugal rights, child custody, alimony",
        "description": "Governs marriage, mutual consent divorce (Section 13B), contested divorce grounds, permanent alimony, maintenance pendente lite, and child custody for Hindus, Buddhists, Jains, and Sikhs.",
        "jurisdiction": "Personal Law (Applies to Hindus throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1560",
        "source_name": "Legislative Department, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Special Marriage Act, 1954",
        "category": "Family Law",
        "related_issue": "Civil marriage registration, inter-faith marriage, mutual consent divorce",
        "description": "Secular law providing civil marriage registration for any two Indian citizens regardless of religion or faith. Provides detailed statutory procedures for solemnization, mutual consent divorce, and property inheritance under secular law.",
        "jurisdiction": "Secular Law (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1545",
        "source_name": "Legislative Department, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Hindu Succession Act, 1956 (amended 2005)",
        "category": "Family Law",
        "related_issue": "Ancestral property inheritance, coparcenary rights for daughters, succession",
        "description": "Governs intestate succession and ancestral property division among Hindus. The landmark 2005 amendment established equal coparcenary rights by birth for daughters on par with sons in ancestral property.",
        "jurisdiction": "Personal Law (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1564",
        "source_name": "Legislative Department, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Transfer of Property Act, 1882",
        "category": "Property and Real Estate",
        "related_issue": "Lease agreements, tenancy rights, sale deeds, mortgages, property transfers",
        "description": "Regulates the transfer of immovable property by act of parties in India. Governs legal rights and liabilities of lessors and lessees, determination of leases, notice requirements, mortgages, gifts, and sale deeds.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2338",
        "source_name": "India Code, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Real Estate (Regulation and Development) Act, 2016 (RERA)",
        "category": "Property and Real Estate",
        "related_issue": "Delayed possession by builders, homebuyer rights, escrow accounts, builder disputes",
        "description": "Established dedicated state Real Estate Regulatory Authorities (RERA) to protect homebuyers against delayed flat possession, misleading builder promises, unauthorized plan alterations, and structural defects. Mandates deposit of 70% project funds in escrow.",
        "jurisdiction": "Central Legislation (Enforced via State RERA Authorities)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2158",
        "source_name": "Ministry of Housing and Urban Affairs (MoHUA)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Right to Information Act, 2005 (RTI)",
        "category": "Government and Public Services",
        "related_issue": "Transparency, administrative accountability, official documents, public grievance records",
        "description": "Empowers Indian citizens to request official information, inspection of work, and certified copies of documents from public authorities within a mandated 30-day timeframe, with internal First Appeal and State/Central Information Commission remedies.",
        "jurisdiction": "Central Legislation (Applies to all public authorities in India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2065",
        "source_name": "Department of Personnel and Training (DoPT), Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Sexual Harassment of Women at Workplace Act, 2013 (PoSH Act)",
        "category": "Women's Legal Support",
        "related_issue": "Workplace sexual harassment, Internal Complaints Committee (ICC), employer liability",
        "description": "Mandates that every workplace with 10 or more employees constitute an Internal Complaints Committee (ICC) to investigate complaints of sexual harassment. Provides time-bound inquiry procedures, confidentiality safeguards, and conciliation mechanisms.",
        "jurisdiction": "Central Legislation (Applies to all Indian workplaces)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2104",
        "source_name": "Ministry of Women and Child Development",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Code on Wages, 2019 & Payment of Wages Act, 1936",
        "category": "Employment and Labour Law",
        "related_issue": "Unpaid salaries, unlawful salary deductions, minimum wages, full and final settlement",
        "description": "Prohibits employers from making arbitrary deductions from earned wages and guarantees timely payment of salaries. Prescribes remedies before the Labour Authority for recovery of withheld or delayed wages.",
        "jurisdiction": "Central Legislation (Enforced via Central and State Labour Departments)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/11993",
        "source_name": "Ministry of Labour and Employment, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Negotiable Instruments Act, 1881 (Section 138)",
        "category": "Civil Disputes",
        "related_issue": "Cheque bounce, dishonour of cheques for insufficient funds, statutory demand notices",
        "description": "Section 138 creates criminal and civil liability for the dishonour of cheques drawn for the discharge of any debt or liability. Requires issuing a statutory demand notice within 30 days of receiving the bank dishonour memo.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2187",
        "source_name": "India Code, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Indian Contract Act, 1872",
        "category": "Civil Disputes",
        "related_issue": "Breach of contract, recovery of debt, agreements, damages, promissory notes",
        "description": "Governs the formation, performance, and enforceability of contracts in India. Outlines legal remedies for breach of contract, assessment of liquidated damages, promissory obligations, and commercial agreements.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2187",
        "source_name": "India Code, Ministry of Law and Justice",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Motor Vehicles Act, 1988 (as amended 2019)",
        "category": "Civil Disputes",
        "related_issue": "Road accident compensation, third-party insurance claims, Motor Accident Claims Tribunal (MACT)",
        "description": "Regulates road transport, mandatory third-party motor insurance, and adjudicates compensation claims for vehicular accident injuries or fatalities before the Motor Accident Claims Tribunal (MACT).",
        "jurisdiction": "Central Legislation (Enforced by State Transport Departments)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1798",
        "source_name": "Ministry of Road Transport and Highways (MoRTH)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Copyright Act, 1957",
        "category": "Intellectual Property",
        "related_issue": "Copyright infringement, digital piracy, unauthorized content duplication, software code",
        "description": "Protects original literary, dramatic, musical, artistic works, cinematograph films, and computer programs. Provides civil remedies (injunctions, damages) and criminal penalties for copyright infringement and unauthorized digital copying.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1367",
        "source_name": "Department for Promotion of Industry and Internal Trade (DPIIT)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Trade Marks Act, 1999",
        "category": "Intellectual Property",
        "related_issue": "Brand name protection, trademark infringement, counterfeit products, passing off",
        "description": "Provides for the registration and better protection of trademarks for goods and services, preventing fraudulent use of marks and trademark infringement through civil suits and statutory injunctions.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1993",
        "source_name": "Controller General of Patents, Designs and Trade Marks (CGPDTM)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Protection of Children from Sexual Offences Act, 2012 (POCSO)",
        "category": "Criminal Law",
        "related_issue": "Offenses against children, child safety, mandatory reporting",
        "description": "Comprehensive statute to protect children below 18 years from sexual assault, harassment, and pornography. Establishes child-friendly procedures, Special POCSO Courts, and mandatory reporting obligations for citizens and institutions.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/2079",
        "source_name": "Ministry of Women and Child Development",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Legal Services Authorities Act, 1987",
        "category": "Other / Needs Clarification",
        "related_issue": "Free legal aid entitlement (Section 12), Lok Adalats, DLSA representation",
        "description": "Statutory framework providing free and competent legal services to eligible citizens (women, children, SC/ST, custody inmates, disabled, and low-income persons) through NALSA, State Legal Services Authorities, and District Legal Services Authorities (DLSA).",
        "jurisdiction": "Central Legislation (Enforced across all Indian States & UTs)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1937",
        "source_name": "National Legal Services Authority (NALSA)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Reserve Bank of India Integrated Ombudsman Scheme, 2021",
        "category": "Banking and Financial Issues",
        "related_issue": "Banking customer grievances, recovery agent harassment, unauthorized debits, credit card disputes",
        "description": "Provides a single-window cost-free dispute resolution mechanism for bank customers against deficiency in services by banks, NBFCs, and payment system participants, including violations of Fair Practices Code by loan recovery agents.",
        "jurisdiction": "Regulatory Framework (Applies to all RBI-regulated entities in India)",
        "official_reference_link": "https://cms.rbi.org.in",
        "source_name": "Reserve Bank of India (RBI)",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Regulatory Scheme"
    },
    {
        "law_name": "Passports Act, 1967",
        "category": "Immigration and Documentation",
        "related_issue": "Passport issuance, refusal grounds, impounding, police verification adverse reports",
        "description": "Regulates the issuance of passports and travel documents to Indian citizens. Specifies statutory grounds under Section 6 for refusal or impounding, and procedures for obtaining Court No-Objection Certificates (NOC) when minor matters are pending.",
        "jurisdiction": "Central Legislation (Applies throughout India)",
        "official_reference_link": "https://www.indiacode.nic.in/handle/123456789/1647",
        "source_name": "Ministry of External Affairs (MEA), Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    },
    {
        "law_name": "Clinical Establishments (Registration and Regulation) Act, 2010 & Charter of Patients' Rights",
        "category": "Medical and Healthcare Issues",
        "related_issue": "Medical records access, emergency medical care, patient rights, hospital transparency",
        "description": "Provides registration standards for healthcare facilities and recognizes the National Human Rights Commission (NHRC) / MoHFW Charter of Patients' Rights, guaranteeing patient access to complete case records, itemized billing, and informed consent.",
        "jurisdiction": "Central Legislation (Enacted by participating Indian States)",
        "official_reference_link": "https://clinicalestablishments.gov.in",
        "source_name": "Ministry of Health and Family Welfare, Government of India",
        "last_verified_date": "November 2026",
        "verification_status": "Verified Official Statute"
    }
]


def get_relevant_indian_laws(category: str, subcategory: str = None, query_text: str = "") -> list[dict]:
    """Retrieves relevant Indian legal frameworks for a detected category and optional subcategory.
    Matches primarily by broad category and filters or ranks by keyword relevance.
    """
    category_matches = [
        law for law in INDIAN_LAW_FRAMEWORKS 
        if law["category"] == category
    ]

    if not category_matches:
        # Fallback to general fundamental rights / legal services act
        return [
            law for law in INDIAN_LAW_FRAMEWORKS 
            if law["law_name"].startswith("Legal Services Authorities Act") or 
               law["law_name"].startswith("Constitution of India")
        ]

    # If subcategory or query_text provided, prioritize laws matching related_issue
    if subcategory or query_text:
        search_terms = (f"{subcategory or ''} {query_text}").lower()
        sorted_matches = sorted(
            category_matches,
            key=lambda l: any(term in l["related_issue"].lower() for term in search_terms.split() if len(term) > 3),
            reverse=True
        )
        return sorted_matches[:3]

    return category_matches[:3]


SUBCATEGORY_RULES = {
    "Family Law": [
        ("Divorce and separation", ["divorce", "separation", "talaq", "separate", "split"]),
        ("Maintenance and alimony", ["maintenance", "alimony", "child support", "expense", "kharcha"]),
        ("Child custody", ["custody", "visitation", "child", "minor", "bachha", "daughter", "son"]),
        ("Domestic violence", ["domestic violence", "beating", "assault by husband", "torture", "marpeet"]),
        ("Dowry-related complaints", ["dowry", "dahej", "gold demand", "cash demand"]),
        ("Marriage registration", ["marriage registration", "certificate", "nikahnama", "special marriage"]),
        ("Family property disputes", ["ancestral property", "family property", "partition", "khandani"]),
        ("Inheritance and succession", ["inheritance", "succession", "will", "wasiyat", "heir"]),
        ("Adoption-related issues", ["adoption", "adopt", "orphan", "foster", "cara"])
    ],
    "Property and Real Estate": [
        ("Real estate builder disputes", ["builder", "possession delay", "project delayed", "allotment"]),
        ("RERA-related complaints", ["rera", "builder complaint", "promoter", "occupancy certificate"]),
        ("Tenant and landlord disputes", ["landlord", "tenant", "deposit", "makan malik", "kirayedaar", "pg"]),
        ("Rent issues", ["rent", "kiraya", "rent increase", "arrears", "withhold rent"]),
        ("Eviction", ["eviction", "vacate", "khali karna", "lockout", "throw luggage"]),
        ("Property fraud", ["forged deed", "fake registry", "fraud sale", "sold twice"]),
        ("Boundary disputes", ["boundary", "encroach", "wall", "kabza", "neighbor land"]),
        ("Property ownership disputes", ["title deed", "ownership", "registry", "mutation", "khata", "patta"]),
        ("Land disputes", ["land", "agricultural land", "khet", "plot dispute", "survey"])
    ],
    "Criminal Law": [
        ("Theft", ["theft", "stolen", "chori", "snatching", "robbery", "break-in"]),
        ("Assault", ["assault", "attack", "hit", "injury", "marpeet", "physical violence"]),
        ("Threats", ["threat", "dhamki", "intimidation", "death threat", "extortion"]),
        ("Fraud", ["fraud", "scam", "forgery", "fake document", "impersonation"]),
        ("Cheating", ["cheating", "420", "cheated", "deceived", "dhoka"]),
        ("Harassment", ["harassment", "stalking", "blackmail", "nuisance"]),
        ("Criminal complaints", ["criminal complaint", "sho", "magistrate complaint"]),
        ("FIR-related queries", ["fir", "zero fir", "ncr", "police station", "thaney", "refuse fir"]),
        ("Bail-related general queries", ["bail", "anticipatory bail", "regular bail", "arrest", "custody"]),
        ("General criminal procedure questions", ["crpc", "bnss", "remand", "warrant", "chargesheet"])
    ],
    "Consumer Rights": [
        ("Defective products", ["defective", "damaged", "broken", "faulty", "manufacturing defect", "cracked"]),
        ("Refund disputes", ["refund", "money back", "return rejected", "cancellation refund"]),
        ("Online shopping fraud", ["flipkart", "amazon", "ecommerce", "online order", "fake product", "wrong item"]),
        ("Service deficiencies", ["service deficiency", "poor service", "not working", "airline cancel", "telecom"]),
        ("Misleading advertisements", ["misleading", "false claim", "exaggerated", "advertisement"]),
        ("Warranty disputes", ["warranty", "guarantee", "service center", "repair refusal"]),
        ("Banking and payment-related consumer complaints", ["payment gateway", "excess charge", "billing error"])
    ],
    "Employment and Labour Law": [
        ("Unpaid salaries", ["unpaid salary", "salary not paid", "salary pending", "withheld salary", "vetan"]),
        ("Wrongful termination", ["fired", "terminated", "wrongful termination", "fired without notice", "layoff"]),
        ("Workplace harassment", ["workplace harassment", "boss harassment", "toxic", "threaten fired"]),
        ("Discrimination at work", ["discrimination", "bias", "maternity denied", "equal pay"]),
        ("Employment contracts", ["offer letter", "contract breach", "bond", "notice period"]),
        ("Gratuity", ["gratuity", "gratuity not paid"]),
        ("Provident fund issues", ["pf", "provident fund", "epfo", "uan", "pf deduction"]),
        ("Leave and workplace rights", ["leave", "medical leave", "sick leave", "working hours"]),
        ("Labour-related disputes", ["labour court", "labour commissioner", "union", "overtime"])
    ],
    "Cybercrime and Digital Issues": [
        ("UPI fraud", ["upi", "google pay", "phonepe", "paytm", "qr code", "unauthorized upi"]),
        ("Banking cyber fraud", ["otp", "netbanking", "phishing", "sim swap", "bank fraud"]),
        ("Online scams", ["scam", "telegram task", "lottery scam", "job scam", "crypto scam", "investment fraud"]),
        ("Social media harassment", ["instagram", "facebook", "whatsapp", "fake profile", "trolling"]),
        ("Cyberbullying", ["bullying", "online abuse", "group harassment"]),
        ("Identity theft", ["identity theft", "impersonation", "fake account in my name"]),
        ("Hacking complaints", ["hacked", "account compromised", "gmail hacked", "unauthorized access"]),
        ("Blackmail using digital platforms", ["blackmail", "deepfake", "morphing", "loan app", "extortion"]),
        ("Online privacy concerns", ["privacy", "data leak", "data breach", "personal photos leaked"])
    ],
    "Education-Related Legal Issues": [
        ("School and college admission disputes", ["admission cancelled", "quota", "seat dispute", "entrance"]),
        ("Fee disputes", ["fees refund", "excess fees", "capitation", "fee penalty", "annual fees"]),
        ("University complaints", ["original certificates", "marksheet", "degree withheld", "ugc", "aicte"]),
        ("Examination issues", ["hall ticket", "exam detained", "attendance", "paper leak", "revaluation"]),
        ("Scholarship problems", ["scholarship", "sanctioned amount", "stipend not credited"]),
        ("Discrimination in educational institutions", ["discrimination", "caste bias", "unfair treatment"]),
        ("Student harassment", ["ragging", "anti ragging", "warden", "hostel expulsion", "seniors"])
    ],
    "Women's Legal Support": [
        ("Domestic violence", ["domestic violence", "beating", "abused", "shared household", "cruelty"]),
        ("Workplace sexual harassment", ["posh", "sexual harassment", "icc", "colleague misbehavior", "boss advances"]),
        ("Dowry harassment", ["dowry", "dahej", "in-laws harassment", "498a", "bns 85"]),
        ("Stalking", ["stalking", "following", "monitoring", "threat to leak photos"]),
        ("Women's property rights", ["stridhan", "jewelry return", "women property share", "maintenance for wife"]),
        ("Marriage-related legal issues", ["abandoned", "deserted", "second wife", "maintenance"]),
        ("Protection and support resources", ["protection officer", "sakhi centre", "women helpline 1091", "mahila thana"])
    ],
    "Civil Disputes": [
        ("Contract disputes", ["breach of contract", "agreement broken", "mou violation", "vendor agreement"]),
        ("Recovery of money", ["money recovery", "lent money", "borrowed", "debt", "udhaar", "unpaid loan"]),
        ("Neighbour disputes", ["neighbour", "encroachment", "wall", "noise", "water leakage", "nuisance"]),
        ("Defamation", ["defamation", "manhani", "false rumor", "reputation damaged", "social media post"]),
        ("Legal notices", ["legal notice", "reply to notice", "statutory notice"]),
        ("Civil compensation", ["damages", "compensation", "property damage", "accident claim"]),
        ("General civil litigation", ["civil suit", "injunction", "stay order", "specific performance", "order 37"])
    ],
    "Banking and Financial Issues": [
        ("Loan disputes", ["loan", "foreclosure", "interest rate hike", "settlement", "personal loan"]),
        ("Recovery harassment", ["recovery agent", "threatening call", "calling relatives", "abusive agent"]),
        ("Credit card disputes", ["credit card", "hidden charge", "annual fee dispute", "disputed transaction"]),
        ("Unauthorized banking transactions", ["unauthorized debit", "money deducted", "without otp", "reversal"]),
        ("Insurance claims", ["insurance claim", "health insurance rejected", "claim repudiated", "tpa"]),
        ("Financial fraud", ["cibil score", "fraudulent loan in my name", "chit fund", "ponzi"])
    ],
    "Government and Public Services": [
        ("RTI-related general information", ["rti", "right to information", "first appeal", "public information officer"]),
        ("Pension issues", ["pension", "pension delayed", "ppo", "gratuity delayed", "retirement"]),
        ("Government service complaints", ["cpgrams", "pgportal", "delay in service", "corruption", "bribe"]),
        ("Public authority complaints", ["municipality", "corporation", "tehsildar", "collector", "discom"]),
        ("Administrative grievances", ["ration card", "aadhaar correction", "voter id", "caste certificate"]),
        ("Public service delivery disputes", ["public service guarantee", "sewa", "arbitrary rejection"])
    ],
    "Intellectual Property": [
        ("Copyright issues", ["copyright", "song copied", "book copied", "code copied", "piracy"]),
        ("Trademark disputes", ["trademark", "brand name", "logo copied", "brand infringement", "counterfeit"]),
        ("Unauthorized content usage", ["stolen content", "my photo used", "video reuploaded", "dmca takedown"]),
        ("Intellectual property infringement", ["patent", "design infringement", "cease and desist", "ipr lawsuit"])
    ],
    "Medical and Healthcare Issues": [
        ("Medical negligence concerns", ["medical negligence", "wrong surgery", "wrong diagnosis", "doctor mistake"]),
        ("Hospital billing disputes", ["overcharging", "inflated bill", "unnecessary test", "icu charges"]),
        ("Insurance rejection", ["cashless denied", "tpa rejected claim", "pre-existing clause"]),
        ("Patient rights", ["medical records denied", "discharge summary withheld", "detained patient"]),
        ("Healthcare service complaints", ["pharmacy expired medicine", "lab error", "nurse negligence"])
    ],
    "Immigration and Documentation": [
        ("Passport-related issues", ["passport", "passport delay", "police verification adverse", "rpo show cause"]),
        ("Documentation disputes", ["birth certificate correction", "name mismatch", "affidavit", "apostille"]),
        ("General visa-related questions", ["visa rejected", "embassy dispute", "travel authorization"]),
        ("Citizenship and documentation queries", ["citizenship", "oci card", "travel ban", "look out circular"])
    ]
}


def detect_subcategory(category: str, query_text: str) -> str:
    """Detects the specific subcategory within the predicted category based on user query keywords."""
    cat_rules = SUBCATEGORY_RULES.get(category)
    if not cat_rules:
        cat_info = LEGAL_CATEGORIES.get(category)
        if cat_info and cat_info.get("subcategories"):
            return cat_info["subcategories"][0]
        return "General"

    q_lower = query_text.lower()
    for subcat_name, keywords in cat_rules:
        if any(kw in q_lower for kw in keywords):
            return subcat_name

    # Default to first subcategory if no specific keyword matched
    return cat_rules[0][0]
