"""CLI app for DecodeLabs Project 3: AI Recommendation Logic."""

from pathlib import Path

from src.data_loader import create_search_text, load_items_dataset
from src.recommender import build_user_profile, recommend_items
from src.utils import clean_text, ensure_dir, save_results_text, save_similarity_plot


DATA_PATH = Path("data") / "items.csv"
OUTPUT_DIR = Path("outputs")
RECOMMENDATIONS_PATH = OUTPUT_DIR / "sample_recommendations.csv"
PLOT_PATH = OUTPUT_DIR / "similarity_scores.png"
RESULTS_PATH = OUTPUT_DIR / "results.txt"


def get_user_interests():
    """Ask the user for at least 3 comma-separated interests."""
    while True:
        raw_input = input("Enter at least 3 interests separated by commas:\n")

        if not raw_input.strip():
            print("Please enter your interests before continuing.\n")
            continue

        interests = [
            clean_text(interest)
            for interest in raw_input.split(",")
            if clean_text(interest)
        ]

        if len(interests) < 3:
            print("Please enter at least 3 interests, separated by commas.\n")
            continue

        return interests


def print_recommendations(recommendations):
    """Print recommendations in a clear terminal format."""
    print("\nTop Recommendations:")

    for rank, (_, row) in enumerate(recommendations.iterrows(), start=1):
        print(f"{rank}. {row['title']}")
        print(f"   Category: {row['category']}")
        print(f"   Difficulty: {row['difficulty']}")
        print(f"   Similarity Score: {row['similarity_score']:.4f}")
        print(f"   Reason: {row['reason']}\n")


def main():
    """Run the recommendation pipeline."""
    ensure_dir(OUTPUT_DIR)

    print("DecodeLabs AI Internship - Project 3")
    print("AI Recommendation Logic\n")

    items = load_items_dataset(DATA_PATH)
    items = create_search_text(items)

    print("Dataset loaded successfully.")
    print(f"Number of items: {len(items)}\n")

    user_interests = get_user_interests()
    user_profile = build_user_profile(user_interests)

    print(f"\nUser interests: {', '.join(user_interests)}")

    recommendations = recommend_items(items, user_profile, top_n=5)
    print_recommendations(recommendations)

    recommendations.drop(columns=["search_text"]).to_csv(
        RECOMMENDATIONS_PATH,
        index=False,
    )
    save_similarity_plot(recommendations, PLOT_PATH)
    save_results_text(recommendations, user_interests, RESULTS_PATH)

    print("Output files saved:")
    print(f"- {RECOMMENDATIONS_PATH}")
    print(f"- {PLOT_PATH}")
    print(f"- {RESULTS_PATH}")


if __name__ == "__main__":
    main()
