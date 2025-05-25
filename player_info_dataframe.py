import requests
import pandas as pd

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerInfo"

querystring = {"playerName":"keenan_a","getStats":"true"}

headers = {
	"x-rapidapi-key": "ed5b5763f5msh60a32b281315712p165ec7jsne408d86bb9b9",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#print(response.json())
"""
Function retrieves player information and creates dataframe
"""
def get_player_info_dataframe():
    player_info = [] #declare player info list

    data = response.json() #refernce json request

    for player in data["body"]: #Looping body
        player_info_dict = {
            "espn_name": player.get("espnName"),
            "stats": player.get("stats"),
            "injury_status": player.get("injury"),
        }
        player_info.append(player_info_dict)

    df = pd.DataFrame(player_info)
    return df

def main():
    player_information_df = get_player_info_dataframe()
    print(player_information_df)

main()