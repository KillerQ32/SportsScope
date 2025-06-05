import requests
from bs4 import BeautifulSoup
import pandas as pd


def create_df_2023():
    url = "https://www.pro-football-reference.com/years/2023/kicking.htm"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the kicking stats table
    table = soup.find("table", id="kicking")

    # Extract header row
    header_row = table.find("thead").find_all("tr")[-1]
    headers = [th.text.strip() for th in header_row.find_all("th")]

    # Get all player rows
    rows = table.find("tbody").find_all("tr")

    kicking_stats_list = []

    for row in rows:
        if row.get("class") == ["thead"]:
            continue  # skip embedded header rows

        cols = row.find_all(["th", "td"])
        values = [col.text.strip() for col in cols]

        if len(values) != len(headers):
            continue

        player_stats = dict(zip(headers, values))
        kicking_stats_list.append(player_stats)

    # Convert to DataFrame
    kicking_stats_df = pd.DataFrame(kicking_stats_list)
    kicking_stats_df.set_index("Rk",inplace=True)
    
    return kicking_stats_df

