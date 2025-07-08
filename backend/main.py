from fastapi import FastAPI
from backend.routes import players
from backend.routes import rush_stats
from backend.routes import passing_stats
from backend.routes import kicking_stats
from backend.routes import receiving_stats
from backend.routes import retrieve_all

app = FastAPI()
app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(rush_stats.router, prefix="/rushing", tags=["Rush"])
app.include_router(passing_stats.router, prefix="/passing", tags=["Passing"])
app.include_router(kicking_stats.router, prefix="/kicking", tags=["kicking"])
app.include_router(receiving_stats.router, prefix="/receiving", tags=["Receiving"])
app.include_router(retrieve_all.router, prefix="/all", tags=["all"])

@app.get("/")
def root():
    return {"Message": "NFL stats API"}

    