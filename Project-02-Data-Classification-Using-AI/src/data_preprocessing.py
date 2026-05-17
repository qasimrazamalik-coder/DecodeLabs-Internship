"""Data loading and preprocessing functions for the Iris project."""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_iris_dataframe():
    """Load the Iris dataset and return features, labels, and a DataFrame."""
    iris_data = load_iris()

    X = iris_data.data
    y = iris_data.target
    feature_names = list(iris_data.feature_names)
    target_names = [str(name) for name in iris_data.target_names]

    dataframe = pd.DataFrame(X, columns=feature_names)
    dataframe["target"] = y
    dataframe["class"] = dataframe["target"].apply(lambda value: target_names[value])

    return X, y, feature_names, target_names, dataframe


def split_and_scale_data(X, y, test_size=0.2, random_state=42):
    """Split the dataset and apply StandardScaler to the feature values."""
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
