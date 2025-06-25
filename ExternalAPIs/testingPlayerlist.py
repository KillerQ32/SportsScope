import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

def get_player_list_data() -> dict:
    """
    Retrieve full NFL player list data from the API.

    Returns:
        dict: Raw JSON response from the API
    """
    url = f"{X_API_BASE_URL}/getNFLPlayerList"
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

def parse_player_list(json_data: dict) -> pd.DataFrame:
    """
    Parse player list JSON data into pandas DataFrame format.

    Args:
        json_data (dict): Raw JSON API response

    Returns:
        pd.DataFrame: Cleaned player list dataframe
    """
    player_list = []

    for player in json_data.get("body", []):
        player_info = {
            "player_name": player.get("longName"),
            "espn_name": player.get("espnName"),
            "team": player.get("team"),
            "jersey_number": player.get("jerseyNum"),
            "age": player.get("age"),
            "weight": player.get("weight"),
            "height": player.get("height"),
            "position": player.get("pos"),
            "college": player.get("school"),
            "team_ID": player.get("teamID"),
            "player_ID": player.get("playerID"),
            "espn_ID": player.get("espnID"),
            "headshot": player.get("espnHeadshot"),
            "free_agent_status": player.get("isFreeAgent")
        }
        player_list.append(player_info)

    return pd.DataFrame(player_list)

def get_player_list_dataframe() -> pd.DataFrame:
    """
    Full pipeline to retrieve and convert player list data into DataFrame.

    Returns:
        pd.DataFrame: Player list dataframe
    """
    raw_data = get_player_list_data()
    if not raw_data:
        return pd.DataFrame()
    return parse_player_list(raw_data)

def main():
    """
    Example usage for testing player list retrieval.
    """
    df = get_player_list_dataframe()
    print(df)

if __name__ == "__main__":
    main()
