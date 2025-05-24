import requests
import pandas as pd


def get_team_schedule(team: str, year: str) -> pd.DataFrame:

    """
    access api to get team schedule for a given year.
    Uses helper function to parse json before get_team_schedule puts it in a dataframe
    
    args: 
        team (str): abreviated team name. ex: Ravens to BAL
        year (str): specify season by the year. ex: 2025 is 2024-2025 szn
    
    returns:
        pandas DataFrame object. 
    """
    
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

    querystring = {"teamAbv":team,"season":year}

    headers = {
        "x-rapidapi-key": "e4d9ccd164msh48d5a320d67f4e5p149cccjsn86edee235fb3",
        "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
        }
    try:
        response = requests.get(url,headers=headers,params=querystring)
        data = response.json()

        if "body" not in data or "schedule" not in data["body"]:
            raise ValueError("Missing expected keys in API response.")

        # parse through json data to grab seasonType, gameTime, and gameWeek
        def parse_game_schedule():
            game_data = []

            for item in data["body"]["schedule"]:
                game_dict = {"season_type": item["seasonType"],
                        "game_time": item["gameTime"],
                        "game_week": item["gameWeek"]}
                game_data.append(game_dict)
            return game_data

        # takes the parsed dictionary and throws it into a dataframe
        # returns a dataframe containing data from dictionary 
        game_data = parse_game_schedule()
        team_schedule_df = pd.DataFrame(game_data)
        return team_schedule_df
    
    
    except requests.RequestException as e:
        raise ConnectionError(f"Request failed: {e}")
    
    except ValueError as e:
        raise ValueError(f"Data format error: {e}")
    
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")


def league_schedule_df_creator():
    """
    creates dataframes for the whole leagues schedules 
    
    args: NONE
    
    returns: a dictonary full of dataframes with 
    the key being the name of the team 
    """

    teams = ["ARI", "ATL", "BAL", "BUF","CAR", 
             "CHI", "CIN", "CLE",
             "DAL", "DEN", "DET",
             "GB", "HOU", "IND", 
             "JAX","KC", "MIA",
             "MIN", "NE", "NO", 
             "NYG", "NYJ", "LV",
             "PHI","PIT", "LAC", 
             "SF","SEA", "LAR", 
             "TB", "TEN", "WSH"]

    game_schedule = {}

    for team in teams:
        try:
            game_schedule[team] = get_team_schedule(team=team, year="2025")
        except Exception as e:
            print(f"Error retrieving schedule for team {team}: {e}")
    return game_schedule
        
if __name__ == "__main__":
    test = league_schedule_df_creator()

