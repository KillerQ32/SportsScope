from player_stats_2022.kicking_stats_2022 import create_df_2022
from player_stats_2023.kicking_stats_2023 import create_df_2023
from player_stats_2024.kicking_stats_2024 import create_df_2024
from utils.filtering import filter_df


kicking_stats_2022 = create_df_2022()
kicking_stats_2023 = create_df_2023()
kicking_stats_2024 = create_df_2024()

kicking_stats_2022.head()
kicking_stats_2023.head()
kicking_stats_2024.head()

cols = ["FGA", "FGM", "XPA", "XPM"]

kicking_2022 = filter_df(kicking_stats_2022, 2022, cols)
kicking_2023 = filter_df(kicking_stats_2023, 2023, cols)
kicking_2024 = filter_df(kicking_stats_2024, 2024, cols)


kicking_2022.head()
kicking_2023.head()
kicking_2024.head()