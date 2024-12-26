import pandas as pd

# Create a sample DataFrame
data = {
    'Player': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie', 'Alice'],
    'Team': ['Team A', 'Team A', 'Team B', 'Team B', 'Team A', 'Team B', 'Team A'],
    'Points': [10, 20, 15, 30, 25, 35, 20],
    'Assists': [5, 7, 8, 5, 9, 6, 7]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Create a pivot table
pivot_table = df.pivot_table(values=['Points', 'Assists'],  # The columns you want to aggregate (e.g., 'Points' and 'Assists').
                             index='Player',                # The columns to group by (e.g., 'Player')
                             columns='Team',                # The columns to pivot (e.g., 'Team')
                             aggfunc='sum',                 # The aggregation function to apply (e.g., 'sum' to sum the values)
                             fill_value=0)                  # The value to replace missing values (e.g., 0)

print("\nPivot Table:")
print(pivot_table)

# Reset the index (optional)
pivot_table_reset = pivot_table.reset_index()
print("\nPivot Table with Reset Index:")
print(pivot_table_reset)

