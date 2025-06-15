import pandas as pd

def filter_df(df: pd.DataFrame, year: int, cols: list[str]) -> pd.DataFrame:
    """
    Filter rows where any of the specified columns contain values > 0.

    Args:
        df (pd.DataFrame): Input dataframe.
        year (int): Year to assign to the filtered rows.
        cols (list[str]): List of column names to check.

    Returns:
        pd.DataFrame: Filtered dataframe with 'Year' column added.
    """
    df = df.copy()

    # Convert specified columns to numeric, coercing non-numeric to NaN, then fill NaN with 0
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)

    # Keep only rows where sum across specified columns > 0
    df = df[df[cols].sum(axis=1) > 0]

    # Add year column
    df["Year"] = year
    return df


def strip_columns(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    Drop specified columns from the dataframe.

    Args:
        df (pd.DataFrame): Input dataframe.
        cols (list[str]): List of columns to drop.

    Returns:
        pd.DataFrame: Dataframe with specified columns removed.
    """
    df = df.drop(cols, axis=1)
    return df


def combine_df(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatenate multiple dataframes and drop duplicate rows.

    This ensures that players with identical data appear only once, but
    allows multiple rows for players with the same name but different stats.

    Args:
        dfs (list[pd.DataFrame]): List of dataframes to combine.

    Returns:
        pd.DataFrame: Combined dataframe with duplicates removed.
    """
    df = pd.concat(dfs, axis=0)
    df = df.drop_duplicates()
    return df
