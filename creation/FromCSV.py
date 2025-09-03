# Import the pandas library, which is necessary for DataFrame operations.
import pandas as pd

# --- Creating a DataFrame from a CSV File ---

# This is one of the most common ways to create a DataFrame.
# The pd.read_csv() function is powerful and flexible.

# We specify the path to the CSV file.
# In this case, the file is in the same directory as the script.
csv_file_path = "creation/data/sample_data.csv"

# Use the pd.read_csv() function to read the CSV file and create a DataFrame.
# Pandas automatically uses the first row of the CSV file as the header (column names).
df = pd.read_csv(csv_file_path)

# Print the resulting DataFrame to display the structured data.
print(f"DataFrame created from {csv_file_path}:")
print(df)
