# Project Explanation

## What is a Recommendation System?

A recommendation system suggests items that may be useful for a user. In this project, the system recommends learning resources based on the interests entered by the user.

## What is Content-Based Filtering?

Content-based filtering recommends items by looking at item features and user interests. If a user is interested in Python, machine learning, and automation, the system searches for resources with similar words in their titles, tags, categories, and descriptions.

## Why Not Collaborative Filtering Here?

Collaborative filtering usually needs many users, ratings, or past activity. This project uses a small learning resource dataset, so content-based filtering is a better fit because it can work with item details only.

## What is TF-IDF?

TF-IDF turns text into numbers. It gives higher importance to useful and specific words, and lower importance to very common words.

For example, words like `python`, `automation`, and `machine learning` help identify what a learning resource is about.

## What is Cosine Similarity?

Cosine similarity checks how close two vectors are in direction. In this project, it compares the user interest vector with each learning resource vector.

A higher similarity score means the item is a better match for the user's interests.

## The 4-Step Pipeline

1. Ingestion: Load the learning resource dataset and combine useful text columns.
2. Scoring: Convert text with TF-IDF and calculate cosine similarity.
3. Sorting: Sort items from highest similarity score to lowest.
4. Filtering: Return only the Top-N recommendations.

## Cold Start Problem

If a user gives no preferences, the recommendation system has very little information to work with. This makes recommendations weak. That is why the CLI project asks for at least 3 interests.

## Streamlit Frontend

The Streamlit frontend lets users select interests, type custom interests, and get recommendations without using the terminal. It also shows the similarity scores in a simple bar chart.

## What I Observed

I tested the project with this input:

```text
python, machine learning, automation
```

The system loaded 32 learning resources and returned these top 5 recommendations:

1. Machine Learning Starter - 0.5558
2. Feature Engineering Basics - 0.4854
3. Excel Automation - 0.3662
4. Automation with Python - 0.3562
5. Python Web Scraping - 0.3015

The highest result was Machine Learning Starter because it contains strong matches for machine learning, Python, and beginner model-building topics. Automation-related resources also appeared because automation was included in the user interests.
