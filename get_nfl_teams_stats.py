import requests
import pandas as pd

def get_nfl_single_player_team_stats_dataframe(year="2024") -> pd.DataFrame:
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeams"
    querystring = {
        "sortBy": "standings",
        "rosters": "false",
        "schedules": "false",
        "topPerformers": "true",
        "teamStats": "true",
        "teamStatsSeason": year
    }

    headers = {
        "x-rapidapi-key": "e4d9ccd164msh48d5a320d67f4e5p149cccjsn86edee235fb3",
        "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    teams = data["body"]

    all_teams_data = []

    for team in teams:
        team_data = {
            "teamAbv": team["teamAbv"],
            "teamName": team["teamName"],
            "division": team["division"],
            "conference": team["conferenceAbv"],
            "byeWeek": team["byeWeeks"][year],
            "wins": team["wins"],

            # Top Performers - Rushing
            "rushYds": team["topPerformers"]["Rushing"]["rushYds"]["total"],
            "rushYdsPlayer": team["topPerformers"]["Rushing"]["rushYds"]["playerID"][0],
            "rushCarries": team["topPerformers"]["Rushing"]["carries"]["total"],
            "rushCarriesPlayer": team["topPerformers"]["Rushing"]["carries"]["playerID"][0],
            "rushTDs": team["topPerformers"]["Rushing"]["rushTD"]["total"],
            "rushTDsPlayer": team["topPerformers"]["Rushing"]["rushTD"]["playerID"][0],

            # Top Performers - Passing
            "passYds": team["topPerformers"]["Passing"]["passYds"]["total"],
            "passYdsPlayer": team["topPerformers"]["Passing"]["passYds"]["playerID"][0],
            "passTDs": team["topPerformers"]["Passing"]["passTD"]["total"],
            "passTDsPlayer": team["topPerformers"]["Passing"]["passTD"]["playerID"][0],

            # Defense
            "totalTackles": team["topPerformers"]["Defense"]["totalTackles"]["total"],
            "tacklesPlayer": team["topPerformers"]["Defense"]["totalTackles"]["playerID"][0],
            "sacks": team["topPerformers"]["Defense"]["sacks"]["total"],
            "sacksPlayer": team["topPerformers"]["Defense"]["sacks"]["playerID"][0],
            "interceptions": team["topPerformers"]["Defense"]["defensiveInterceptions"]["total"],
            "interceptionsPlayers": team["topPerformers"]["Defense"]["defensiveInterceptions"]["playerID"][0],

            # Receiving
            "recYds": team["topPerformers"]["Receiving"]["recYds"]["total"],
            "recYdsPlayer": team["topPerformers"]["Receiving"]["recYds"]["playerID"][0],
            "recTDs": team["topPerformers"]["Receiving"]["recTD"]["total"],
            "recTDsPlayer": team["topPerformers"]["Receiving"]["recTD"]["playerID"][0]
        }

        all_teams_data.append(team_data)

    return pd.DataFrame(all_teams_data)




def get_total_nfl_team_stats_dataframe(year="2024") -> pd.DataFrame:
    url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLTeams"
    querystring = {
        "sortBy": "standings",
        "rosters": "false",
        "schedules": "false",
        "topPerformers": "false",
        "teamStats": "true",
        "teamStatsSeason": year
    }

    headers = {
        "x-rapidapi-key": "e4d9ccd164msh48d5a320d67f4e5p149cccjsn86edee235fb3",
        "x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    teams = data["body"]

    all_stats = []

    for team in teams:
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

test = get_nfl_single_player_team_stats_dataframe()
test.to_csv("test",index=False)

test2 = get_total_nfl_team_stats_dataframe()
test2.to_csv("test2",index=False)


test.shape
test2.shape

# testing the shape of the df and putting it in csv to look at it better
