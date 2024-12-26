import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Before dropna
print("Original DataFrame:")
print(df)



# Using dropna
df_clean_dropna = df.dropna()

# After dropna
print("\nDataFrame after dropna:")
print(df_clean_dropna)



# 1. fillna()
# Purpose: Fills missing data (NaN values) with a specified value or method.
# Example: Replace NaN values with 0.

df_filled = df.fillna(8888)

print("\nDataFrame after fillna:")
print(df_filled)




# 2. replace()
# Purpose: Replaces specific values throughout the DataFrame with another value.
# Example: Replace all occurrences of 12 with NaN.

df_replaced = df.replace(12, np.nan)

print("\nDataFrame after replace:")
print(df_replaced)
# Usage: Useful for correcting or standardizing values, such as replacing placeholders or erroneous data.




# 3. drop_duplicates()
# Purpose: Removes duplicate rows from the DataFrame.
# Example: Drop duplicate rows based on all columns.

df_unique = df.drop_duplicates()

print("\nDataFrame after drop duplicates:")
print(df_unique)



# 4. astype()
# Purpose: Converts the data type of a column (or multiple columns).
# Example: Convert a column to float type.

df['A'] = df['A'].astype(float)
print("\nDataFrame after converting data type:")
print(df['A'])

# Usage: Important when you need to ensure columns have the correct data types, especially before performing calculations or aggregations.



# 12. isnull() / notnull()
# Purpose: Detects missing data (NaN values).
# Example: Find all rows where a column is NaN.

df_missing = df[df['A'].isnull()]

print("\nDataFrame after find missing value in A column:")
print(df_missing)


# Others:
# isnull() / notnull()
# pd.cut()
# pd.to_datetime()
# str.strip(), str.lower(), str.replace()
# query()
# rename()
# map()
# apply()
