from db.engine import engine
from sqlalchemy import text
from filtered_stats_data.player_names import player_names
from filtered_stats_data.teams import team_headers
from filtered_stats_data.rushing import rush_player_stats
from filtered_stats_data.passing import passing_player_stats
from filtered_stats_data.receiving import rec_player_stats
from filtered_stats_data.kicking import kicking_player_stats


def insert_into_players_table(df):
    insert_query = text("""
                        INSERT INTO players (player_name, position)
                        VALUES(:Player, :Pos)
                        ON CONFLICT (player_name) DO NOTHING;
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()


def insert_into_teams_table(df):
    insert_query = text("""
                        INSERT INTO teams (team_name, division, conference)
                        VALUES(:teamAbv, :division, :conference)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()


def insert_into_rushing_table(df):
    insert_query = text("""
                        INSERT INTO rushing_stats (season_year, rush_attempts, rush_yards, rush_tds, longest_rush, games_played, team_name, player_name)
                        VALUES(:Year, :Att, :Yds, :TD, :Lng, :G, :Team, :Player)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()
        
        
def insert_into_receiving_table(df):
    insert_query = text("""
                        INSERT INTO receiving_stats (season_year, targets, receptions, rec_yards, rec_tds, rec_long, games_played, team_name, player_name)
                        VALUES(:Year, :Tgt, :Rec, :Yds, :TD, :Lng, :G, :Team, :Player)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()

      
def insert_into_passing_table(df):
    insert_query = text("""
                        INSERT INTO passing_stats (season_year, pass_completed, pass_attempts, pass_yards, pass_tds, pass_ints, pass_long, games_played, team_name, player_name)\
                        VALUES(:Year, :Cmp, :Att, :Yds, :TD, :Int, :Lng, :G, :Team, :Player)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()


def insert_into_kicking_table(df):
    insert_query = text("""
                        INSERT INTO kicking_stats (season_year, fg_attempts, fg_made, fg_long, xp_made, xp_attempts, games_played, team_name, player_name)
                        VALUES(:Year, :FGA, :FGM, :Lng, :XPM, :XPA, :G, :Team, :Player)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()
        

if __name__ == "__main__":
    insert_into_players_table(player_names)
    insert_into_teams_table(team_headers)
    insert_into_rushing_table(rush_player_stats)
    insert_into_receiving_table(rec_player_stats)
    insert_into_passing_table(passing_player_stats)
    insert_into_kicking_table(kicking_player_stats)