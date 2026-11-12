"""Reusable analysis functions for this project."""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    return pd.read_csv(path)


def validate_required_columns(df: pd.DataFrame, required: list[str]) -> None:
    """Raise a helpful error when required columns are missing."""
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
