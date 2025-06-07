from player_stats_2022.passing_stats_2022 import create_df_2022
from player_stats_2023.passing_stats_2023 import create_df_2023
from player_stats_2024.passing_stats_2024 import create_df_2024
from utils.filtering import filter_df


passing_2022_df = create_df_2022()
passing_2023_df = create_df_2023()
passing_2024_df = create_df_2024()

passing_2022_df.head()
passing_2023_df.head()
passing_2024_df.head()

cols = ["Cmp", "Att", "Yds", "TD", "Int"]
#might and remove attempts as a filter 

pass_2022 = filter_df(passing_2022_df, 2022, cols)
pass_2023 = filter_df(passing_2023_df, 2023, cols)
pass_2024 = filter_df(passing_2024_df, 2024, cols)

pass_2022.head()
pass_2023.head()
pass_2024.head()