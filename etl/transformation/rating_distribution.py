import os
import psycopg2
import dotenv

dotenv.load_dotenv("D:\\projects\\Tourism_analytics\\.env")

def calculate_rating_distribution():
    try:
        conn = psycopg2.connect(f"dbname={os.getenv('dbname')} user={os.getenv('user')} password={os.getenv('password')} host={os.getenv('host')} port={os.getenv('port')}")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hotel_rating_dist (
            rating DECIMAL PRIMARY KEY,
            count INT)
        """)
        cursor.execute("""
            INSERT INTO hotel_rating_dist (rating, count)
            SELECT rating, COUNT(*)
            FROM hotels
            GROUP BY rating
        """)
        conn.commit()
        cursor.close()  
        conn.close()
        return True
    
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        return False
    
print(calculate_rating_distribution())