import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2024/defense.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the defense stats table
table = soup.find("table", id="defense")

# Get headers from the last header row in the thead
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Extract all player rows
rows = table.find("tbody").find_all("tr")

defense_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # skip mid-table header rows

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    defense_stats_list.append(player_stats)

# Convert to DataFrame
defense_df = pd.DataFrame(defense_stats_list)

# Preview top rows
print(defense_df)
