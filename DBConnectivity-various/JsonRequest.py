import requests
import pandas as pd

response = requests.get(
  "https://raw.githubusercontent.com/statsbomb/open-data/master/data/matches/223/282.json"
)
matches_df = pd.json_normalize(response.json(), sep='_')
#print(matches_df)


# can create separate dataframe for a certain match 
events_df = pd.json_normalize(response.json(), sep='_')
events_df["match_id"] = 3943077

print(events_df)




result= events_df.query("home_score >= 5")

print(result)