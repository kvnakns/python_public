

import psycopg2

def get_db_connection():
    # Connect to your PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname="<db name>",
            user="< username >",
            password="< password >",
            host="< hostname >",
            port="< port >"
)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None