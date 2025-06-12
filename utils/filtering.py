import pandas as pd

def filter_df(df: pd.DataFrame, year: int, cols: list[str]) -> pd.DataFrame:
    """
    checks for value greater than 0 in specified columns. applys row wise. 
    if a player has a stat recoreded in any columns specified it keeps them.
    """
    df = df.copy()
    # changes all columns in col to numbers if that fails it changes it to NA
    # then any NA value is turned to 0. changes all numbers to make sure its an int rather than float
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)
    # checks rows across specified columns for any values 
    df = df[df[cols].sum(axis=1)>0]
    df["Year"] = year
    return df

def strip_columns(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """
    drops all columns specified in the arguments.
    used to get only player name and position 
    """
    df = df.drop(cols, axis=1)
    return df

def combine_df(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    """
    returns concatenated df with all duplicates dropped
    this allows only one copy of a player to show up.
    EX: if there are two "lamar jackson's" they will show up as 2 different people,
    as long as one column is different. this allows for same name players to both exist 
    """
    df = pd.concat(dfs, axis=0)
    df = df.drop_duplicates()
    return df