from fastapi import APIRouter, Depends, Query, Path
from backend.db.database import get_db
import backend.queries.receiving_stats_queries as rs

router = APIRouter()

@router.get("/receiving")
def get_receiving_stats(player_name: str, db=Depends(get_db)):
    """ return all receiving stats for a player"""
    query = rs.player_receiving_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]

@router.get("/receiving/{season_year}")
def get_receiving_stats_by_year(player_name: str, season_year: int = Path(..., ge=2022, le=2024), db=Depends(get_db)):
    """ return all receiving stats for a player in a specific season"""
    query = rs.player_receiving_stats_year()
    result = db.execute(query, {"player_name": player_name, "season_year": season_year})
    return [dict(row._mapping) for row in result]
