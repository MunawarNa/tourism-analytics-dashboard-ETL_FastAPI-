import requests
import dotenv
import os 
import psycopg2

dotenv.load_dotenv("D:\\projects\\Tourism_analytics\\.env")

def extract_data():

    api_key = os.getenv("API_KEY")  

    params = {
        "country": "France"
    }
    headers = {
    "X-API-KEY": api_key
    }

    url = "https://api.hotels-api.com/v1/hotels/search"

    try:
        response = requests.get(url=url, params=params, headers=headers)
        response.raise_for_status()
        date = response.json()
         
        conn = psycopg2.connect(f"dbname={os.getenv('dbname')} user={os.getenv('user')} password={os.getenv('password')} host={os.getenv('host')} port={os.getenv('port')}")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hotels (
            hotel_id TEXT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255),
            city VARCHAR(255),
            country VARCHAR(255),
            price DECIMAL,
            rating DECIMAL
        )
        """)
        for hotel in date["data"]:
            cursor.execute("""
                INSERT INTO hotels (hotel_id, name, address, city, country, rating)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                hotel.get("id"),
                hotel.get("name"),
                hotel.get("address"),
                hotel.get("city"),
                hotel.get("country"),
                hotel.get("rating")
            ))
        conn.commit()
        cursor.close()
        conn.close()
        return date

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
print(extract_data())
