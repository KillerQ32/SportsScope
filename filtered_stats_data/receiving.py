from player_stats_2022.receiving_stats_2022 import create_df_2022
from player_stats_2023.receiving_stats_2023 import create_df_2023
from player_stats_2024.receiving_stats_2024 import create_df_2024
from utils.filtering import filter_df


receiving_stats_2022 = create_df_2022()
receiving_stats_2023 = create_df_2023()
receiving_stats_2024 = create_df_2024()

cols = ["Tgt","Rec","Yds","TD"]


rec_2022 = filter_df(receiving_stats_2022, 2022, cols)
rec_2023 = filter_df(receiving_stats_2023, 2023, cols)
rec_2024 = filter_df(receiving_stats_2024, 2024, cols)

print(rec_2022.head())
print(rec_2023.head())
print(rec_2024.head())