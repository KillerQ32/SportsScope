from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import players
from backend.routes import rush_stats
from backend.routes import passing_stats
from backend.routes import kicking_stats
from backend.routes import receiving_stats

app = FastAPI()
app.include_router(players.router, prefix="/players", tags=["Players"])
app.include_router(rush_stats.router, prefix="/rushing", tags=["Rush"])
app.include_router(passing_stats.router, prefix="/passing", tags=["Passing"])
app.include_router(kicking_stats.router, prefix="/kicking", tags=["kicking"])
app.include_router(receiving_stats.router, prefix="/receiving", tags=["Receiving"])

origins = ["http://localhost:5500"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"]
)

@app.get("/")
def root():
    return {"Message": "NFL stats API"}

    