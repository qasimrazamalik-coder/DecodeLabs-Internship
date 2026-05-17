"""Evaluation and plotting functions for the Iris classification project."""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def evaluate_model(model, X_test, y_test, target_names):
    """Evaluate the trained model and return the important results."""
    y_pred = model.predict(X_test)

    results = {
        "y_pred": y_pred,
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted"),
        "recall": recall_score(y_test, y_pred, average="weighted"),
        "f1_score": f1_score(y_test, y_pred, average="weighted"),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(
            y_test,
            y_pred,
            target_names=target_names,
        ),
    }

    return results


def save_confusion_matrix(y_test, y_pred, target_names, output_path):
    """Save a confusion matrix plot as an image."""
    matrix = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))
    plt.imshow(matrix, interpolation="nearest", cmap="Blues")
    plt.title("Confusion Matrix")
    plt.colorbar()

    tick_marks = np.arange(len(target_names))
    plt.xticks(tick_marks, target_names)
    plt.yticks(tick_marks, target_names)

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            plt.text(
                col,
                row,
                matrix[row, col],
                ha="center",
                va="center",
                color="white" if matrix[row, col] > matrix.max() / 2 else "black",
            )

    plt.xlabel("Predicted Class")
    plt.ylabel("Actual Class")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_k_accuracy_plot(k_values, accuracies, output_path):
    """Save a line plot showing K value against test accuracy."""
    plt.figure(figsize=(8, 5))
    plt.plot(k_values, accuracies, marker="o")
    plt.title("K Value vs Accuracy")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")
    plt.xticks(k_values)
    plt.ylim(0.8, 1.05)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
