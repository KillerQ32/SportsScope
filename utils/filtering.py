import pandas as pd

def filter_df(df: pd.DataFrame, year: int, cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    # changes all columns in col to numbers if that fails it changes it to NA
    # then any NA value is turned to 0. changes all numbers to make sure its an int rather than float
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)
    # checks rows across specified columns for any values 
    df = df[df[cols].sum(axis=1)>0]
    df["Year"] = year
    return df

def get_names_only(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    df = df.drop(cols, axis=1)
    return df

def combine_df(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(dfs, axis=0)
    df = df.drop_duplicates()
    return df