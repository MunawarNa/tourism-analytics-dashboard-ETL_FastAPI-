import psycopg2
import os
import dotenv

dotenv.load_dotenv("D:\\projects\\Tourism_analytics\\.env")

def calculate_city_statistics():
    try:
        conn = psycopg2.connect(f"dbname={os.getenv('dbname')} user={os.getenv('user')} password={os.getenv('password')} host={os.getenv('host')} port={os.getenv('port')}")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS city_hotel_stats (
            city TEXT PRIMARY KEY,
            total_hotels INT,
            avg_rating DECIMAL
            )
            """)
        cursor.execute("""
            INSERT INTO city_hotel_stats (city, total_hotels, avg_rating)
            SELECT city, COUNT(*), AVG(rating)
            FROM hotels 
            GROUP BY city
        """)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return False
    
print(calculate_city_statistics())