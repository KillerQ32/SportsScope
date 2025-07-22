from fastapi import APIRouter, Depends, Path
from backend.db.database import get_db
import backend.queries.retrieve_all_queries as ra

router = APIRouter()

@router.get('/stats')
def get_all_stats(player_name: str, db=Depends(get_db)):
    player_name = player_name.lower()
    """Return all stats for a player across all stat tables"""
    queries = ra.get_all_stats_by_player_name_query(player_name)
    stats = {}

    for stat_type, query in queries.items():
        result = db.execute(query)
        stats[stat_type] = [dict(row._mapping) for row in result]

    return stats

@router.get('/stats/{season_year}')
def get_all_stats(player_name: str, season_year: int = Path(...,ge=2022, le=2024), db=Depends(get_db)):
    player_name = player_name.lower()
    """Return all stats for a player across all stat tables"""
    queries = ra.get_all_stats_by_player_name_season_year_query(player_name, season_year)
    stats = {}

    for stat_type, query in queries.items():
        result = db.execute(query)
        stats[stat_type] = [dict(row._mapping) for row in result]

    return stats