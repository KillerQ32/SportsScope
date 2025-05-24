import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2022/scrimmage.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the scrimmage stats table
table = soup.find("table", id="scrimmage")

# Grab the actual header row
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Find all player rows in the table body
rows = table.find("tbody").find_all("tr")

scrimmage_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # Skip repeated headers inside tbody

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    scrimmage_stats_list.append(player_stats)

# Convert to DataFrame
scrimmage_df = pd.DataFrame(scrimmage_stats_list)

# Preview top rows
print(scrimmage_df)
