from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.passing_stats_queries as ps



router = APIRouter()

@router.get("/players")
def get_players(player_name: str, db=Depends(get_db)):
    """ return all passing players"""
    query = ps.player_passing_stats()
    result = db.execute(query, {"player_name": player_name})
    return [dict(row._mapping) for row in result]