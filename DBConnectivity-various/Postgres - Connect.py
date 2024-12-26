
import psycopg2
from psycopg2 import sql
from decimal import Decimal  # Import Decimal class
from datetime import datetime  # Import datetime class

# Database connection settings
conn = psycopg2.connect(
    dbname="<db name>",
    user="< username >",
    password="< password >",
    host="< hostname >",
    port="< port >"
)

# Create a cursor object
cur = conn.cursor()

# Example: Insert a record
# cur.execute(
#     sql.SQL("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"),
#     ("John Doe", "john@example.com", "123-456-7890")
# )

# Example: Select records
cur.execute("select * from public.TableName limit 10;")
rows = cur.fetchall()

# Process and print each row
for row in rows:
    processed_row = []
    for item in row:
        if isinstance(item, Decimal):
            processed_row.append(float(item))  # Convert Decimal to float
        elif isinstance(item, datetime):
            processed_row.append(item.strftime('%Y-%m-%d %H:%M:%S'))  # Format datetime as string
        else:
            processed_row.append(item)  # Keep other types as they are
    print(tuple(processed_row))


# Example: Update a record
# cur.execute(
#     sql.SQL("UPDATE customers SET email = %s WHERE id = %s"),
#     ("newemail@example.com", 1)
# )

# Example: Delete a record
# cur.execute(
#     sql.SQL("DELETE FROM TableName WHERE id = %s"),
#     (1,)
# )

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
