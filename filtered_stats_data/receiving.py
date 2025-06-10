from player_stats_2022.receiving_stats_2022 import create_df_2022
from player_stats_2023.receiving_stats_2023 import create_df_2023
from player_stats_2024.receiving_stats_2024 import create_df_2024
from utils.filtering import filter_df
from utils.filtering import get_names_only
from utils.filtering import combine_df

def verify_player_stats():
    receiving_stats_2022 = create_df_2022()
    receiving_stats_2023 = create_df_2023()
    receiving_stats_2024 = create_df_2024()

    cols = ["Tgt","Rec","Yds","TD"]

    rec_2022 = filter_df(receiving_stats_2022, 2022, cols)
    rec_2023 = filter_df(receiving_stats_2023, 2023, cols)
    rec_2024 = filter_df(receiving_stats_2024, 2024, cols)
    
    return rec_2022, rec_2023, rec_2024

def combine_all_players():
    rec_2022, rec_2023, rec_2024 = verify_player_stats()
    
    removed_cols = ["Succ%", "Y/R", "Y/G", "R/G", "Fmb", "Awards",
                    "Team","G", "GS", "Tgt", "TD", "1D", "Lng", "Year",
                    "Yds", "Age", "Y/Tgt", "Ctch%", "Rec"]
    
    rec_2022_names = get_names_only(rec_2022,removed_cols)
    rec_2023_names = get_names_only(rec_2023,removed_cols)
    rec_2024_names = get_names_only(rec_2024,removed_cols)
    
    combined_df = combine_df([rec_2022_names, rec_2023_names, rec_2024_names])
    
    return combined_df

rec_player_list = combine_all_players() 