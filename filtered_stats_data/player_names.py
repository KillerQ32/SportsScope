from utils.filtering import combine_df
from filtered_stats_data.rushing import rush_player_list
from filtered_stats_data.receiving import rec_player_list
from filtered_stats_data.passing import passing_player_list
from filtered_stats_data.kicking import kicking_player_list


def create_player_list():
    df = combine_df([rush_player_list,rec_player_list,passing_player_list,kicking_player_list])
    return df

player_names = create_player_list()