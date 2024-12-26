
# pip install nba-api pandas



# Import required libraries
from nba_api.stats.endpoints import leaguestandings
import pandas as pd



# Step 1: Connect to the NBA API and fetch the current NBA standings
standings = leaguestandings.LeagueStandings()


# info gather
# what methods are available for standings
# print(dir(standings))




# Step 2: Extract the JSON data from the API response
standings_data = standings.get_dict()



# Inspect the response structure
print(standings_data.keys()) 


# Step 3: The data is nested inside the "resultSets" key. Extract the relevant information.
standings_list = standings_data['resultSets'][0]['rowSet']  # Data rows
column_headers = standings_data['resultSets'][0]['headers']  # Column names



# Step 4: Insert the data into a pandas DataFrame
standings_df = pd.DataFrame(standings_list, columns=column_headers)



# Step 5: Display the first few rows of the DataFrame
print(standings_df.head())
