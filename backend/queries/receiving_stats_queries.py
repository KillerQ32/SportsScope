from sqlalchemy import text

def player_receiving_stats():
    query = text("""select p.player_name, p.position, rs.targets, rs.receptions, rs.rec_yards, rs.rec_tds, rs.rec_long, rs.season_year
                FROM receiving_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name);""")
    return query

def player_receiving_stats_year():
    query = text("""select p.player_name, p.position, rs.targets, rs.receptions, rs.rec_yards, rs.rec_tds, rs.rec_long, rs.season_year
                FROM receiving_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name) AND rs.season_year = :season_year;""")
    return query