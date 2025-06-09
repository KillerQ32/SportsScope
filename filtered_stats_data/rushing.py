from player_stats_2022.rushing_stats_2022 import create_df_2022
from player_stats_2023.rushing_stats_2023 import create_df_2023
from player_stats_2024.rushing_stats_2024 import create_df_2024
from utils.filtering import filter_df
from utils.filtering import get_names_only
from utils.filtering import combine_df


rushing_data_2022 = create_df_2022()
rushing_data_2023 = create_df_2023()
rushing_data_2024 = create_df_2024()

verification_cols = ["Att","Yds","TD"]


rs_2022 = filter_df(rushing_data_2022, 2022, verification_cols)
rs_2023 = filter_df(rushing_data_2023, 2023, verification_cols)
rs_2024 = filter_df(rushing_data_2024, 2024, verification_cols)

rs_2022.head()
rs_2023.head()
rs_2024.head()

removed_cols = ["Succ%", "Y/A", "Y/G", "A/G", "Fmb", "Awards",
                "Team","G", "GS", "Att", "TD", "1D", "Lng", "Year",
                "Yds", "Age"]

rs_2022_names = get_names_only(rs_2022, removed_cols)
rs_2023_names = get_names_only(rs_2023, removed_cols)
rs_2024_names = get_names_only(rs_2024, removed_cols)

combined_df = combine_df([rs_2022_names,rs_2023_names,rs_2024_names])

print(combined_df)