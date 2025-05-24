import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2023/punting.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Locate the punting stats table
table = soup.find("table", id="punting")

# Get the final header row (for column names)
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Collect player rows from tbody
rows = table.find("tbody").find_all("tr")
punting_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # skip mid-body headers

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    punting_stats_list.append(player_stats)

# Convert to DataFrame
punting_df = pd.DataFrame(punting_stats_list)

# Preview the result
print(punting_df)
