# Import the pandas library, which is necessary for DataFrame operations.
import pandas as pd

# --- Creating a DataFrame from a List of Dictionaries ---

# This method is useful when your data is structured as a series of records or entries,
# where each record is a dictionary.

# We create a list where each element is a dictionary.
#   - Each dictionary in the list represents a single ROW in the DataFrame.
#   - The KEYS of the dictionaries become the COLUMN headers.
#   - The VALUES of the dictionaries become the data for each cell in that row.

# Note: pandas is smart enough to handle missing keys. If a dictionary is missing a key
# that exists in other dictionaries, pandas will fill that cell with 'NaN' (Not a Number).
listDict = [
    {"English": 200, "Maths": 499, "Science": 430},  # This dictionary will become the first row (index 0)
    {"English": 320, "Maths": 430, "Science": 402},  # This will be the second row (index 1)
    {"English": 400, "Maths": 129, "Science": 439}   # This will be the third row (index 2)
]

# Use the pd.DataFrame() constructor to convert the list of dictionaries into a DataFrame.
# pandas will automatically infer the column names from the dictionary keys.
df = pd.DataFrame(listDict)

# By default, a new integer-based index (0, 1, 2) is created for the rows.

# Print the resulting DataFrame to display the structured data.
print("DataFrame created from a List of Dictionaries:")
print(df)

# Example of how pandas handles missing data with this method:
# listDict_with_missing_data = [
#     {"Name": "Alice", "Age": 25},
#     {"Name": "Bob", "Age": 30, "City": "New York"}, # This dict has an extra key "City"
#     {"Name": "Charlie"} # This dict is missing the "Age" key
# ]
# df_missing = pd.DataFrame(listDict_with_missing_data)
# print("\nDataFrame with missing values:")
# print(df_missing)
# In the output, you would see NaN for Alice's city and Charlie's age.
