from fastapi import APIRouter, Depends, Query, Path
from backend.db.database import get_db
import backend.queries.rushing_stats_queries as rs



router = APIRouter()

@router.get("/tds")
def get_tds(min_tds: int = Query(1, ge=0), db=Depends(get_db)):
    """ return top rushing players sorted by tds. defualt is 1 or more tds"""
    query = rs.most_tds()
    result = db.execute(query, {"min_tds": min_tds})
    return [dict(row._mapping) for row in result]

@router.get("/players")
def get_players(player_name: str, db=Depends(get_db)):
    """ return all rushing players"""
    query = rs.player_rushing_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]

@router.get("/players/{season_year}")
def get_players_by_year(player_name: str, season_year: int = Path(..., ge=2022, le=2024), db=Depends(get_db)):
    """ return all rushing players for a specific season"""
    query = rs.player_rushing_stats_year()
    result = db.execute(query, {"player_name": player_name, "season_year": season_year})
    return [dict(row._mapping) for row in result]
