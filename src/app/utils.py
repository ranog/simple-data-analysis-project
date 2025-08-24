import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file into a DataFrame."""
    return pd.read_csv(path)
