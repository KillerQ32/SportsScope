from fastapi import APIRouter, Depends
from backend.db.database import get_db
import backend.queries.rushing_stats_queries as rs



router = APIRouter()

@router.get("/tds")
def get_tds(tds: int = 8, db=Depends(get_db)):
    """ return top rushing players sorted by tds. defualt is 8 or more tds"""
    
    query = rs.most_tds()
    result = db.execute(query, {"tds": tds})
    return [dict(row._mapping) for row in result]