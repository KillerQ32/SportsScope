import requests
import pandas as pd

url = "https://tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com/getNFLPlayerList"

headers = {
	"x-rapidapi-key": "ed5b5763f5msh60a32b281315712p165ec7jsne408d86bb9b9",
	"x-rapidapi-host": "tank01-nfl-live-in-game-real-time-statistics-nfl.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

#print(response.json())

def create_player_list_dataframe():
    data = response.json()
    player_list = []
    
    for player in data["body"]:
        player_info = {
            "player_name": player.get("longName"),
            "espn_name": player.get("espnName"),
            "team": player.get("team"),
            "jersey_number": player.get("jerseyNum"),
            "age": player.get("age"),  # Safe access
            "weight": player.get("weight"),
            "height": player.get("height"),
            "position": player.get("pos"),
            "College": player.get("school"),
            "team_ID": player.get("teamID"),
            "player_ID": player.get("playerID"),
            "espn_ID": player.get("espnID"),
            "headshot":player.get("espnHeadshot"),
            "free_agent_status": player.get("isFreeAgent")
        }
        player_list.append(player_info)
    
    df = pd.DataFrame(player_list)
    return df


def main():
    print("Testing DataFrame Creation")

    player_list_dataframe = create_player_list_dataframe()
    print(player_list_dataframe)

main()

