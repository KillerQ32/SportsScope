import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

def get_player_info(player_name: str) -> dict:
    """
    Retrieve player info from the API based on player name.

    Args:
        player_name (str): Player name formatted for the API query

    Returns:
        dict: Raw JSON response from the API
    """
    url = f"{X_API_BASE_URL}/getNFLPlayerInfo"
    querystring = {"playerName": player_name, "getStats": "true"}
    headers = {
        "x-rapidapi-key": X_API_KEY,
        "x-rapidapi-host": X_API_HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

def parse_player_info(json_data: dict) -> pd.DataFrame:
    """
    Parse player info JSON response into pandas DataFrame.

    Args:
        json_data (dict): Raw JSON API response

    Returns:
        pd.DataFrame: DataFrame containing player info
    """
    player_info = []

    for player in json_data.get("body", []):
        player_info_dict = {
            "espn_name": player.get("espnName"),
            "stats": player.get("stats"),
            "injury_status": player.get("injury"),
        }
        player_info.append(player_info_dict)

    return pd.DataFrame(player_info)

def get_player_info_dataframe(player_name: str) -> pd.DataFrame:
    """
    Full pipeline to retrieve and convert player info into DataFrame.

    Args:
        player_name (str): Player name for lookup

    Returns:
        pd.DataFrame: Player information as DataFrame
    """
    raw_data = get_player_info(player_name)
    return parse_player_info(raw_data)

def main():
    """
    Example usage for testing with Keenan Allen.
    """
    player_information_df = get_player_info_dataframe("keenan_a")
    print(player_information_df)

if __name__ == "__main__":
    main()