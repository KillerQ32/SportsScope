import pandas as pd



def filter_df(df: pd.DataFrame, year: int)-> pd.DataFrame:
    df = df.copy()
    cols = ["Att","Yds","TD","Lng"]
    # changes all columns in col to numbers if that fails it changes it to NA
    # then any NA value is turned to 0. changes all numbers to make sure its an int rather than float
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)
    # checks rows across specified columns for any values 
    df = df[df[cols].sum(axis=1)>0]
    df["Year"] = year
    return df