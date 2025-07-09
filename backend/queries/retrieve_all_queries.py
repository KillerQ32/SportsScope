from sqlalchemy import text

def get_all_stats_by_player_name_query(player_name: str):
    player_name = player_name.lower()
    return {
        "passing": text("""
            SELECT 
                ps.season_year,
                ps.pass_completed,
                ps.pass_attempts,
                ps.pass_yards,
                ps.pass_tds,
                ps.pass_ints,
                ps.pass_long,
                ps.games_played,
                t.team_name
            FROM passing_stats ps
            JOIN players p ON ps.player_id = p.player_id
            JOIN teams t ON ps.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name
        """).bindparams(player_name=player_name),

        "rushing": text("""
            SELECT 
                rs.season_year,
                rs.rush_attempts,
                rs.rush_yards,
                rs.rush_tds,
                rs.longest_rush,
                t.team_name
            FROM rushing_stats rs
            JOIN players p ON rs.player_id = p.player_id
            JOIN teams t ON rs.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name
        """).bindparams(player_name=player_name),

        "receiving": text("""
            SELECT 
                rs.season_year,
                rs.targets,
                rs.rec_yards,
                rs.rec_tds,
                rs.rec_long,
                t.team_name
            FROM receiving_stats rs
            JOIN players p ON rs.player_id = p.player_id
            JOIN teams t ON rs.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name
        """).bindparams(player_name=player_name),

        "kicking": text("""
            SELECT 
                ks.season_year,
                ks.fg_attempts,
                ks.fg_made,
                ks.fg_long,
                ks.xp_made,
                ks.xp_attempts,
                t.team_name
            FROM kicking_stats ks
            JOIN players p ON ks.player_id = p.player_id
            JOIN teams t ON ks.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name
        """).bindparams(player_name=player_name),
    }

def get_all_stats_by_player_name_season_year_query(player_name: str, season_year: int):
    player_name = player_name.lower()
    return {
        "passing": text("""
            SELECT 
                ps.season_year,
                ps.pass_completed,
                ps.pass_attempts,
                ps.pass_yards,
                ps.pass_tds,
                ps.pass_ints,
                ps.pass_long,
                ps.games_played,
                t.team_name
            FROM passing_stats ps
            JOIN players p ON ps.player_id = p.player_id
            JOIN teams t ON ps.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name AND ps.season_year = :season_year
        """).bindparams(player_name=player_name, season_year=season_year),

        "rushing": text("""
            SELECT 
                rs.season_year,
                rs.rush_attempts,
                rs.rush_yards,
                rs.rush_tds,
                rs.longest_rush,
                t.team_name
            FROM rushing_stats rs
            JOIN players p ON rs.player_id = p.player_id
            JOIN teams t ON rs.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name AND rs.season_year = :season_year
        """).bindparams(player_name=player_name, season_year=season_year),

        "receiving": text("""
            SELECT 
                rs.season_year,
                rs.targets,
                rs.rec_yards,
                rs.rec_tds,
                rs.rec_long,
                t.team_name
            FROM receiving_stats rs
            JOIN players p ON rs.player_id = p.player_id
            JOIN teams t ON rs.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name AND rs.season_year = :season_year
        """).bindparams(player_name=player_name, season_year=season_year),

        "kicking": text("""
            SELECT 
                ks.season_year,
                ks.fg_attempts,
                ks.fg_made,
                ks.fg_long,
                ks.xp_made,
                ks.xp_attempts,
                t.team_name
            FROM kicking_stats ks
            JOIN players p ON ks.player_id = p.player_id
            JOIN teams t ON ks.team_id = t.team_id
            WHERE LOWER(p.player_name) = :player_name AND ks.season_year = :season_year
        """).bindparams(player_name=player_name, season_year=season_year),
    }