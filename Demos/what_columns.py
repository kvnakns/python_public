import requests
import pandas as pd

# Define the API URL
api_url = "https://api.spacexdata.com/v5/launches"

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Load the data into a DataFrame
    data = response.json()
    df = pd.json_normalize(data)  # Normalize JSON to handle nested structures

    # Adjust Pandas settings to show all columns
    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.width', None)  # Expand display width

    # Display the column names and a sample of records
    print("Columns available in the API data:")
    print(df.columns)
    
    print("\nSample data from each column:")
    print(df.head())  # Shows the first 5 records
else:
    print("Failed to retrieve data:", response.status_code)
