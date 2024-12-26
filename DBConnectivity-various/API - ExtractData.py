import requests


# Define the API endpoint
url = 'https://opentdb.com/api.php?amount=1'

# Fetch the data
response = requests.get(url)
data = response.json()

# Print the raw data
print(data)

print()




## Transform Data:

# Extract relevant fields from the response
if data['results']:
    trivia_data = data['results'][0]
    transformed_data = {
        'question': trivia_data['question'],
        'correct_answer': trivia_data['correct_answer'],
        'incorrect_answers': trivia_data['incorrect_answers'],
        'category': trivia_data['category']
    }

    # Print transformed data
    print(transformed_data)
else:
    print("No trivia data found.")




## LAOD DATA TO POSTGRES NOW - SEPERATE THIS TO ANOTHER FILE LATER

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

# Create the destination table if it does not exist
create_table_query = """
CREATE TABLE IF NOT EXISTS public.trivia (
    id SERIAL PRIMARY KEY,
    question TEXT,
    correct_answer TEXT,
    incorrect_answers TEXT[],
    category TEXT
);
"""
cur.execute(create_table_query)
conn.commit()

# Define the SQL query for insertion
insert_query = """
INSERT INTO public.trivia (question, correct_answer, incorrect_answers, category)
VALUES (%s, %s, %s, %s)
"""

# Prepare data for insertion
incorrect_answers = transformed_data['incorrect_answers']

# Execute the query
cur.execute(insert_query, (transformed_data['question'], transformed_data['correct_answer'], incorrect_answers, transformed_data['category']))

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()

print("Data has been inserted into public.trivia.")
