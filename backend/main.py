from fastapi import FastAPI
from backend.routes import players


app = FastAPI()
app.include_router(players.router, prefix="/players", tags=["Players"])

@app.get("/")
def root():
    return {"Message": "NFL stats API"}

    