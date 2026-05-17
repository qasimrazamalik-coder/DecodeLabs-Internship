"""Utility functions for Project 3."""

from pathlib import Path

import matplotlib.pyplot as plt


def ensure_dir(path):
    """Create a folder if it does not already exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def clean_text(text):
    """Clean text input for easier matching."""
    return text.lower().strip()


def save_results_text(recommendations, user_interests, output_path):
    """Save recommendation results to a text file."""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write("DecodeLabs AI Internship - Project 3 Results\n")
        file.write("Project: AI Recommendation Logic\n\n")
        file.write(f"User interests: {', '.join(user_interests)}\n")
        file.write(f"Number of recommendations: {len(recommendations)}\n\n")
        file.write("Top Recommendations:\n")

        for index, (_, row) in enumerate(recommendations.iterrows(), start=1):
            file.write(f"{index}. {row['title']}\n")
            file.write(f"   Category: {row['category']}\n")
            file.write(f"   Difficulty: {row['difficulty']}\n")
            file.write(f"   Similarity Score: {row['similarity_score']:.4f}\n")
            file.write(f"   Reason: {row['reason']}\n\n")

        file.write("Generated Output Files:\n")
        file.write("- outputs/sample_recommendations.csv\n")
        file.write("- outputs/similarity_scores.png\n")
        file.write("- outputs/results.txt\n")


def save_similarity_plot(recommendations, output_path):
    """Save a readable bar chart of recommendation similarity scores."""
    sorted_recommendations = recommendations.sort_values(
        by="similarity_score",
        ascending=True,
    )

    plt.figure(figsize=(9, 5))
    plt.barh(
        sorted_recommendations["title"],
        sorted_recommendations["similarity_score"],
        color="#4C78A8",
    )
    plt.title("Top Recommendation Similarity Scores")
    plt.xlabel("Similarity Score")
    plt.ylabel("Learning Resource")
    plt.xlim(0, max(sorted_recommendations["similarity_score"]) + 0.05)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
