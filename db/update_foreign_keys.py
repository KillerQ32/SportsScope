from db.engine import engine
from sqlalchemy import text


def update_rushing_foreign_keys():
    # update_team_id = text("""
    #              UPDATE rushing_stats rs
    #              SET team_id = t.team_id
    #              FROM teams t
    #              WHERE rs.team_name = t.team_name
    #              AND rs.team_id IS NULL
    #              """)
    
    update_player_id = text("""
                            UPDATE rushing_stats rs
                            SET player_id = p.player_id
                            FROM players p
                            WHERE rs.player_name = p.player_name
                            AND rs.player_id IS NULL
                            """)
    
    with engine.connect() as conn:
        # conn.execute(update_team_id)
        conn.execute(update_player_id)
        conn.commit()

update_rushing_foreign_keys()