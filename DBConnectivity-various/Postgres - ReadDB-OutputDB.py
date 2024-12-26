import psycopg2
import pandas as pd



# Establish connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="<db name>",
    user="< username >",
    password="< password >",
    host="< hostname >",
    port="< port >"
)

# Create a cursor object
cur = conn.cursor()

# Define the SQL query to fetch data
query = "SELECT amount, order_id, item_id, created_at, updated_at FROM public.TableName LIMIT 10;"

# Use pandas to execute the query and store the result in a DataFrame
df = pd.read_sql_query(query, conn)

# Create the destination table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS public.TableName_stage (
    id SERIAL PRIMARY KEY,
    amount NUMERIC(10, 2),
    order_id INTEGER,
    item_id INTEGER,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
"""
cur.execute(create_table_query)
conn.commit()

# Insert the data into the public.TableName_stage table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO public.TableName_stage (amount, order_id, item_id, created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s);
    """
    cur.execute(insert_query, (
        row['amount'],
        row['order_id'],
        row['item_id'],
        row['created_at'],
        row['updated_at']
    ))
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data has been inserted into public.TableName_stage.")
