import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

url = f"{X_API_BASE_URL}/getNFLDepthCharts"

headers = {
	"x-rapidapi-key": X_API_KEY,
	"x-rapidapi-host": X_API_HOST
}

response = requests.get(url, headers=headers)

#print(response.json())



#def create_dictionary(name: str, dict: dict, keyname: str):
#   for key in dict:
#        if key == keyname:
#            dict[key][name] = {}
#
#def add_to_dictionary(name: str, dict_obj: dict, keyname: str):
    

def get_depth_chart():
    depth_list = []

    data = response.json()

    for team in data["body"]:
        team_abv = team.get("teamAbv")
        team_id = team.get("teamID")
        depth_chart = team.get("depthChart", {})

        for position_group, players in depth_chart.items():
            for player in players:
                depth_list.append({
                    "team_abv": team_abv,
                    "team_id": team_id,
                    "position_group": position_group,
                    "depth_position": player.get("depthPosition"),
                    "player_id": player.get("playerID"),
                    "player_name": player.get("longName")
                })
    df = pd.DataFrame(depth_list)
    print(df)
    return pd.DataFrame(depth_list)

df = get_depth_chart()