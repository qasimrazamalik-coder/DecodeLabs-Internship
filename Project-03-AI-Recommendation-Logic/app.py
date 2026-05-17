"""Streamlit frontend for the recommendation system."""

import matplotlib.pyplot as plt
import streamlit as st

from src.data_loader import create_search_text, load_items_dataset
from src.recommender import build_user_profile, recommend_items
from src.utils import clean_text


INTEREST_OPTIONS = [
    "Python",
    "Machine Learning",
    "Artificial Intelligence",
    "Data Analytics",
    "Web Development",
    "Frontend",
    "Backend",
    "Cybersecurity",
    "Cloud Computing",
    "Automation",
    "Computer Vision",
    "NLP",
    "SQL",
    "Portfolio Projects",
]


@st.cache_data
def load_data():
    """Load the item dataset for the app."""
    items = load_items_dataset("data/items.csv")
    return create_search_text(items)


def show_similarity_chart(recommendations):
    """Show a simple similarity score bar chart."""
    chart_data = recommendations.sort_values("similarity_score", ascending=True)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(chart_data["title"], chart_data["similarity_score"], color="#4C78A8")
    ax.set_xlabel("Similarity Score")
    ax.set_ylabel("Learning Resource")
    ax.set_title("Recommendation Scores")
    ax.set_xlim(0, max(chart_data["similarity_score"]) + 0.05)
    fig.tight_layout()
    st.pyplot(fig)


st.title("AI Recommendation System")
st.write("DecodeLabs AI Internship - Project 3")
st.write(
    "This app recommends learning resources based on user interests using "
    "TF-IDF and cosine similarity."
)

top_n = st.sidebar.slider("Number of recommendations", 3, 10, 5)
selected_interests = st.sidebar.multiselect("Select interests", INTEREST_OPTIONS)
custom_interests = st.text_input(
    "Add custom interests separated by commas",
    placeholder="python, machine learning, automation",
)

if st.button("Get Recommendations"):
    typed_interests = [
        clean_text(interest)
        for interest in custom_interests.split(",")
        if clean_text(interest)
    ]
    all_interests = [clean_text(interest) for interest in selected_interests]
    all_interests.extend(typed_interests)
    all_interests = list(dict.fromkeys(all_interests))

    if len(all_interests) < 3:
        st.info("Please select or type at least 3 interests.")
    else:
        items = load_data()
        user_profile = build_user_profile(all_interests)
        recommendations = recommend_items(items, user_profile, top_n=top_n)

        st.success("Recommendations generated.")

        for _, row in recommendations.iterrows():
            st.subheader(row["title"])
            st.write(f"Category: {row['category']}")
            st.write(f"Difficulty: {row['difficulty']}")
            st.write(f"Similarity score: {row['similarity_score'] * 100:.2f}%")
            st.write(f"Tags: {row['tags']}")
            st.write(row["description"])
            st.info(row["reason"])

        show_similarity_chart(recommendations)

st.subheader("Small Explanation")
st.write(
    "Content-based filtering recommends items by comparing user interests "
    "with item details like tags and descriptions."
)
st.write(
    "TF-IDF turns text into numbers and gives more weight to useful words."
)
st.write(
    "Cosine similarity checks how close the user profile is to each item. "
    "A higher score means a better match."
)
