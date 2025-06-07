from player_stats_2022.rushing_stats_2022 import create_df_2022
from player_stats_2023.rushing_stats_2023 import create_df_2023
from player_stats_2024.rushing_stats_2024 import create_df_2024
from utils.filtering import filter_df


rushing_data_2022 = create_df_2022()
rushing_data_2023 = create_df_2023()
rushing_data_2024 = create_df_2024()

cols = ["Att","Yds","TD"]


rs_2022 = filter_df(rushing_data_2022, 2022, cols)
rs_2023 = filter_df(rushing_data_2023, 2023, cols)
rs_2024 = filter_df(rushing_data_2024, 2024, cols)

rs_2022.head()
rs_2023.head()
rs_2024.head()