from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.kicking_stats_queries as ks

router = APIRouter()

@router.get("/fg_made")
def get_fg_made(limit: int = Query(10,ge=0),db=Depends(get_db)):
    query = ks.kicking_stats(limit)
    result = db.execute(query)
    return [dict(row._mapping) for row in result]