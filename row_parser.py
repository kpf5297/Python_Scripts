# Import the pandas library, which is a powerful tool for data analysis and manipulation.
import pandas as pd

# Ask the user to input the file path of the Excel file they want to process.
# The input function captures user input as a string.
# .strip('"') removes any double quotes from the input, which can be added by some users inadvertently.
file_path = input('Enter the file path: ').strip('"')

# Load the Excel file into a pandas DataFrame. A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# pd.read_excel() is a function that reads Excel files.
# file_path is the location of the file to read, as provided by the user.
df = pd.read_excel(file_path)

# Filter the rows of the DataFrame.
# pd.concat() is used to concatenate pandas objects. Here it combines two selections from the original DataFrame:
# df.iloc[0:0] selects no rows but keeps the column headers.
# df.iloc[0::22] selects every 22nd row starting from the first row (index 0).
# ignore_index=True resets the index to the default integer index.
# The result is a new DataFrame that includes the header row and every 21st row after the first data row.
df_filtered = pd.concat([df.iloc[0:0], df.iloc[0::22]], ignore_index=True)

# Define the file path for the new CSV file. 
# The .replace() function changes the '.xlsm' extension of the original file path to '_filtered.csv', indicating that this file is a filtered version of the original.
csv_file_path = file_path.replace('.xlsm', '_filtered.csv')

# Save the filtered DataFrame to a new CSV file.
# to_csv() is a function that writes the DataFrame to a comma-separated values (csv) file.
# csv_file_path is the destination file path.
# index=False means that the index (row labels) will not be written to the file. This keeps the file clean if you don't need the index.
df_filtered.to_csv(csv_file_path, index=False)
