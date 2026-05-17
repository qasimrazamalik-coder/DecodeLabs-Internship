# Project Explanation

## What is Data Classification?

Data classification means predicting a category or class for a given input. In this project, the model looks at flower measurements and predicts which Iris species the flower belongs to.

## What is the Iris Dataset?

The Iris dataset is a small and popular dataset used for beginner machine learning practice. It contains 150 flower samples, 4 measurement features, and 3 flower classes.

The features are sepal length, sepal width, petal length, and petal width. The classes are setosa, versicolor, and virginica.

## Why Train-Test Split?

Train-test split is used to check how well the model performs on data it has not seen before. The model learns from the training data, then it is tested on the testing data.

In this project, 80% of the data is used for training and 20% is used for testing. The split also uses `stratify=y`, so each class is represented fairly in both sets.

## Why Feature Scaling?

Feature scaling is important for KNN because KNN uses distance. If one feature has larger values than another feature, it can affect the distance more than it should.

StandardScaler helps put the feature values on a similar scale. The scaler is fitted only on the training data, then applied to both training and testing data.

## What is KNN?

KNN stands for K-Nearest Neighbors. It predicts a class by looking at the nearest data points in the training set.

For example, when `k=5`, the model checks the 5 closest training examples and predicts the class that appears the most.

## Why Try Different K Values?

Trying different K values helps compare how the model performs with different numbers of neighbors.

- Very small K can overfit because it may react too much to individual points.
- Very large K can underfit because it may make the model too general.
- Testing different K values helps find a better balance.

## What is a Confusion Matrix?

A confusion matrix shows correct and incorrect predictions for each class. It helps show which classes the model predicted correctly and where it made mistakes.

## What is F1 Score?

F1 score balances precision and recall. It is useful when we want one score that considers both false positives and false negatives.

## Streamlit Frontend

The Streamlit frontend lets users enter flower measurements with sliders. The app scales the values, sends them to the trained KNN model, and shows the predicted Iris species.

## What I Observed

The KNN model with `k=5` performed well on the Iris test set.

- Accuracy: 93.33%
- Precision: 94.44%
- Recall: 93.33%
- F1 Score: 93.27%
- Best K from 1 to 15: 1

The confusion matrix showed that all setosa and versicolor test samples were predicted correctly. Two virginica samples were predicted as versicolor, which lowered the final score slightly.
