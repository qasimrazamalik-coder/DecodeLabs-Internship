# Data Classification Using AI

## Overview

This project is part of my DecodeLabs Artificial Intelligence Internship. The goal is to build a basic supervised learning classification model using the Iris dataset.

## Objective

To train a machine learning model that can classify Iris flowers into three species using flower measurements.

## Dataset

Dataset: Iris dataset

Details:

- 150 samples
- 4 input features
- 3 target classes

Features:

- Sepal length
- Sepal width
- Petal length
- Petal width

Classes:

- Setosa
- Versicolor
- Virginica

## Algorithm Used

K-Nearest Neighbors, also called KNN.

KNN predicts the class of a new data point by checking the closest data points in the training data and using majority vote.

## Features of This Project

- Loads Iris dataset
- Splits data into training and testing sets
- Applies feature scaling
- Trains KNN classifier
- Tests different K values
- Evaluates model using accuracy, precision, recall, and F1 score
- Generates confusion matrix
- Includes Streamlit frontend for prediction

## Concepts Used

- Supervised learning
- Classification
- Train-test split
- Feature scaling
- KNN algorithm
- Confusion matrix
- F1 score
- Model validation
- Streamlit frontend

## Folder Structure

```text
Project-02-Data-Classification-Using-AI/
|-- README.md
|-- requirements.txt
|-- main.py
|-- app.py
|-- src/
|   |-- data_preprocessing.py
|   |-- model_training.py
|   `-- evaluation.py
|-- outputs/
|   |-- confusion_matrix.png
|   |-- k_value_accuracy.png
|   `-- results.txt
|-- docs/
|   `-- project_explanation.md
`-- demo/
    `-- demo_transcript.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the ML Project

```bash
python main.py
```

## Run the Streamlit App

```bash
streamlit run app.py
```

## Output Files

- outputs/confusion_matrix.png
- outputs/k_value_accuracy.png
- outputs/results.txt

## Example Results

After running `main.py`, these were the actual results:

- Accuracy: 0.9333 (93.33%)
- Precision: 0.9444 (94.44%)
- Recall: 0.9333 (93.33%)
- F1 Score: 0.9327 (93.27%)
- Best K: 1

## What I Learned

- I learned how classification works in supervised learning.
- I learned how to split data into training and testing sets.
- I learned why feature scaling is important for KNN.
- I learned how to evaluate a model using confusion matrix and F1 score.
- I learned how to create a simple frontend for an ML model using Streamlit.

## Internship Info

Company: DecodeLabs  
Domain: Artificial Intelligence  
Project: 2  
Batch: 2026
