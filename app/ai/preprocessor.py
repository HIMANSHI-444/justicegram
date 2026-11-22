import re
import string

# Common English & Hinglish stop words and fillers that don't add legal signal
LEGAL_STOP_WORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
    'he', 'she', 'it', 'they', 'them', 'what', 'which', 'who', 'whom', 'this',
    'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
    'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
    'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
    'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all',
    'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
    'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'can', 'will', 'just', 'don', 'should', 'now',
    'please', 'plz', 'pls', 'sir', 'madam', 'dear', 'hello', 'hi',
    # Hinglish fillers
    'kya', 'hai', 'hain', 'ka', 'ki', 'ke', 'ko', 'se', 'me', 'mein', 'par',
    'ye', 'yeh', 'woh', 'bhi', 'ho', 'gaya', 'gayi', 'raha', 'rahi', 'kare',
    'batao', 'chahiye', 'karna', 'kuch', 'mera', 'meri', 'mere', 'kripya'
}

GENERIC_VAGUE_WORDS = {
    'help', 'problem', 'issue', 'advice', 'guidance', 'matter', 'case',
    'need', 'want', 'madat', 'urgent', 'legal', 'advocate', 'lawyer', 'query'
}

def clean_text(text: str) -> str:
    """Cleans natural language input by normalizing whitespace,
    lowercasing, and standardizing characters.
    """
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower().strip()
    
    # Replace URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    
    # Replace email addresses
    text = re.sub(r'\S+@\S+', ' ', text)
    
    # Replace special punctuation with space, keep alphanumeric and hyphens
    text = re.sub(r'[^\w\s\-]', ' ', text)
    
    # Normalize multiple whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_for_model(text: str) -> str:
    """Preprocesses user input for the TF-IDF vectorizer.
    Removes common stopwords while retaining critical domain keywords.
    """
    cleaned = clean_text(text)
    words = cleaned.split()
    
    # Filter stopwords if text is sufficiently long, but preserve words if query is short
    if len(words) > 3:
        filtered_words = [w for w in words if w not in LEGAL_STOP_WORDS and len(w) > 1]
        if filtered_words:
            return " ".join(filtered_words)
            
    return cleaned

def is_query_ambiguous(text: str) -> tuple[bool, str]:
    """Analyzes if a query is too vague, too short, or lacks legal substance.
    Returns (is_ambiguous, reason).
    """
    cleaned = clean_text(text)
    raw_words = cleaned.split()
    substantive_words = [w for w in raw_words if w not in LEGAL_STOP_WORDS]
    
    if len(cleaned) < 12 or len(substantive_words) < 2:
        return True, "Query is too brief to understand the legal context. Please describe what happened in a sentence or two."

    # Check if all words are generic/vague words
    all_generic = all(w in GENERIC_VAGUE_WORDS or w in LEGAL_STOP_WORDS for w in raw_words)
    if all_generic:
        return True, "Your query contains only general requests. Please describe the specific party involved (e.g. landlord, employer, seller, family member) and what occurred."

    generic_vague_phrases = [
        "i need help", "help me", "problem", "i have an issue", "legal advice",
        "madat chahiye", "kya karu", "urgent help", "police case", "advocate number",
        "need help", "help please", "please help", "lawyer help", "case help"
    ]
    if cleaned in generic_vague_phrases or (len(substantive_words) <= 2 and any(p in cleaned for p in generic_vague_phrases)):
        return True, "Your query is very broad. Please describe the specific situation in more detail."
        
    return False, ""
