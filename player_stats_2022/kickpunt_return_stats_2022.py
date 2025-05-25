import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2022/returns.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Locate the return stats table
table = soup.find("table", id="returns")

# Get column headers from the last <tr> in the <thead>
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Get all player rows in the body
rows = table.find("tbody").find_all("tr")
returns_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # skip mid-table headers

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    returns_stats_list.append(player_stats)

# Convert to DataFrame
returns_df = pd.DataFrame(returns_stats_list)

# Show preview
print(returns_df)
