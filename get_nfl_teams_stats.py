import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

def get_nfl_single_player_team_stats_dataframe(year="2024") -> pd.DataFrame:
    """ 
    Pull NFL team stats with top performers data from the API.
    This includes team level data and individual top performing player IDs.

    Args:
        year (str): season year (default is "2024")

    Returns:
        pd.DataFrame: dataframe of team stats with top performers
    """
    url = f"{X_API_BASE_URL}/getNFLTeams"
    querystring = {
        "sortBy": "standings",
        "rosters": "false",
        "schedules": "false",
        "topPerformers": "true",
        "teamStats": "true",
        "teamStatsSeason": year
    }
    headers = {
        "x-rapidapi-key": X_API_KEY,
        "x-rapidapi-host": X_API_HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()["body"]
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return pd.DataFrame()
    except (KeyError, ValueError) as e:
        print(f"Error parsing JSON response: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()

    all_teams_data = []

    for team in data:
        team_data = {
            "teamAbv": team["teamAbv"],
            "teamName": team["teamName"],
            "division": team["division"],
            "conference": team["conferenceAbv"],
            "byeWeek": team["byeWeeks"][year],
            "wins": team["wins"],
            
            # Rushing leaders
            "rushYds": team["topPerformers"]["Rushing"]["rushYds"]["total"],
            "rushYdsPlayer": team["topPerformers"]["Rushing"]["rushYds"]["playerID"][0],
            "rushCarries": team["topPerformers"]["Rushing"]["carries"]["total"],
            "rushCarriesPlayer": team["topPerformers"]["Rushing"]["carries"]["playerID"][0],
            "rushTDs": team["topPerformers"]["Rushing"]["rushTD"]["total"],
            "rushTDsPlayer": team["topPerformers"]["Rushing"]["rushTD"]["playerID"][0],

            # Passing leaders
            "passYds": team["topPerformers"]["Passing"]["passYds"]["total"],
            "passYdsPlayer": team["topPerformers"]["Passing"]["passYds"]["playerID"][0],
            "passTDs": team["topPerformers"]["Passing"]["passTD"]["total"],
            "passTDsPlayer": team["topPerformers"]["Passing"]["passTD"]["playerID"][0],

            # Defense leaders
            "totalTackles": team["topPerformers"]["Defense"]["totalTackles"]["total"],
            "tacklesPlayer": team["topPerformers"]["Defense"]["totalTackles"]["playerID"][0],
            "sacks": team["topPerformers"]["Defense"]["sacks"]["total"],
            "sacksPlayer": team["topPerformers"]["Defense"]["sacks"]["playerID"][0],
            "interceptions": team["topPerformers"]["Defense"]["defensiveInterceptions"]["total"],
            "interceptionsPlayers": team["topPerformers"]["Defense"]["defensiveInterceptions"]["playerID"][0],

            # Receiving leaders
            "recYds": team["topPerformers"]["Receiving"]["recYds"]["total"],
            "recYdsPlayer": team["topPerformers"]["Receiving"]["recYds"]["playerID"][0],
            "recTDs": team["topPerformers"]["Receiving"]["recTD"]["total"],
            "recTDsPlayer": team["topPerformers"]["Receiving"]["recTD"]["playerID"][0]
        }
        all_teams_data.append(team_data)

    return pd.DataFrame(all_teams_data)

def get_total_nfl_team_stats_dataframe(year="2024") -> pd.DataFrame:
    """
    Pull full NFL team stats (excluding top performers) from the API.
    This includes full team stats across all categories (rushing, passing, defense, special teams).

    Args:
        year (str): season year (default is "2024")

    Returns:
        pd.DataFrame: dataframe of full team stats
    """
    url = f"{X_API_BASE_URL}/getNFLTeams"
    querystring = {
        "sortBy": "standings",
        "rosters": "false",
        "schedules": "false",
        "topPerformers": "false",
        "teamStats": "true",
        "teamStatsSeason": year
    }
    headers = {
        "x-rapidapi-key": X_API_KEY,
        "x-rapidapi-host": X_API_HOST
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()["body"]
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return pd.DataFrame()
    except (KeyError, ValueError) as e:
        print(f"Error parsing JSON response: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error: {e}")
        return pd.DataFrame()

    all_stats = []

    for team in data:
        ts = team["teamStats"]

        team_stats = {
            "teamAbv": team["teamAbv"],
            "teamName": team["teamName"],
            
            # Rushing
            "rushYds": ts["Rushing"]["rushYds"],
            "rushCarries": ts["Rushing"]["carries"],
            "rushTDs": ts["Rushing"]["rushTD"],
            
            # Kicking
            "fgAttempts": ts["Kicking"]["fgAttempts"],
            "fgMade": ts["Kicking"]["fgMade"],
            "xpMade": ts["Kicking"]["xpMade"],
            "fgYds": ts["Kicking"]["fgYds"],
            "kickYards": ts["Kicking"]["kickYards"],
            "xpAttempts": ts["Kicking"]["xpAttempts"],
            
            # Passing
            "passAttempts": ts["Passing"]["passAttempts"],
            "passTDs": ts["Passing"]["passTD"],
            "passYds": ts["Passing"]["passYds"],
            "interceptions": ts["Passing"]["int"],
            "passCompletions": ts["Passing"]["passCompletions"],
            
            # Punting
            "puntYds": ts["Punting"]["puntYds"],
            "punts": ts["Punting"]["punts"],
            "puntsIn20": ts["Punting"]["puntsin20"],
            "puntTouchbacks": ts["Punting"]["puntTouchBacks"],
            
            # Receiving
            "receptions": ts["Receiving"]["receptions"],
            "recTDs": ts["Receiving"]["recTD"],
            "targets": ts["Receiving"]["targets"],
            "recYds": ts["Receiving"]["recYds"],
            
            # Defense
            "fumblesLost": ts["Defense"]["fumblesLost"],
            "defTDs": ts["Defense"]["defTD"],
            "fumbles": ts["Defense"]["fumbles"],
            "fumblesRecovered": ts["Defense"]["fumblesRecovered"],
            "soloTackles": ts["Defense"]["soloTackles"],
            "qbHits": ts["Defense"]["qbHits"],
            "passingTDsAllowed": ts["Defense"]["passingTDAllowed"],
            "passDeflections": ts["Defense"]["passDeflections"],
            "passingYdsAllowed": ts["Defense"]["passingYardsAllowed"],
            "totalTackles": ts["Defense"]["totalTackles"],
            "defInterceptions": ts["Defense"]["defensiveInterceptions"],
            "tfl": ts["Defense"]["tfl"],
            "rushingYdsAllowed": ts["Defense"]["rushingYardsAllowed"],
            "sacks": ts["Defense"]["sacks"],
            "rushingTDsAllowed": ts["Defense"]["rushingTDAllowed"]
        }
        all_stats.append(team_stats)

    return pd.DataFrame(all_stats)

def main():
    """
    Example usage for quick testing and demonstration.
    """
    player_stats_df = get_nfl_single_player_team_stats_dataframe()
    total_stats_df = get_total_nfl_team_stats_dataframe()
    
    print(player_stats_df.head())
    print(total_stats_df.head())

if __name__ == "__main__":
    main()
