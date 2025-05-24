import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.pro-football-reference.com/years/2022/receiving.htm"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Locate the receiving stats table
table = soup.find("table", id="receiving")

# Get the final header row (sometimes there are multiple <tr>s in <thead>)
header_row = table.find("thead").find_all("tr")[-1]
headers = [th.text.strip() for th in header_row.find_all("th")]

# Get all player rows in <tbody>
rows = table.find("tbody").find_all("tr")

receiving_stats_list = []

for row in rows:
    if row.get("class") == ["thead"]:
        continue  # Skip embedded header rows inside <tbody>

    cols = row.find_all(["th", "td"])
    values = [col.text.strip() for col in cols]

    # Skip rows that don’t match the number of headers
    if len(values) != len(headers):
        continue

    player_stats = dict(zip(headers, values))
    receiving_stats_list.append(player_stats)

# Convert to DataFrame
receiving_df = pd.DataFrame(receiving_stats_list)

# Preview first few rows
print(receiving_df)
