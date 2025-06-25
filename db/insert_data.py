from db.engine import engine
from sqlalchemy import text

def insert_into_players_table(df):
    insert_query = text("""
                        INSERT INTO players (player_name, position)
                        VALUES(:Player, :Pos)
                        ON CONFLICT (player_name) DO NOTHING;
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()

from filtered_stats_data.player_names import player_names
insert_into_players_table(player_names)

def insert_into_teams_table(df):
    insert_query = text("""
                        INSERT INTO teams (team_name, division, conference)
                        VALUES(:teamAbv, :division, :conference)
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()
    
from filtered_stats_data.teams import team_headers
insert_into_teams_table(team_headers)

def insert_into_rushing_table(df):
    insert_query = text("""
                        INSERT INTO rushing_stats ()
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()
        
from filtered_stats_data.rushing import rush_player_stats
insert_into_rushing_table(rush_player_stats)
        
def insert_into_receiving_table(df):
    insert_query = text("""
                        INSERT INTO receiving_stats ()
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()
        
        
def insert_into_passing_table(df):
    insert_query = text("""
                        INSERT INTO passing_stats ()
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()


def insert_into_kicking_table(df):
    insert_query = text("""
                        INSERT INTO kicking_stats ()
                        """)
    
    with engine.connect() as conn:
        conn.execute(insert_query,df.to_dict(orient="records"))
        conn.commit()