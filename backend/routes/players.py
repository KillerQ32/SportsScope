from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.players_queries as pq


router = APIRouter()

@router.get("/")
def get_players(limit: int = Query(50, ge=1, le=970),db=Depends(get_db)):
    query = pq.all_players(limit)
    result = db.execute(query)
    return [dict(row._mapping) for row in result]

