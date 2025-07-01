from fastapi import APIRouter, Depends, Query, Path
from backend.db.database import get_db
import backend.queries.passing_stats_queries as ps



router = APIRouter()

@router.get("/players")
def get_players(player_name: str, db=Depends(get_db)):
    """ return all passing players"""
    query = ps.player_passing_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]

@router.get("/players/{season_year}")
def get_players_by_year(player_name: str, season_year: int = Path(..., ge=2022, le=2024), db=Depends(get_db)):
    """ return all passing players for a specific season"""
    query = ps.player_passing_stats_year()
    result = db.execute(query, {"player_name": player_name, "season_year": season_year})
    return [dict(row._mapping) for row in result]