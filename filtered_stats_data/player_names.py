from utils.filtering import combine_df
from rushing import rush_player_list
from receiving import rec_player_list
from passing import passing_player_list
from kicking import kicking_player_list


def create_player_list():
    df = combine_df([rush_player_list,rec_player_list,passing_player_list,kicking_player_list])
    return df
