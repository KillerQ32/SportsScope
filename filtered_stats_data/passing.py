from player_stats_2022.passing_stats_2022 import create_df_2022
from player_stats_2023.passing_stats_2023 import create_df_2023
from player_stats_2024.passing_stats_2024 import create_df_2024
from utils.filtering import filter_df
from utils.filtering import combine_df
from utils.filtering import get_names_only

def verify_player_stats():
    passing_2022_df = create_df_2022()
    passing_2023_df = create_df_2023()
    passing_2024_df = create_df_2024()

    cols = ["Cmp", "Att", "Yds", "TD", "Int"]
    
    pass_2022 = filter_df(passing_2022_df, 2022, cols)
    pass_2023 = filter_df(passing_2023_df, 2023, cols)
    pass_2024 = filter_df(passing_2024_df, 2024, cols)

    return pass_2022, pass_2023, pass_2024

def combine_all_player():
    pass_2022, pass_2023, pass_2024 = verify_player_stats()
    
    removed_cols = ["Age", "Team", "G", "GS", "QBrec",
                    "Cmp", "Att","QBR", "Sk", "Sk%", 
                    "NY/A", "ANY/A", "4QC", "GWD", 
                    "Awards", "Year", "Cmp%", "Yds",
                    "TD", "TD%", "Int", "Int%", "1D", "Succ%",
                    "Lng", "Y/A", "AY/A", "Y/C", "Y/G", "Rate"]
    
    pass_2022_names = get_names_only(pass_2022,removed_cols)
    pass_2023_names = get_names_only(pass_2023,removed_cols)
    pass_2024_names = get_names_only(pass_2024,removed_cols)
    
    combined_df = combine_df([pass_2022_names,pass_2023_names,pass_2024_names])
    
    return combined_df

passing_player_list = combine_all_player()