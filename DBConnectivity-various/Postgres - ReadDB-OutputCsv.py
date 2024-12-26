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

# Define the SQL query
query = "SELECT * FROM public.TableName LIMIT 10;"

# Use pandas to execute the query and store the result in a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Output the result to a CSV file
output_file = "/<My directory goes here>/FileDrop/Output/item_prices_sample.csv"
df.to_csv(output_file, index=False)


print(f"Query results have been written to {output_file}")
