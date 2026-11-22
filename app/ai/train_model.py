"""JusticeGram AI Module - Model Training and Evaluation Script
Trains a TF-IDF + Logistic Regression classification pipeline on synthetic legal query data.
Evaluates accuracy, precision, recall, and F1-score across all 10 legal categories.
"""

import sys
import os
import csv
from pathlib import Path
from collections import Counter
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Ensure the root directory is on the path so app modules can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from app.ai.preprocessor import preprocess_for_model
from app.config import Config

def load_dataset(csv_path):
    """Loads query and category pairs from a CSV file."""
    queries = []
    categories = []
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            q = row['query'].strip()
            c = row['category'].strip()
            if q and c:
                queries.append(q)
                categories.append(c)
    return queries, categories

def train_and_evaluate(data_path=None, model_dir=None):
    """Loads dataset, trains TF-IDF + LogisticRegression model, evaluates, and saves artifacts."""
    if data_path is None:
        data_path = Config.SAMPLE_DATA_PATH
    if model_dir is None:
        model_dir = Config.MODEL_DIR

    model_dir = Path(model_dir)
    model_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 65)
    print("  JUSTICEGRAM AI LEGAL CLASSIFIER - TRAINING & EVALUATION PIPELINE")
    print("=" * 65)
    print(f"[*] Loading training dataset from: {data_path}")

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset file not found at: {data_path}")

    raw_queries, categories = load_dataset(data_path)
    print(f"[*] Total labeled samples loaded: {len(raw_queries)}")
    print(f"[*] Distribution across legal categories:")
    counts = Counter(categories)
    for cat, count in sorted(counts.items()):
        print(f"    - {cat:28s}: {count:3d} samples")

    # Preprocessing
    print("\n[*] Preprocessing and normalizing query texts...")
    clean_queries = [preprocess_for_model(q) for q in raw_queries]

    # Stratified Train-Test Split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        clean_queries, categories, test_size=0.20, random_state=42, stratify=categories
    )
    print(f"[*] Train set size: {len(X_train)} | Test evaluation set size: {len(X_test)}")

    # Vectorizer setup with unigrams + bigrams and sublinear TF scaling
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=1,
        sublinear_tf=True,
        max_features=2500
    )

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Classifier setup - Multinomial Logistic Regression with balanced class weights
    classifier = LogisticRegression(
        C=2.5,
        max_iter=1000,
        class_weight='balanced',
        random_state=42
    )

    print("[*] Training Logistic Regression classifier on TF-IDF feature space...")
    classifier.fit(X_train_vec, y_train)

    # Evaluation on holdout test set
    y_pred = classifier.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 65)
    print(f"  EVALUATION METRICS ON HOLDOUT TEST SET (Accuracy: {accuracy * 100:.2f}%)")
    print("=" * 65)
    print(classification_report(y_test, y_pred, zero_division=0))

    # Retrain on full dataset to maximize production coverage
    print("[*] Fitting final model on complete dataset for deployment...")
    full_vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        min_df=1,
        sublinear_tf=True,
        max_features=3000
    )
    X_full_vec = full_vectorizer.fit_transform(clean_queries)
    final_classifier = LogisticRegression(
        C=2.5,
        max_iter=1000,
        class_weight='balanced',
        random_state=42
    )
    final_classifier.fit(X_full_vec, categories)

    # Save artifacts
    vectorizer_path = model_dir / 'tfidf.joblib'
    model_path = model_dir / 'model.joblib'

    joblib.dump(full_vectorizer, vectorizer_path)
    joblib.dump(final_classifier, model_path)

    print(f"[+] Saved Vectorizer to: {vectorizer_path}")
    print(f"[+] Saved Classifier Model to: {model_path}")
    print("=" * 65)
    print("  MODEL TRAINING COMPLETED SUCCESSFULLY")
    print("=" * 65)

    return {
        'accuracy': accuracy,
        'vectorizer_path': str(vectorizer_path),
        'model_path': str(model_path)
    }

if __name__ == '__main__':
    train_and_evaluate()
