
import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        # Initialize the class with the file path to the CSV file
        self.file_path = file_path
        self.data = None
    
    # Method to load the CSV file into a DataFrame
    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            return f"Data loaded successfully from {self.file_path}."
        except FileNotFoundError:
            return "Error: File not found."
    
 # Method to clean the data (e.g., remove rows with missing values)
    def clean_data(self):
        if self.data is not None:
            # Remove rows with missing values
            self.data.dropna(inplace=True)
            
            # Modify 'Category' column: remove "5k-" from the beginning of strings
            if 'Category' in self.data.columns:
                self.data['Category'] = self.data['Category'].str.replace(r'^5k-', '', regex=True)
                return "Data cleaned: removed rows with missing values and updated 'Category' column."
            else:
                return "Data cleaned: removed rows with missing values, but 'Category' column not found."
        else:
            return "Error: No data to clean. Please load the data first."
    
    # Method to calculate the average value of a column
    def calculate_average(self, column_name):
        if self.data is not None:
            if column_name in self.data.columns:
                average_value = self.data[column_name].mean()
                return f"The average value of {column_name} is {average_value}."
            else:
                return f"Error: Column '{column_name}' not found in the data."
        else:
            return "Error: No data loaded. Please load the data first."





   
   
   
    # Method to save the cleaned data to a new CSV file
    def save_cleaned_data(self, output_file_path):
        if self.data is not None:
            self.data.to_csv(output_file_path, index=False)
            return f"Cleaned data saved to {output_file_path}."
        else:
            return "Error: No data to save. Please load and clean the data first."