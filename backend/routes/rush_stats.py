from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.rushing_stats_queries as rs



router = APIRouter()

@router.get("/tds")
def get_tds(min_tds: int = Query(0, ge=0), db=Depends(get_db)):
    """ return top rushing players sorted by tds. defualt is 0 or more tds"""
    
    query = rs.most_tds()
    result = db.execute(query, {"min_tds": min_tds})
    return [dict(row._mapping) for row in result]

@router.get("/players")
def get_players(player_id: int, db=Depends(get_db)):
    """ return all rushing players"""
    query = rs.player_rushing_stats()
    result = db.execute(query, {"player_id": player_id})
    return [dict(row._mapping) for row in result]