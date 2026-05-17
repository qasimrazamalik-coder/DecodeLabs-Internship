"""Dataset loading helpers for the recommendation project."""

import pandas as pd


REQUIRED_COLUMNS = [
    "item_id",
    "title",
    "category",
    "difficulty",
    "tags",
    "description",
]


def load_items_dataset(file_path):
    """Load the learning resources dataset and check required columns."""
    dataframe = pd.read_csv(file_path)

    missing_columns = [
        column for column in REQUIRED_COLUMNS if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return dataframe


def create_search_text(df):
    """Combine useful text columns into one search_text column."""
    dataframe = df.copy()
    text_columns = ["title", "category", "difficulty", "tags", "description"]

    for column in text_columns:
        dataframe[column] = dataframe[column].fillna("").astype(str)

    dataframe["search_text"] = (
        dataframe["title"]
        + " "
        + dataframe["category"]
        + " "
        + dataframe["difficulty"]
        + " "
        + dataframe["tags"]
        + " "
        + dataframe["description"]
    )

    return dataframe
