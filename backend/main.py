from fastapi import FastAPI, Depends, HTTPException
from backend.db.database import get_db
from backend.routes import players


app = FastAPI()
app.include_router(players.router, prefix="/players", tags=["Players"])

@app.get("/")
def root():
    return {"Message": "NFL stats API"}

    