from db.engine import engine
from sqlalchemy import text


def update_rushing_foreign_keys():
    update_team_id = text("""
                 UPDATE rushing_stats rs
                 SET team_id = t.team_id
                 FROM teams t
                 WHERE rs.team_name = t.team_name
                 AND rs.team_id IS NULL
                 """)
    
    update_player_id = text("""
                            UPDATE rushing_stats rs
                            SET player_id = p.player_id
                            FROM players p
                            WHERE rs.player_name = p.player_name
                            AND rs.player_id IS NULL
                            """)
    
    with engine.begin() as conn:
        conn.execute(update_team_id)
        conn.execute(update_player_id)
    


def update_receiving_foreign_keys():
    update_team_id = text("""
                 UPDATE receiving_stats rs
                 SET team_id = t.team_id
                 FROM teams t
                 WHERE rs.team_name = t.team_name
                 AND rs.team_id IS NULL
                 """)
    
    update_player_id = text("""
                            UPDATE receiving_stats rs
                            SET player_id = p.player_id
                            FROM players p
                            WHERE rs.player_name = p.player_name
                            AND rs.player_id IS NULL
                            """)
    
    with engine.begin() as conn:
        conn.execute(update_team_id)
        conn.execute(update_player_id)


def update_passing_foreign_keys():
    update_team_id = text("""
                 UPDATE passing_stats ps
                 SET team_id = t.team_id
                 FROM teams t
                 WHERE ps.team_name = t.team_name
                 AND ps.team_id IS NULL
                 """)
    
    update_player_id = text("""
                            UPDATE passing_stats ps
                            SET player_id = p.player_id
                            FROM players p
                            WHERE ps.player_name = p.player_name
                            AND ps.player_id IS NULL
                            """)
    
    with engine.begin() as conn:
        conn.execute(update_team_id)
        conn.execute(update_player_id)



def update_kicking_foreign_keys():
    update_team_id = text("""
                 UPDATE kicking_stats ks
                 SET team_id = t.team_id
                 FROM teams t
                 WHERE ks.team_name = t.team_name
                 AND ks.team_id IS NULL
                 """)
    
    update_player_id = text("""
                            UPDATE kicking_stats ks
                            SET player_id = p.player_id
                            FROM players p
                            WHERE ks.player_name = p.player_name
                            AND ks.player_id IS NULL
                            """)
    
    with engine.begin() as conn:
        conn.execute(update_team_id)
        conn.execute(update_player_id)



if __name__ == "__main__":
    update_rushing_foreign_keys()
    update_receiving_foreign_keys()
    update_passing_foreign_keys()
    update_kicking_foreign_keys()