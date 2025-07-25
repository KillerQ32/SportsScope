from fastapi import APIRouter, Depends, Query, Path
from backend.db.database import get_db
import backend.queries.receiving_stats_queries as rs

router = APIRouter()

@router.get("/yds")
def get_yards(min_yards: int = Query(1,ge=0),db=Depends(get_db)):
    """return top receiving players sorted by yds. default is 1 or more yds"""
    query = rs.most_yds()
    result = db.execute(query, {"min_yards": min_yards})
    return [dict(row._mapping) for row in result]

@router.get("/tds")
def get_tds(min_tds: int = Query(1,ge=0),db=Depends(get_db)):
    """return top receiving players sorted by tds. default is 1 or more tds"""
    query = rs.most_tds()
    result = db.execute(query, {"min_tds": min_tds})
    return [dict(row._mapping) for row in result]

@router.get("/players")
def get_receiving_stats(player_name: str, db=Depends(get_db)):
    player_name = player_name.lower()
    """ return all receiving stats for a player"""
    query = rs.player_receiving_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]

@router.get("/players/{season_year}")
def get_receiving_stats_by_year(player_name: str, season_year: int = Path(..., ge=2022, le=2024), db=Depends(get_db)):
    player_name = player_name.lower()
    """ return all receiving stats for a player in a specific season"""
    query = rs.player_receiving_stats_year()
    result = db.execute(query, {"player_name": player_name, "season_year": season_year})
    return [dict(row._mapping) for row in result]
