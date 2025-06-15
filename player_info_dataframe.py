import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

X_API_BASE_URL = os.getenv("X_API_BASE_URL")
X_API_KEY = os.getenv("X_API_KEY")
X_API_HOST = os.getenv("X_API_HOST")

url = f"{X_API_BASE_URL}/getNFLPlayerInfo"

querystring = {"playerName":"keenan_a","getStats":"true"}

headers = {
	"x-rapidapi-key": X_API_KEY,
	"x-rapidapi-host": X_API_HOST
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