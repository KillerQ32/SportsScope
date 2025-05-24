import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2022/passing.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Get table and headers
table = soup.find("table", id="passing")
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Find all table rows inside tbody
rows = table.find("tbody").find_all("tr")

qb_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # skip duplicate header rows

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    # Skip rows that don’t match the header length
    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    qb_stats_list.append(player_stats)

# Print 3 examples
##    print(qb)
#    print("-" * 40)

qb_stats_2024_df = pd.DataFrame(qb_stats_list)
print(qb_stats_2024_df)