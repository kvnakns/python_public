import requests
import pandas as pd


# Example API endpoint
api_url = 'https://opentdb.com/api.php?amount=1'

# Fetch data from API
response = requests.get(api_url)
data = response.json()

# Convert JSON data to DataFrame
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())



# Drop rows with missing values
df_clean = df.dropna()

# Remove duplicates
df_clean = df_clean.drop_duplicates()

# Handle outliers (e.g., by capping or removing them)
#df_clean = df_clean[df_clean['numeric_column'] < some_threshold]
