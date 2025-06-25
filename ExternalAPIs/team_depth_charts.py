import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

def get_depth_chart_data() -> dict:
    """
    Retrieve full NFL depth chart data from the API.

    Returns:
        dict: Raw JSON response from the API
    """
    url = f"{X_API_BASE_URL}/getNFLDepthCharts"
    headers = {
        "x-rapidapi-key": X_API_KEY,
        "x-rapidapi-host": X_API_HOST
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return {}
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}

def parse_depth_chart(json_data: dict) -> pd.DataFrame:
    """
    Parse JSON depth chart data into pandas DataFrame format.

    Args:
        json_data (dict): Raw JSON API response

    Returns:
        pd.DataFrame: Cleaned depth chart dataframe
    """
    depth_list = []

    for team in json_data.get("body", []):
        team_abv = team.get("teamAbv")
        team_id = team.get("teamID")
        depth_chart = team.get("depthChart", {})

        for position_group, players in depth_chart.items():
            for player in players:
                try:
                    depth_list.append({
                        "team_abv": team_abv,
                        "team_id": team_id,
                        "position_group": position_group,
                        "depth_position": player.get("depthPosition"),
                        "player_id": player.get("playerID"),
                        "player_name": player.get("longName")
                    })
                except Exception as e:
                    print(f"Error parsing player data: {e}")

    return pd.DataFrame(depth_list)

def get_depth_chart_dataframe() -> pd.DataFrame:
    """
    Full pipeline to retrieve and convert depth chart data into DataFrame.

    Returns:
        pd.DataFrame: Depth chart dataframe
    """
    raw_data = get_depth_chart_data()
    if not raw_data:
        return pd.DataFrame()
    return parse_depth_chart(raw_data)

def main():
    """
    Example usage for testing depth chart retrieval.
    """
    df = get_depth_chart_dataframe()
    print(df)

if __name__ == "__main__":
    main()
