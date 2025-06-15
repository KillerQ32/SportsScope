import requests
from bs4 import BeautifulSoup
import pandas as pd

weeks = [f"https://www.pro-football-reference.com/years/2024/week_{i}.htm" for i in range(1, 19)]
headers = {"User-Agent": "Mozilla/5.0"}

games_list = []

for week_num, url in enumerate(weeks, start=1):
    print(f"Scraping Week {week_num}...")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all divs that hold box scores
    games = soup.find_all("div", class_="game_summary")

    for game in games:
        try:
            # Date
            date_div = game.find_previous("div", class_="section_heading")
            game_date = date_div.find("h2").text.strip() if date_div else f"Week {week_num}"

            # Team names and scores
            teams = game.find_all("tr")
            team_1 = teams[1].find("td").text.strip()
            score_1 = teams[1].find_all("td")[-1].text.strip()

            team_2 = teams[2].find("td").text.strip()
            score_2 = teams[2].find_all("td")[-1].text.strip()

            game_data = {
                "week": week_num,
                "date": game_date,
                "away_team": team_1,
                "away_pts": score_1,
                "home_team": team_2,
                "home_pts": score_2
            }

            games_list.append(game_data)

        except Exception as e:
            print(f"Error parsing game in week {week_num}: {e}")
            continue

# Convert to DataFrame
games_df = pd.DataFrame(games_list)

# Clean up numeric scores
games_df["away_pts"] = pd.to_numeric(games_df["away_pts"], errors="coerce")
games_df["home_pts"] = pd.to_numeric(games_df["home_pts"], errors="coerce")

# Preview
print(games_df.columns)
