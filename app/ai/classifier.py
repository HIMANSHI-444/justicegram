import os
import re
import joblib
from pathlib import Path
from app.ai.preprocessor import clean_text, preprocess_for_model, is_query_ambiguous
from app.ai.legal_knowledge import LEGAL_CATEGORIES, get_relevant_indian_laws, detect_subcategory
from app.config import Config

class LegalClassifier:
    """Production AI inference engine for JusticeGram.
    Combines TF-IDF + Logistic Regression with domain keyword heuristics,
    sub-category identification, verified Indian law retrieval,
    confidence scoring, and ambiguity detection.
    """

    def __init__(self, model_path=None, vectorizer_path=None):
        self.model_path = Path(model_path) if model_path else Config.CLASSIFIER_MODEL_PATH
        self.vectorizer_path = Path(vectorizer_path) if vectorizer_path else Config.VECTORIZER_PATH
        self.model = None
        self.vectorizer = None
        self.load_artifacts()

    def load_artifacts(self):
        """Loads serialized TF-IDF vectorizer and Logistic Regression model."""
        try:
            if self.model_path.exists() and self.vectorizer_path.exists():
                self.vectorizer = joblib.load(self.vectorizer_path)
                self.model = joblib.load(self.model_path)
                print(f"[AI Engine] Successfully loaded model from {self.model_path}")
            else:
                print("[AI Engine] Model artifacts not found. Operating in keyword heuristic mode.")
        except Exception as e:
            print(f"[AI Engine] Error loading model artifacts: {e}. Falling back to heuristics.")
            self.model = None
            self.vectorizer = None

    def _keyword_heuristic_classify(self, text: str) -> tuple[str, float, list[str]]:
        """Fallback rule-based classifier based on domain keywords with word-boundary matching."""
        cleaned = clean_text(text)
        best_category = "Other / Needs Clarification"
        max_matches = 0
        matched_keywords = []

        for category, info in LEGAL_CATEGORIES.items():
            if category == "Other / Needs Clarification":
                continue
            cat_keywords = info.get("keywords", [])
            matches = []
            for kw in cat_keywords:
                # Use regex word boundaries to avoid false substring matches
                pattern = r'\b' + re.escape(kw) + r'\b'
                if re.search(pattern, cleaned):
                    matches.append(kw)

            if len(matches) > max_matches:
                max_matches = len(matches)
                best_category = category
                matched_keywords = matches

        if max_matches == 0:
            return "Other / Needs Clarification", 25.0, []
        
        # Calculate heuristic confidence: 1 match -> ~55%, 2 -> ~72%, 3+ -> ~85-92%
        confidence = min(92.0, 45.0 + (max_matches * 15.0))
        return best_category, confidence, matched_keywords

    def classify(self, query_text: str, manual_category: str = None) -> dict:
        """Executes the complete multi-stage AI classification pipeline.
        Supports manual category override if user specifies a preference.
        """
        # 1. Validation
        if not query_text or not query_text.strip():
            return {
                "success": False,
                "error": "Please provide a description of your legal situation."
            }

        if len(query_text.strip()) > 3000:
            return {
                "success": False,
                "error": "Submission is too long (maximum 3,000 characters). Please summarize the main problem."
            }

        raw_query = query_text.strip()

        # 2. Manual Category Selection (if requested by user)
        if manual_category and manual_category in LEGAL_CATEGORIES and manual_category != "Other / Needs Clarification":
            cat_data = LEGAL_CATEGORIES[manual_category]
            subcat = detect_subcategory(manual_category, raw_query)
            relevant_laws = get_relevant_indian_laws(manual_category, subcat, raw_query)
            return {
                "success": True,
                "query": raw_query,
                "category": manual_category,
                "subcategory": subcat,
                "confidence": 100.0,
                "is_ambiguous": False,
                "ambiguity_reason": None,
                "method_used": "Manual User Selection",
                "explanation": f"Categorized under '{manual_category}' as manually requested by the user.",
                "why_classified": f"You manually selected '{manual_category}'. The subcategory '{subcat}' was identified based on relevant keywords in your text.",
                "guidance": cat_data["guidance"],
                "relevant_laws": relevant_laws,
                "important_documents": cat_data["important_documents"],
                "suggested_next_steps": cat_data["suggested_next_steps"],
                "official_resources": cat_data["official_resources"],
                "clarifying_prompts": cat_data["clarifying_prompts"],
                "badge_color": "navy",
                "icon": cat_data["icon"]
            }

        # 3. Ambiguity & Vague Input Detection
        ambiguous, reason = is_query_ambiguous(raw_query)
        if ambiguous:
            cat_data = LEGAL_CATEGORIES.get("Other / Needs Clarification")
            relevant_laws = get_relevant_indian_laws("Other / Needs Clarification", None, raw_query)
            return {
                "success": True,
                "query": raw_query,
                "category": "Other / Needs Clarification",
                "subcategory": "General Inquiry Requiring Details",
                "confidence": 28.0,
                "is_ambiguous": True,
                "ambiguity_reason": reason,
                "method_used": "Ambiguity Detector",
                "explanation": f"Your input is broad or lacks key legal details: {reason}",
                "why_classified": "The query contains general keywords or lacks specific party/remedy information. Additional details or manual category selection will improve accuracy.",
                "guidance": cat_data["guidance"],
                "relevant_laws": relevant_laws,
                "important_documents": cat_data["important_documents"],
                "suggested_next_steps": cat_data["suggested_next_steps"],
                "official_resources": cat_data["official_resources"],
                "clarifying_prompts": cat_data["clarifying_prompts"],
                "badge_color": "secondary",
                "icon": cat_data["icon"]
            }

        # 4. Model Inference or Fallback
        predicted_category = "Other / Needs Clarification"
        confidence = 0.0
        method_used = "Keyword Heuristic"
        matched_keywords = []

        if self.model is not None and self.vectorizer is not None:
            try:
                clean_q = preprocess_for_model(raw_query)
                vec = self.vectorizer.transform([clean_q])
                probabilities = self.model.predict_proba(vec)[0]
                classes = self.model.classes_

                best_idx = probabilities.argmax()
                model_category = classes[best_idx]
                model_confidence = float(probabilities[best_idx] * 100.0)

                # Heuristic cross-check for high domain safety
                kw_category, kw_confidence, kw_matches = self._keyword_heuristic_classify(raw_query)

                # If model confidence is acceptable (>= 30%), use model prediction
                if model_confidence >= 30.0:
                    predicted_category = model_category
                    confidence = round(model_confidence, 1)
                    method_used = "TF-IDF + Logistic Regression Classifier"
                    matched_keywords = kw_matches
                elif kw_matches:
                    predicted_category = kw_category
                    confidence = round(kw_confidence, 1)
                    method_used = "Keyword Heuristic (Model Confidence Low)"
                    matched_keywords = kw_matches
                else:
                    predicted_category = model_category
                    confidence = round(model_confidence, 1)
                    method_used = "TF-IDF + Logistic Regression Classifier"

            except Exception as e:
                print(f"[AI Engine] Error in model inference: {e}. Falling back to keywords.")
                predicted_category, confidence, matched_keywords = self._keyword_heuristic_classify(raw_query)
                method_used = "Keyword Heuristic (Inference Fallback)"
        else:
            predicted_category, confidence, matched_keywords = self._keyword_heuristic_classify(raw_query)
            method_used = "Keyword Heuristic (Model Unloaded)"

        # 5. Low Confidence Check
        is_low_confidence = confidence < 35.0
        if is_low_confidence and predicted_category != "Other / Needs Clarification":
            explanation = (
                f"We identified potential elements of '{predicted_category}' with lower confidence ({confidence}%). "
                "Because your query may have overlapping legal elements, you can review our clarifying questions or manually pick a category."
            )
            why_classified = f"Low confidence match ({confidence}%). Query contains overlapping or subtle legal signals."
        elif matched_keywords:
            explanation = (
                f"Identified as '{predicted_category}' based on contextual legal analysis and key indicators "
                f"({', '.join(matched_keywords[:3])})."
            )
            why_classified = f"Categorized based on key legal indicators: {', '.join(matched_keywords[:4])}."
        else:
            explanation = f"Categorized as '{predicted_category}' with {confidence}% confidence based on trained Indian legal patterns."
            why_classified = f"Machine learning feature vectors aligned with known patterns in {predicted_category}."

        # 6. Subcategory and Indian Law Retrieval
        subcat = detect_subcategory(predicted_category, raw_query)
        cat_data = LEGAL_CATEGORIES.get(predicted_category, LEGAL_CATEGORIES["Other / Needs Clarification"])
        relevant_laws = get_relevant_indian_laws(predicted_category, subcat, raw_query)

        return {
            "success": True,
            "query": raw_query,
            "category": predicted_category,
            "subcategory": subcat,
            "confidence": confidence,
            "is_ambiguous": is_low_confidence,
            "ambiguity_reason": "Multiple overlapping areas detected; review clarifying prompts or select category manually" if is_low_confidence else None,
            "method_used": method_used,
            "explanation": explanation,
            "why_classified": why_classified,
            "guidance": cat_data["guidance"],
            "relevant_laws": relevant_laws,
            "important_documents": cat_data["important_documents"],
            "suggested_next_steps": cat_data["suggested_next_steps"],
            "official_resources": cat_data["official_resources"],
            "clarifying_prompts": cat_data["clarifying_prompts"],
            "badge_color": "navy",
            "icon": cat_data["icon"]
        }

# Global singleton classifier instance
ai_classifier = LegalClassifier()
