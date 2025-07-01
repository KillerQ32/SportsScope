from sqlalchemy import text

def all_players(limit):
    query = text(f"SELECT * FROM players LIMIT {limit};")
    return query