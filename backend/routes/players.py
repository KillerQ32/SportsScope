from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
from backend.queries.players_queries import all_players


router = APIRouter()

@router.get("/")
def get_players(limit: int = Query(50, ge=1, le=970),db=Depends(get_db)):
    query = all_players(limit)
    result = db.execute(query)
    return [dict(row._mapping) for row in result]

