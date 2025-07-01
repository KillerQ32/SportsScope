from fastapi import FastAPI
from backend.routes import players
from backend.routes import rush_stats
from backend.routes import kicking_stats

app = FastAPI()
app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(rush_stats.router, prefix="/rushing", tags=["Rush"])
app.include_router(kicking_stats.router, prefix="/kicking", tags=["kicking"])

@app.get("/")
def root():
    return {"Message": "NFL stats API"}

    