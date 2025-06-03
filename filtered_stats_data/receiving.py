import pandas as pd
from player_stats_2022.receiving_stats_2022 import create_df_2022
from player_stats_2023.receiving_stats_2023 import create_df_2023
from player_stats_2024.receiving_stats_2024 import create_df_2024


receiving_stats_2022 = create_df_2022()
receiving_stats_2023 = create_df_2023()
receiving_stats_2024 = create_df_2024()


def filter_df(df: pd.DataFrame, year: int)-> pd.DataFrame:
    df = df.copy()
    cols = ["Tgt","Rec","Yds","TD","Lng"]
    # changes all columns in col to numbers if that fails it changes it to NA
    # then any NA value is turned to 0. changes all numbers to make sure its an int rather than float
    df[cols] = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)
    # checks rows across specified columns for any values 
    df = df[df[cols].sum(axis=1)>0]
    df["Year"] = year
    return df

rec_2022 = filter_df(receiving_stats_2022, 2022)
rec_2023 = filter_df(receiving_stats_2023, 2023)
rec_2024 = filter_df(receiving_stats_2024, 2024)

print(rec_2022.head())
print(rec_2023.head())
print(rec_2024.head())