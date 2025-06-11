from utils.filtering import combine_df
from rushing import rush_player_list
from receiving import rec_player_list
from passing import passing_player_list



combine_df([rush_player_list, passing_player_list, rec_player_list])
print(rush_player_list)
print(rec_player_list)
print(passing_player_list)

    