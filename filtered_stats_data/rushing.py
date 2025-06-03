import pandas as pd
from player_stats_2022.rushing_stats_2022 import create_df_2022
from player_stats_2023.rushing_stats_2023 import create_df_2023
from player_stats_2024.rushing_stats_2024 import create_df_2024

rushing_data_2022 = create_df_2022()
rushing_data_2023 = create_df_2023()
rushing_data_2024 = create_df_2024()


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

rs_2022 = filter_df(rushing_data_2022, 2022)
rs_2023 = filter_df(rushing_data_2023, 2023)
rs_2024 = filter_df(rushing_data_2024, 2024)

print(rs_2022.head())
print(rs_2023.head())
print(rs_2024.head())

