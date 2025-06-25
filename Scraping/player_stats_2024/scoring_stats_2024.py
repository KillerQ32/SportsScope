import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2024/scoring.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Locate the scoring stats table
table = soup.find("table", id="scoring")

# Get header labels
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Iterate through all data rows
rows = table.find("tbody").find_all("tr")
scoring_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # skip embedded headers in tbody

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    scoring_stats_list.append(player_stats)

# Convert to DataFrame
scoring_df = pd.DataFrame(scoring_stats_list)

# Preview top rows
print(scoring_df)
