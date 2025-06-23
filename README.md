
# NFL Intelligence Hub

A full-stack project for NFL analytics combining data engineering and software engineering.
This project processes, stores, and visualizes NFL player and team statistics, built to run locally and scale to cloud deployment.

---

## Project Structure Summary

```
nfl-intelligence-hub/
├── frontend/                    # React + Tailwind
├── backend/                     # Python FastAPI
├── data-engineering/            # PySpark ETL + validation
├── db/                          # PostgreSQL schema
├── utils/                       # Reusable data functions
├── airflow/                     # (Optional) Scheduled ETL DAGs
└── docker-compose.yml           # Multi-container orchestration
```

---

## What We've Done So Far

### Data Engineering

- Built modular ETL scripts to extract, filter, and transform stats (rushing, receiving, passing, kicking).
- Created reusable filter utilities (like `filter_df`) to remove zero-value rows and standardize column types.
- Wrote deduplication logic to ensure no redundant players are inserted across multiple seasons.
- Aggregated player names/positions into a central `players` table with unique `player_id`s.

### PostgreSQL Integration

- Manual SQL schema: `players`, `teams`, `rushing_stats`, etc.
- Used raw SQL insert functions for transparency and control.
- Used SQLAlchemy with ORM abstraction

### Utils Directory

- **Why we chose it:** We noticed repeated code patterns (like filtering, column cleanup). Instead of duplicating across each stat file, we built `utils/` to hold:
  - `filter_df()` — keeps only meaningful player rows.
  - `strip_columns()` — removes irrelevant metadata.
  - `combine_df()` — merges seasonally split data.
- This allows us to centralize logic, improve readability, and make future refactoring easier.

### Docker Planning

- We will containerize each service: frontend, backend, data loader, and database.
- Docker enables us to run everything locally now and eventually on cloud infrastructure with consistency.

---

## Why Each Component Was Chosen

| Layer         | Stack                           | Why Chosen |
|---------------|---------------------------------|------------|
| Frontend      | React + Tailwind                | Fast, interactive UI, good for stat charts |
| Backend       | Python FastAPI                  | Simple, performant REST API |
| ETL Pipeline  | Pandas                          | Scalable + flexible transformation |
| DB            | PostgreSQL                      | Strong relational support for stats |
| DevOps        | Docker + Docker Compose         | Consistent dev/test/prod environments |
| Cloud         | AWS EC2, RDS, S3 (planned)      | Real-world deployment, autoscaling |
| Docs          | Swagger/OpenAPI                 | Auto-generated API documentation |
| Orchestration | Airflow (optional)              | For repeatable ETL on schedules |

---

## Key Observations

- Having a `utils/` module made the project **easier to scale and debug**.
- Filtering out players with no meaningful stats greatly reduced junk in our database.
- Using raw SQL gave us a deeper understanding of database schemas, joins, and integrity.
- We prioritized **clarity and learning** over full automation or abstraction.

---

## To Do

- [ ] Finish inserting all stats types (kicking, returns, passing)
- [ ] Build FastAPI endpoints
- [ ] Connect backend to frontend with Axios
- [ ] Dockerize and test multi-container stack
- [ ] Deploy to AWS (EC2 + RDS)
- [ ] Integrate charts and leaderboard UI

---

## Author

**Quinten Ballard**  
Computer Science @ UMBC  

**Jesse Ankrah**  
Information Science @ UMD 

