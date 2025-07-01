from sqlalchemy import text

def kicking_stats(limit):
    query = text(f"""
                 select p.player_name, k.fg_attempts, k.fg_made, k.xp_attempts,k.xp_made,k.season_year
                from kicking_stats k
                join players p 
                on p.player_id = k.player_id
                order by k.fg_made desc
                limit {limit}
                 """)
    return query