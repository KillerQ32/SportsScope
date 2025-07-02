from sqlalchemy import text

def most_tds():
    query = text("""select p.player_name, rs.rush_attempts, rs.rush_yards, rs.rush_tds, rs.season_year
                FROM rushing_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE rs.rush_tds >= :min_tds
                order by rs.rush_tds desc;""")
    return query

def player_rushing_stats():
    query = text("""select p.player_name, p.position, rs.rush_attempts, rs.rush_yards, rs.rush_tds, rs.longest_rush, rs.season_year
                FROM rushing_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name);""")
    return query

def player_rushing_stats_year():
    query = text("""select p.player_name, p.position, rs.rush_attempts, rs.rush_yards, rs.rush_tds, rs.longest_rush, rs.season_year
                FROM rushing_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name) AND rs.season_year = :season_year
                WHERE p.player_id = :player_id;""")
    return query