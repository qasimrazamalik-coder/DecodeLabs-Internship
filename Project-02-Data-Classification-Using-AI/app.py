"""Streamlit app for predicting Iris flower species."""

import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def train_model():
    """Train the KNN model used by the Streamlit app."""
    iris_data = load_iris()
    X = iris_data.data
    y = iris_data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)

    predictions = model.predict(X_test_scaled)
    test_accuracy = accuracy_score(y_test, predictions)

    return model, scaler, iris_data.target_names, test_accuracy


st.title("Iris Flower Classification App")

st.write("This app was built for DecodeLabs AI Internship Project 2.")
st.write("It uses KNN classification on the Iris dataset.")

model, scaler, target_names, test_accuracy = train_model()

st.sidebar.header("Flower Measurements")
sepal_length = st.sidebar.slider("Sepal length in cm", 4.0, 8.0, 5.8)
sepal_width = st.sidebar.slider("Sepal width in cm", 2.0, 4.5, 3.0)
petal_length = st.sidebar.slider("Petal length in cm", 1.0, 7.0, 4.0)
petal_width = st.sidebar.slider("Petal width in cm", 0.1, 2.5, 1.2)

user_input = pd.DataFrame(
    [[sepal_length, sepal_width, petal_length, petal_width]],
    columns=[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ],
)

scaled_input = scaler.transform(user_input.values)
prediction = model.predict(scaled_input)
predicted_class = target_names[prediction[0]]

st.subheader("Prediction")
st.success(f"Predicted Iris species: {predicted_class}")

st.subheader("Model Info")
st.info(
    f"Algorithm: K-Nearest Neighbors\n\n"
    f"Dataset: Iris\n\n"
    f"K value: 5\n\n"
    f"Test accuracy: {test_accuracy * 100:.2f}%"
)

st.subheader("Small Explanation")
st.write(
    "KNN predicts a class by checking the nearest training examples and using "
    "majority vote."
)
st.write(
    "Scaling is used because KNN depends on distance. Scaling keeps all feature "
    "values on a fair range."
)
