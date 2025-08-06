# Import the pandas library, which is the foundation for creating and working with DataFrames.
import pandas as pd

# --- Creating a DataFrame from a Dictionary of Lists ---

# This is one of the most common ways to create a DataFrame.
# We define a dictionary where:
#   - Each KEY is a string that will become a COLUMN NAME (e.g., "Roll No", "Name").
#   - Each VALUE is a LIST of data points that will populate the rows for that column.

# Important: All lists in the dictionary must have the same length.
# If they don't, pandas will raise an error because columns must have an equal number of rows.

data = {
    "Roll No": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Math": [88, 76, 95, 69, 85],
    "Science": [91, 82, 89, 74, 90],
    "English": [84, 79, 92, 81, 87],
    "History": [78, 85, 88, 73, 80],
    "Computer Science": [93, 89, 97, 88, 92]
}

# Use the pd.DataFrame() constructor to create the DataFrame from our dictionary.
# pandas automatically understands that the keys are column headers and the lists are the column data.
df = pd.DataFrame(data)

# By default, pandas will create a simple integer-based index (0, 1, 2, 3, 4).
# You could set a specific column as the index later if needed, for example, by using df.set_index("Roll No").

# Print the resulting DataFrame to see the structured table.
print("DataFrame created from a Dictionary of Lists:")
print(df)
