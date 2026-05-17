# AI Recommendation Logic

## Overview

This project is part of my DecodeLabs Artificial Intelligence Internship. The goal is to build a simple recommendation system that suggests learning resources based on user interests.

## Objective

To take user preferences, compare them with item details, and display the most relevant recommendations.

## Dataset

The dataset contains learning resources with:

- title
- category
- difficulty
- tags
- description

There are 32 learning resources in `data/items.csv`.

## Recommendation Method

Content-Based Filtering

This method recommends items by comparing user interests with item features. If the user's interests are similar to an item's tags and description, that item gets a higher recommendation score.

## How It Works

1. User enters interests.
2. Item text is converted into numerical vectors using TF-IDF.
3. User interests are also converted into a vector.
4. Cosine similarity compares the user vector with item vectors.
5. Items are sorted by similarity score.
6. Top recommendations are displayed.

## Features

- Takes user interests as input
- Uses TF-IDF vectorization
- Uses cosine similarity
- Generates Top-N recommendations
- Saves recommendation results
- Creates similarity score chart
- Includes Streamlit frontend

## Concepts Used

- Recommendation systems
- Content-based filtering
- TF-IDF
- Cosine similarity
- Similarity scoring
- Sorting and ranking
- Top-N filtering
- Streamlit frontend

## Folder Structure

```text
Project-03-AI-Recommendation-Logic/
|-- README.md
|-- requirements.txt
|-- main.py
|-- app.py
|-- data/
|   `-- items.csv
|-- src/
|   |-- data_loader.py
|   |-- recommender.py
|   `-- utils.py
|-- outputs/
|   |-- sample_recommendations.csv
|   |-- similarity_scores.png
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

## Run CLI Project

```bash
python main.py
```

## Run Streamlit App

```bash
streamlit run app.py
```

## Output Files

- outputs/sample_recommendations.csv
- outputs/similarity_scores.png
- outputs/results.txt

## Example Input

```text
python, machine learning, automation
```

## Example Output

Actual top recommendations from running `main.py`:

| Rank | Title | Similarity Score |
|------|-------|------------------|
| 1 | Machine Learning Starter | 0.5558 |
| 2 | Feature Engineering Basics | 0.4854 |
| 3 | Excel Automation | 0.3662 |
| 4 | Automation with Python | 0.3562 |
| 5 | Python Web Scraping | 0.3015 |

## What I Learned

- I learned how recommendation systems work.
- I learned how user interests can be matched with item features.
- I learned how TF-IDF converts text into numbers.
- I learned how cosine similarity measures closeness between user preferences and items.
- I learned how to show recommendations in a simple Streamlit frontend.

## Internship Info

Company: DecodeLabs  
Domain: Artificial Intelligence  
Project: 3  
Batch: 2026
