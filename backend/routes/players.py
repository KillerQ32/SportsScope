from fastapi import APIRouter, Depends
from sqlalchemy import text
from backend.db.database import get_db

router = APIRouter()

@router.get("/")
def get_players(db=Depends(get_db)):
    result = db.execute(text("SELECT * FROM players LIMIT 20;"))
    return [dict(row._mapping) for row in result]