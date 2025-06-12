from player_stats_2022.kicking_stats_2022 import create_df_2022
from player_stats_2023.kicking_stats_2023 import create_df_2023
from player_stats_2024.kicking_stats_2024 import create_df_2024
from utils.filtering import filter_df
from utils.filtering import combine_df
from utils.filtering import strip_columns

def verify_player_stats():
    kicking_stats_2022 = create_df_2022()
    kicking_stats_2023 = create_df_2023()
    kicking_stats_2024 = create_df_2024()

    verification_cols = ["FGA", "FGM", "XPA", "XPM"]
    
    kicking_2022 = filter_df(kicking_stats_2022, 2022, verification_cols)
    kicking_2023 = filter_df(kicking_stats_2023, 2023, verification_cols)
    kicking_2024 = filter_df(kicking_stats_2024, 2024, verification_cols)
    
    return kicking_2022, kicking_2023, kicking_2024

def get_player_names():
    kicking_2022, kicking_2023, kicking_2024 = verify_player_stats()
    
    removed_cols = ["Age", "Team", "G", "GS", "FGA", "FGM", "Lng",
                    "FG%", "XPA", "XPM" ,"XP%", "KO", "KOYds", "TB", "TB%",
                    "KOAvg", "Awards", "Year"]
    
    kicking_2022_names = strip_columns(kicking_2022,removed_cols)
    kicking_2023_names = strip_columns(kicking_2023,removed_cols)
    kicking_2024_names = strip_columns(kicking_2024,removed_cols)
    
    combined_df = combine_df([kicking_2022_names,kicking_2023_names,kicking_2024_names])
    
    return combined_df

kicking_player_list = get_player_names()

def get_player_stats():
    kicking_2022, kicking_2023, kicking_2024 = verify_player_stats()
    
    removed_cols = ["Age", "GS", "FG%","XP%", "KO",
                    "KOYds", "TB", "TB%", "Pos",
                    "KOAvg", "Awards",]
    
    kicking_2022_names = strip_columns(kicking_2022,removed_cols)
    kicking_2023_names = strip_columns(kicking_2023,removed_cols)
    kicking_2024_names = strip_columns(kicking_2024,removed_cols)
    
    combined_df = combine_df([kicking_2022_names,kicking_2023_names,kicking_2024_names])
    
    return combined_df

kicking_player_stats = get_player_stats()