from sqlalchemy import text

def player_passing_stats():
    query = text("""select p.player_name, p.position, ps.pass_completed, ps.pass_attempts, ps.pass_yards, ps.pass_tds, ps.pass_ints, ps.pass_long, ps.season_year
                FROM passing_stats ps
                join players p 
                on p.player_id = ps.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name);""")
    return query

def player_passing_stats_year():
    query = text("""select p.player_name, p.position, ps.pass_completed, ps.pass_attempts, ps.pass_yards, ps.pass_tds, ps.pass_ints, ps.pass_long, ps.season_year
                FROM passing_stats ps
                join players p 
                on p.player_id = ps.player_id
                WHERE LOWER(p.player_name) = LOWER(:player_name) AND ps.season_year = :season_year;""")
    return query

def player_passing_touchdowns():
    query = text("""select p.player_name, p.position, ps.pass_tds, ps.season_year
                FROM passing_stats ps
                join players p 
                on p.player_id = ps.player_id
                WHERE ps.pass_tds >= :min_pass_tds
                order by ps.pass_tds desc;""")
    return query

def player_passing_yds():
    query = text("""select p.player_name, p.position, ps.pass_yards, ps.season_year
                FROM passing_stats ps
                join players p 
                on p.player_id = ps.player_id
                WHERE ps.pass_yards >= :min_pass_yards
                order by ps.pass_yards desc;""")
    return query