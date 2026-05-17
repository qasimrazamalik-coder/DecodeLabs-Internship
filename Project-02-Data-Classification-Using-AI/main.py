"""Main file for DecodeLabs Project 2: Data Classification Using AI."""

from pathlib import Path

from src.data_preprocessing import load_iris_dataframe, split_and_scale_data
from src.evaluation import (
    evaluate_model,
    save_confusion_matrix,
    save_k_accuracy_plot,
)
from src.model_training import test_k_values, train_knn_model


OUTPUT_DIR = Path("outputs")
CONFUSION_MATRIX_PATH = OUTPUT_DIR / "confusion_matrix.png"
K_ACCURACY_PATH = OUTPUT_DIR / "k_value_accuracy.png"
RESULTS_PATH = OUTPUT_DIR / "results.txt"


def format_percent(value):
    """Format a decimal score as a percentage string."""
    return f"{value * 100:.2f}%"


def write_results_file(
    dataset_shape,
    feature_names,
    target_names,
    train_size,
    test_size,
    results,
    best_k,
    best_accuracy,
    k_values,
    accuracies,
):
    """Save the important results to outputs/results.txt."""
    with RESULTS_PATH.open("w", encoding="utf-8") as file:
        file.write("DecodeLabs AI Internship - Project 2 Results\n")
        file.write("Project: Data Classification Using AI\n\n")

        file.write(f"Dataset shape: {dataset_shape}\n")
        file.write(f"Feature names: {list(feature_names)}\n")
        file.write(f"Target classes: {list(target_names)}\n")
        file.write(f"Training samples: {train_size}\n")
        file.write(f"Testing samples: {test_size}\n\n")

        file.write("KNN Model Result (k=5)\n")
        file.write(f"Accuracy: {results['accuracy']:.4f} ({format_percent(results['accuracy'])})\n")
        file.write(f"Precision: {results['precision']:.4f} ({format_percent(results['precision'])})\n")
        file.write(f"Recall: {results['recall']:.4f} ({format_percent(results['recall'])})\n")
        file.write(f"F1 Score: {results['f1_score']:.4f} ({format_percent(results['f1_score'])})\n\n")

        file.write("Confusion Matrix:\n")
        file.write(f"{results['confusion_matrix']}\n\n")

        file.write("Classification Report:\n")
        file.write(results["classification_report"])
        file.write("\n")

        file.write("K Value Testing:\n")
        for k, accuracy in zip(k_values, accuracies):
            file.write(f"K={k}: {accuracy:.4f} ({format_percent(accuracy)})\n")

        file.write(f"\nBest K: {best_k}\n")
        file.write(f"Best K Accuracy: {best_accuracy:.4f} ({format_percent(best_accuracy)})\n\n")

        file.write("Generated Output Files:\n")
        file.write("- outputs/confusion_matrix.png\n")
        file.write("- outputs/k_value_accuracy.png\n")
        file.write("- outputs/results.txt\n")


def main():
    """Run the full Iris classification pipeline."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    X, y, feature_names, target_names, dataframe = load_iris_dataframe()

    print("DecodeLabs AI Internship - Project 2")
    print("Data Classification Using AI\n")
    print(f"Dataset shape: {dataframe.shape}")
    print(f"Feature names: {list(feature_names)}")
    print(f"Target classes: {list(target_names)}")
    print("\nFirst 5 rows:")
    print(dataframe.head())

    X_train, X_test, y_train, y_test, scaler = split_and_scale_data(X, y)

    print("\nTrain-test split:")
    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    model = train_knn_model(X_train, y_train, k=5)
    results = evaluate_model(model, X_test, y_test, target_names)

    print("\nKNN Model Result (k=5):")
    print(f"Accuracy: {results['accuracy']:.4f} ({format_percent(results['accuracy'])})")
    print(f"Precision: {results['precision']:.4f} ({format_percent(results['precision'])})")
    print(f"Recall: {results['recall']:.4f} ({format_percent(results['recall'])})")
    print(f"F1 Score: {results['f1_score']:.4f} ({format_percent(results['f1_score'])})")

    print("\nConfusion Matrix:")
    print(results["confusion_matrix"])

    print("\nClassification Report:")
    print(results["classification_report"])

    k_values, accuracies = test_k_values(X_train, X_test, y_train, y_test, max_k=15)
    best_accuracy = max(accuracies)
    best_k = k_values[accuracies.index(best_accuracy)]

    print("K Value Testing:")
    for k, accuracy in zip(k_values, accuracies):
        print(f"K={k}: {accuracy:.4f} ({format_percent(accuracy)})")

    print(f"\nBest K: {best_k}")
    print(f"Best K Accuracy: {best_accuracy:.4f} ({format_percent(best_accuracy)})")

    save_confusion_matrix(y_test, results["y_pred"], target_names, CONFUSION_MATRIX_PATH)
    save_k_accuracy_plot(k_values, accuracies, K_ACCURACY_PATH)
    write_results_file(
        dataframe.shape,
        feature_names,
        target_names,
        len(X_train),
        len(X_test),
        results,
        best_k,
        best_accuracy,
        k_values,
        accuracies,
    )

    print("\nOutput files saved:")
    print(f"- {CONFUSION_MATRIX_PATH}")
    print(f"- {K_ACCURACY_PATH}")
    print(f"- {RESULTS_PATH}")


if __name__ == "__main__":
    main()
