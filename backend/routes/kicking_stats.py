from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.kicking_stats_queries as ks

router = APIRouter()
@router.get("/xp_made")
def get_xp_made(min_xp_made: int = Query(1, ge=0), db=Depends(get_db)):
    query = ks.xp_made()
    result = db.execute(query, {"min_xp_made": min_xp_made})
    return [dict(row._mapping) for row in result]

@router.get("/fg_made")
def get_fg_made(min_fg_made: int = Query(10,ge=0),db=Depends(get_db)):
    query = ks.kicking_stats()
    result = db.execute(query,{"min_fg_made": min_fg_made})
    return [dict(row._mapping) for row in result]

@router.get("/players")
def get_player_fg_made(player_name: str, db=Depends(get_db)):
    player_name = player_name.lower()
    query = ks.player_kicking_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]

@router.get("/players/{season_year}")
def get_player_fg_made_year(player_name: str, season_year: int, db=Depends(get_db)):
    player_name = player_name.lower()
    query = ks.player_kicking_stats_year()
    result = db.execute(query, {"player_name": player_name, "season_year": season_year})
    return [dict(row._mapping) for row in result]

