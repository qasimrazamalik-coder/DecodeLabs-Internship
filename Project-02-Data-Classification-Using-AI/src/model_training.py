"""Model training functions for the Iris classification project."""

from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def train_knn_model(X_train, y_train, k=5):
    """Train a K-Nearest Neighbors classifier."""
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    return model


def test_k_values(X_train, X_test, y_train, y_test, max_k=15):
    """Test KNN accuracy for K values from 1 to max_k."""
    k_values = []
    accuracies = []

    for k in range(1, max_k + 1):
        model = train_knn_model(X_train, y_train, k)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        k_values.append(k)
        accuracies.append(accuracy)

    return k_values, accuracies
