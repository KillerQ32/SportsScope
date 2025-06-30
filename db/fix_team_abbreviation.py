from db.engine import engine
from sqlalchemy import text

"""
This file is responsible for fixing issues related to database team abbreviation inconsistencies between players and teams.
"""

def fix_team_abbreviation_rushing_stats():
    """
    Fixes inconsistencies in team abbreviations within the rushing_stats table to align with the teams table.
    Replaces incorrect team abbreviations with the correct ones.
    """

    corrections = {
        "LVR": "LV",
        "SFO": "SF",
        "NOR": "NO",
        "GNB": "GB",
        "NWE": "NE",
        "WAS": "WSH",
        "TAM": "TB",
        "KAN": "KC"
    }

    case_stmt = "CASE team_name\n"
    for wrong, correct in corrections.items():
        case_stmt += f"    WHEN '{wrong}' THEN '{correct}'\n"
    case_stmt += "    ELSE team_name\nEND"

    update_query = f"""
    UPDATE rushing_stats
    SET team_name = {case_stmt}
    WHERE team_name IN ({', '.join(f"'{abbr}'" for abbr in corrections)});
    """

    with engine.connect() as conn:
        conn.execute(text(update_query))
        conn.commit()

    print(" Team abbreviations in rushing_stats table have been updated.")

def fix_team_abbreviation_receiving_stats():
    """
    Fixes inconsistencies in team abbreviations within the receiving_stats table to align with the teams table.
    Replaces incorrect team abbreviations with the correct ones.
    """

    corrections = {
        "LVR": "LV",
        "SFO": "SF",
        "NOR": "NO",
        "GNB": "GB",
        "NWE": "NE",
        "WAS": "WSH",
        "TAM": "TB",
        "KAN": "KC"
    }

    case_stmt = "CASE team_name\n"
    for wrong, correct in corrections.items():
        case_stmt += f"    WHEN '{wrong}' THEN '{correct}'\n"
    case_stmt += "    ELSE team_name\nEND"

    update_query = f"""
    UPDATE receiving_stats
    SET team_name = {case_stmt}
    WHERE team_name IN ({', '.join(f"'{abbr}'" for abbr in corrections)});
    """

    with engine.connect() as conn:
        conn.execute(text(update_query))
        conn.commit()

if __name__ == "__main__":
    fix_team_abbreviation()
