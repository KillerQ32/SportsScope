from Scraping.player_stats_2022.receiving_stats_2022 import create_df_2022
from Scraping.player_stats_2023.receiving_stats_2023 import create_df_2023
from Scraping.player_stats_2024.receiving_stats_2024 import create_df_2024
from utils.filtering import filter_df
from utils.filtering import strip_columns
from utils.filtering import combine_df
import pandas as pd

def verify_player_stats():
    receiving_stats_2022 = create_df_2022()
    receiving_stats_2023 = create_df_2023()
    receiving_stats_2024 = create_df_2024()

    verification_cols = ["Tgt","Rec","Yds","TD"]

    rec_2022 = filter_df(receiving_stats_2022, 2022, verification_cols)
    rec_2023 = filter_df(receiving_stats_2023, 2023, verification_cols)
    rec_2024 = filter_df(receiving_stats_2024, 2024, verification_cols)
    
    return rec_2022, rec_2023, rec_2024

def get_player_names():
    rec_2022, rec_2023, rec_2024 = verify_player_stats()
    
    removed_cols = ["Succ%", "Y/R", "Y/G", "R/G", "Fmb", "Awards",
                    "Team","G", "GS", "Tgt", "TD", "1D", "Lng", "Year",
                    "Yds", "Age", "Y/Tgt", "Ctch%", "Rec"]
    
    rec_2022_names = strip_columns(rec_2022,removed_cols)
    rec_2023_names = strip_columns(rec_2023,removed_cols)
    rec_2024_names = strip_columns(rec_2024,removed_cols)
    
    combined_df = combine_df([rec_2022_names, rec_2023_names, rec_2024_names])
    
    return combined_df

rec_player_list = get_player_names()

def get_player_stats():
    rec_2022, rec_2023, rec_2024 = verify_player_stats()
    
    removed_cols = ["Succ%", "Y/R", "Y/G", "R/G", "Fmb", "Awards",
                    "GS", "1D", "Pos", "Age", "Y/Tgt", "Ctch%"]
    
    rec_2022_names = strip_columns(rec_2022,removed_cols)
    rec_2023_names = strip_columns(rec_2023,removed_cols)
    rec_2024_names = strip_columns(rec_2024,removed_cols)
    
    combined_df = combine_df([rec_2022_names, rec_2023_names, rec_2024_names])
    combined_df = combined_df.copy()
    combined_df[["Lng", "G"]] = combined_df[["Lng", "G"]].apply(pd.to_numeric, errors="coerce").fillna(0).astype(int)

    return combined_df

rec_player_stats = get_player_stats()