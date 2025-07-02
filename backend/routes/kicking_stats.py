from fastapi import APIRouter, Depends, Query
from backend.db.database import get_db
import backend.queries.kicking_stats_queries as ks

router = APIRouter()

@router.get("/fg_made")
def get_fg_made(min_fg_made: int = Query(10,ge=0),db=Depends(get_db)):
    query = ks.kicking_stats()
    result = db.execute(query,{"min_fg_made": min_fg_made})
    return [dict(row._mapping) for row in result]