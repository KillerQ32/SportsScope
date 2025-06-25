from ExternalAPIs.get_nfl_teams_stats import get_nfl_single_player_team_stats_dataframe
import pandas as pd

def extract_team_metadata_df() -> pd.DataFrame:
    df = get_nfl_single_player_team_stats_dataframe()
    return df[["teamAbv", "division", "conference"]].drop_duplicates()

team_headers = extract_team_metadata_df()
if team_headers.empty:
    print("No data returned — check API or environment variables.")
else:
    print(team_headers)

