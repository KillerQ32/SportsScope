from sqlalchemy import text

def most_tds():
    query = text("""select p.player_name, rs.rush_attempts, rs.rush_yards, rs.rush_tds, rs.season_year
                FROM rushing_stats rs
                join players p 
                on p.player_id = rs.player_id
                WHERE rs.rush_tds >= :min_tds
                order by rs.rush_tds desc""")
    return query