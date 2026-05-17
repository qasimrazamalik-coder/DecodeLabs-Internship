"""Content-based recommendation logic."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_user_profile(interests):
    """Create one text profile from a list of user interests."""
    cleaned_interests = [interest.strip().lower() for interest in interests if interest.strip()]
    return " ".join(cleaned_interests)


def recommend_items(df, user_profile, top_n=5):
    """Recommend top items using TF-IDF and cosine similarity."""
    search_texts = df["search_text"].tolist()
    all_texts = search_texts + [user_profile]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    item_vectors = tfidf_matrix[:-1]
    user_vector = tfidf_matrix[-1]

    similarity_scores = cosine_similarity(user_vector, item_vectors).flatten()

    recommendations = df.copy()
    recommendations["similarity_score"] = similarity_scores
    recommendations = recommendations.sort_values(
        by="similarity_score",
        ascending=False,
    )

    top_recommendations = recommendations.head(top_n).copy()
    top_recommendations["reason"] = top_recommendations.apply(
        explain_recommendation,
        axis=1,
    )

    return top_recommendations


def explain_recommendation(row):
    """Create a short reason for a recommendation."""
    category = str(row["category"]).lower()
    tags = str(row["tags"]).lower()

    if "machine learning" in tags:
        return "Recommended because it matches your interest in machine learning."
    if "automation" in tags:
        return "Recommended because it matches your interest in automation."
    if "python" in tags:
        return "Recommended because it matches your interest in Python."
    if "data analytics" in tags:
        return "Recommended because it matches your interest in data analytics."
    if "web development" in tags or category in ["frontend", "backend"]:
        return "Recommended because it matches your interest in web development."
    if "ai" in tags or "artificial intelligence" in category:
        return "Recommended because it matches your interest in AI."

    return "Recommended because its content is close to your selected interests."
