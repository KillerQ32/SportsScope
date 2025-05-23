import requests
import pandas as pd


# url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeamSchedule"

# querystring = {"teamAbv":"PHI","season":"2025"}

# headers = {
# 	"x-rapidapi-key": "e4d9ccd164msh48d5a320d67f4e5p149cccjsn86edee235fb3",
# 	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# response.json()["body"]["schedule"][0]

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

    querystring = {f"teamAbv":team,"season":year}

    headers = {
	"x-rapidapi-key": "e4d9ccd164msh48d5a320d67f4e5p149cccjsn86edee235fb3",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url,headers=headers,params=querystring)
    data = response.json()


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



new_england_games = get_team_schedule("NE","2025")
steelers_games = get_team_schedule("PIT","2025")


def leauge_schedule_df_creator():

    teams = ["PHI","BAL","CIN","BUF" ]

    game_schedule = {}

    for team in teams:
        game_schedule[team] = get_team_schedule(team=team, year="2025")

