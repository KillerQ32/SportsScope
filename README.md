
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


### API Development

- Developed GET endpoints for all major stat categories (rushing, passing, receiving, kicking) using FastAPI.
- Incorporated parameter validation using FastAPI's `Path` and `Query`, including range limits and type enforcement.
- Protected against SQL injection via parameterized queries.
- Served documentation with Swagger UI for testing and validation.
- Identified and refactored redundant API logic by modularizing stat route handlers.

### Bug Fixes

- Fixed an issue where only the first SQL update query was executing; resolved with `engine.begin()`.
- Addressed NULL foreign key values by adjusting insert order and enforcing referential integrity.
- Cleaned all stat data of inconsistent player and team values.
- Dropped columns containing personally identifiable information when required.

### PostgreSQL Integration

- Manual SQL schema: `players`, `teams`, `rushing_stats`, etc.
- Used raw SQL insert functions for transparency and control.
- Used SQLAlchemy without ORM abstraction

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

- [x] Finish inserting all stats types (kicking, returns, passing)
- [ ] Build FastAPI endpoints
- [ ] Connect backend to frontend with Axios
- [ ] Dockerize and test multi-container stack
- [ ] Deploy to AWS (EC2 + RDS)
- [ ] Integrate charts and leaderboard UI
- [ ] Integrate External APIs
- [ ] NBA integration
- [x] Finish Database
- [ ] Create Frontend

---

## Planning for Frontend

---
## Issues we came across
- Issue: Swagger showed wrong summary (e.g., GET teams instead of rushing stats); Fix: matched function name under decorator.
- Issue: player_id updates weren’t executing; Fix: required separate transactions and commits.
- Issue: uvicorn command not recognized; Fix: added user install path to system and corrected module syntax.

- Issue: team_name mis-match between tables; Fix: located wrong information and updated with query
- Issue: engine.connect() would only run one query had to swap to engine.begin() for both queries to run
 
---

## Authors Documentation
  
  ### Why we chose this Project?
    We wanted a project that combined both backend engineering and data transformation work, built on real-world, accessible sports data (NFL).

  ### Our Approach
    We started with scraping and cleaning raw stats data, then normalized it into PostgreSQL. We built APIs on top using FastAPI, focused on clarity and type-safe query patterns, and designed a frontend UI to visualize performance.

  ### Our Observations
    Building modular utilities (ETL filters, SQL insert functions) and simplifying logic early on saved time debugging later. Investing in raw SQL knowledge helped us better understand integrity constraints and query performance.

---
## Author

**Quinten Ballard**  
Computer Science @ UMBC  

**Jesse Ankrah**  
Information Science @ UMD 

---
