import requests
import pandas as pd
from datetime import datetime
import os as os


def extract():

    DATA_DIR = '/<My directory goes here>/FileDrop/Output'
    #now=datetime.now()
    #now='api'  # use this to test if file exists



    # Example API endpoint
    api_url = 'https://opentdb.com/api.php?amount=1'


    for file in ['apidata']:
        if os.path.exists(f'{DATA_DIR}/apidata-{now}.csv'):
            print(f'{DATA_DIR}/apidata-{now}.csv already exists, skipping extract task')
            return


    # Fetch data from API
    apidata = requests.get(api_url).json()


    # Save to CSV file
    pd.DataFrame(apidata).to_csv(f'{DATA_DIR}/apidata-{now}.csv', index=False)


extract()

# # Display the first few rows
# print(df.head())


# # Drop rows with missing values
# df_clean = df.dropna()

# # Remove duplicates
# df_clean = df_clean.drop_duplicates()

# Handle outliers (e.g., by capping or removing them)
#df_clean = df_clean[df_clean['numeric_column'] < some_threshold]



