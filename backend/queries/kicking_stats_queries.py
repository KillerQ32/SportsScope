from sqlalchemy import text

def xp_made():
    query = text("""select p.player_name, p.position, k.xp_made, k.season_year
                FROM kicking_stats k
                join players p 
                on p.player_id = k.player_id
                where k.xp_made >= :min_xp_made
                order by k.xp_made desc;""")
    return query

def fg_made():
    query = text("""select p.player_name, p.position, k.fg_made, k.season_year
                FROM kicking_stats k
                join players p 
                on p.player_id = k.player_id
                where k.fg_made >= :min_fg_made
                order by k.fg_made desc;""")
    return query

def kicking_stats():
    query = text(f"""
                 select p.player_name, k.fg_attempts, k.fg_made, k.fg_long, k.xp_attempts,k.xp_made, k.season_year
                from kicking_stats k
                join players p 
                on p.player_id = k.player_id
                Where k.fg_made >= :min_fg_made
                order by k.fg_made desc
                ;
                 """)
    return query

def player_kicking_stats():
    query = text(f"""
                 select p.player_name, k.fg_attempts, k.fg_made, k.fg_long, k.xp_attempts, k.xp_made, k.season_year
                from kicking_stats k
                join players p 
                on p.player_id = k.player_id
                Where LOWER(p.player_name) = LOWER(:player_name);
                 """)
    return query

def player_kicking_stats_year():
    query = text(f"""
                 select p.player_name, k.fg_attempts, k.fg_made, k.fg_long, k.xp_attempts, k.xp_made, k.season_year
                from kicking_stats k
                join players p 
                on p.player_id = k.player_id
                Where LOWER(p.player_name) = LOWER(:player_name) AND k.season_year = :season_year;
                 """)
    return query