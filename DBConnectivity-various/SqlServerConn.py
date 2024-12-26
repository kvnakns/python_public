import pyodbc

# Notes:
# Had to create inbound rule for my laptop
# Had to create Windows Defender Firewall rule to allow port 1433 connections - Public

# Connection parameters
server = '< server name >'
database = '< db name >'
username = '< username >'
password = '< password >'

# Establish a connection
connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Create a cursor object
cursor = connection.cursor()

try:
    # Execute a SQL query
    cursor.execute("SELECT top 8  DatabaseLogID, PostTime, [Schema],Object FROM [AdventureWorks2022].[dbo].[DatabaseLog]")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("Error while executing SQL query:", e)

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("SQL Server connection is closed")