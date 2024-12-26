import requests
import pandas as pd
from db_connection_psycopg2 import get_db_connection
import psycopg2
from psycopg2 import sql

# Step 1: Fetch data from the SpaceX API
def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an error for bad responses
        data = response.json()  # Parse JSON response
        return data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Step 2: Clean the data
def clean_data(raw_data):
    if not raw_data:
        print("No data to clean.")
        return None
    
    # Convert data to DataFrame for cleaning
    df = pd.json_normalize(raw_data)  # Flattens nested JSON
    
    # Keep essential columns only
    df = df[['name', 'date_utc', 'rocket', 'success', 'links.webcast', 'details']]

    # Fill missing data
    df['details'] = df['details'].fillna('No details available')
    df['date_utc'] = pd.to_datetime(df['date_utc'], errors='coerce')  # Convert to datetime
    
    return df

# Step 3: Load data into PostgreSQL
def load_data_to_db(cleaned_df):
    conn = get_db_connection()
    if conn is None:
        print("Database connection failed.")
        return
    
    try:
        with conn.cursor() as cur:
            for _, row in cleaned_df.iterrows():
                # Define an INSERT statement with conflict handling
                insert_query = sql.SQL(
                    """
                    INSERT INTO kev.spacex_launches (name, date_utc, rocket, success, youtube_id, details)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (name) DO NOTHING;
                    """
                )
                cur.execute(insert_query, (
                    row['name'], row['date_utc'], row['rocket'], row['success'],  row['links.webcast'], row['details']
                ))
            conn.commit()
            print(f"{len(cleaned_df)} records successfully loaded into the database.")
    except (Exception, psycopg2.DatabaseError) as e:
        print(f"Error loading data to database: {e}")
    finally:
        conn.close()



# Step 4: Main ETL Process
def etl_process():
    api_url = "https://api.spacexdata.com/v5/launches"  # SpaceX all launches API
    raw_data = fetch_data(api_url)
    
    if raw_data:
        cleaned_data = clean_data(raw_data)
        if cleaned_data is not None:
            load_data_to_db(cleaned_data)






# Run etl_process
# Ensures the script runs only when executed directly, not when imported as a module.
if __name__ == "__main__":
    etl_process()
