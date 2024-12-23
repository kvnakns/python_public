
import pandas as pd

# Load CSV data with pandas
data = pd.read_csv("data.csv")
print("Average of column:", data["column_name"].mean())

# Filter rows based on a condition
filtered_data = data[data["column_name"] > 50]
print(filtered_data)
