from db.engine import engine
from sqlalchemy import text

"""
This file is made for removing any data from the database
used it to remove temp columns from stats tables
"""

def remove_player_names_rushing_stats():
    #Drop player_name and team_name columns from rushing_stats table
    delete_query = text("""
        ALTER TABLE rushing_stats
        DROP COLUMN player_name,
        DROP COLUMN team_name
    """)

    with engine.begin() as conn:
        conn.execute(delete_query)

def remove_player_names_kicking_stats():
    #Drop player_name and team_name columns from kicking_stats table
    delete_query = text("""
        ALTER TABLE kicking_stats
        DROP COLUMN player_name,
        DROP COLUMN team_name
    """)

    with engine.begin() as conn:
        conn.execute(delete_query)

def remove_player_names_receiving_stats():
    #Drop player_name and team_name columns from receiving_stats table
    delete_query = text("""
        ALTER TABLE receiving_stats
        DROP COLUMN player_name,
        DROP COLUMN team_name
    """)

    with engine.begin() as conn:
        conn.execute(delete_query)

def remove_player_names_passing_stats():
    #Drop player_name and team_name columns from passing_stats table
    delete_query = text("""
        ALTER TABLE passing_stats
        DROP COLUMN player_name,
        DROP COLUMN team_name
    """)

    with engine.begin() as conn:
        conn.execute(delete_query)

if __name__ == "__main__":
    remove_player_names_rushing_stats()
    remove_player_names_receiving_stats()
    remove_player_names_passing_stats()
    remove_player_names_kicking_stats()
