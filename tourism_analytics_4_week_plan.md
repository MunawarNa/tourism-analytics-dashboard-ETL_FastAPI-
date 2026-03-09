# Tourism Analytics — 4‑Week Project Plan

This project combines **Data Engineering + Python Backend + Dashboard API**.

Goal: build a mini data platform that ingests data → processes it → stores analytics → serves dashboard-ready APIs.


✔ Data engineering transforms and stores processed data

✔ Backend reads processed data and exposes it as API

✔ Frontend calls API and displays results

---

## 🧱 Project Overview (Final Result)

You will build:

- ETL pipeline (extract → transform → load)
- Processed analytics tables
- Backend API (FastAPI recommended)
- Dashboard-ready endpoints
- PostgreSQL database
- Clean architecture

---

## 📂 Recommended File Structure

```text
tourism-analytics/
│
├── app/                     # Backend API
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   │
│   ├── routers/
│   │   ├── cities.py
│   │   ├── analytics.py
│   │   └── auth.py
│   │
│   ├── models/              # SQLAlchemy models
│   │   ├── city.py
│   │   ├── booking.py
│   │   └── analytics.py
│   │
│   ├── schemas/             # Pydantic schemas
│   │   ├── city.py
│   │   └── analytics.py
│   │
│   ├── services/            # Business logic
│   │   ├── analytics_service.py
│   │   └── city_service.py
│   │
│   └── utils/
│       └── helpers.py
│
├── etl/                     # Data engineering pipeline
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   └── seed_data.py
│
├── tests/
│
├── requirements.txt
├── .env
├── README.md
└── docker-compose.yml   (optional week 4)
```

---

## 🗓️ 4‑Week Roadmap

---

## 🚀 WEEK 1 — Foundation + Data Modeling

### Goal
Set up project + database + raw data.

### Tasks

1. **Project setup**
   - Create folders
   - Setup virtual environment
   - Install:
     - FastAPI
     - SQLAlchemy
     - Psycopg2
     - Pandas
     - Uvicorn

2. **Database design**
   Create tables:

   **Raw tables**
   - bookings_raw
   - cities
   - hotels

   **Processed analytics tables**
   - city_monthly_stats
   - revenue_summary

3. **Create fake dataset**
   Use CSV or Python script with:
   - city
   - booking_date
   - price
   - rating
   - hotel_id

4. **Test DB connection**
   - Create `database.py`
   - Create first model
   - Insert sample data

### 🎯 End of Week 1
- Database ready
- Data exists
- Project runs

---

## 🔄 WEEK 2 — Data Engineering Pipeline

### Goal
Build ETL pipeline like a data engineer.

### Tasks

1. **Extract (`extract.py`)**
   - Load CSV into Pandas

2. **Transform (`transform.py`)**
   - Clean missing values
   - Parse dates
   - Aggregate metrics:
     - visitors per city/month
     - average rating
     - total revenue

3. **Load (`load.py`)**
   - Insert aggregated results into analytics tables

4. **Pipeline runner (`pipeline.py`)**
   - Run: extract → transform → load

5. **Bonus (optional)**
   - Add logging

### 🎯 End of Week 2
- Running one command updates analytics tables.

---

## 🌐 WEEK 3 — Backend API Development

### Goal
Expose analytics to dashboard.

### Tasks

1. **Build API routes**
   Examples:

   - `GET /cities`
   - `GET /analytics/top-cities`
   - `GET /analytics/monthly-revenue`
   - `GET /analytics/city/{id}`

2. **Add service layer**
   - Keep business logic out of routes.

3. **Add pagination & filters**
   Example:
   - `/analytics/monthly?year=2025`

4. **Response schemas**
   - Use Pydantic models

5. **Basic authentication**
   - Simple JWT

### 🎯 End of Week 3
- Frontend can consume your API.

---

## 📊 WEEK 4 — Dashboard Readiness + Polish

### Goal
Make it portfolio-ready.

### Tasks

1. **Dashboard frontend (simple)**
   - Basic React dashboard template OR
   - Simple HTML + JS charts

2. **Add advanced backend features** (choose 2–3)
   - Caching
   - Background ETL task
   - Error handling middleware
   - API docs customization

3. **Docker (optional but impressive)**
   - Create docker-compose for API + Postgres

4. **Professional README**
   Include:
   - Architecture diagram
   - API endpoints
   - ETL explanation
   - Setup instructions

### 🎯 End of Week 4
- Portfolio-ready project.

---

## ⭐ Why This Project Is Strong

You’ll demonstrate:

- Data engineering workflow
- Backend architecture
- SQL skills
- API design
- System thinking

---

## 💡 Important Advice

Do **not** over-focus on the frontend.  
Your strength is backend + data pipeline design.

---

## 🚀 Optional Next Steps (After Week 4)

- Add scheduled ETL (cron / Celery)
- Add tests (pytest)
- Add monitoring or logging dashboard
- Deploy to cloud (Render, Railway, or similar)

