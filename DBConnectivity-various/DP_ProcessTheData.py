
from DP_DataProcessing import *

# Create an instance of DataProcessor with a CSV file path
processor = DataProcessor("/<My directory goes here>/Raw/DE_sample_50.csv")

# Load the data
print(processor.load_data())

# Clean the data
print(processor.clean_data())

# Calculate the average value of the 'Revenue' column
print(processor.calculate_average("Revenue"))





# Save the cleaned data to a new CSV file
output_file = "/<My directory goes here>/Cleaned/DE_cleaned_sample_50.csv"
print(processor.save_cleaned_data(output_file))