from fastapi import FastAPI
import psycopg2
import os
import dotenv
from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv("D:\\projects\\Tourism_analytics\\.env")


api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev only; later use your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

database_url = f"dbname={os.getenv('dbname')} user={os.getenv('user')} password={os.getenv('password')} host={os.getenv('host')} port={os.getenv('port')}"
@api.get('/')
def main_page():

    return {"message": "tourism analytics page"}

@api.get('/analytics/cities')
def cities_statistics():

    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM city_hotel_stats; ")
            rows = cursor.fetchall()

    data = [{"city": row[0], "total_hotels": row[1], "avg_rating": float(row[2])} for row in rows]

    return {"data": data}

@api.get('/analytics/rating')
def rating_distribution():
    
    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM hotel_rating_dist;")
            rows = cursor.fetchall()

    data = [{"rating": row[0], "total_hotels": row[1]} for row in rows]

    return {"data": data}
    



