import pandas as pd

"""
Row Parser Script
Author: Kevin Fox
Date: June 15, 2024

Description:
This script processes an Excel file by selecting every 22nd row (including the header) and saves the result to a CSV file.
It uses the pandas library for data manipulation.

Steps:
1. Reads an Excel file provided by the user.
2. Filters the rows to include the header and every 22nd row.
3. Saves the filtered data to a new CSV file with '_filtered' added to the original file name.
"""

# Prompt the user to enter the file path of the Excel file to process
file_path = input('Enter the file path: ').strip('"')

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(file_path)

# Filter the DataFrame to include the header and every 22nd row
df_filtered = pd.concat([df.iloc[0:0], df.iloc[0::22]], ignore_index=True)

# Define the file path for the new CSV file
csv_file_path = file_path.replace('.xlsm', '_filtered.csv')

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv(csv_file_path, index=False)
