# Import the pandas library, which is necessary for DataFrame operations.
import pandas as pd

# --- Creating a DataFrame from a List of Lists ---

# This method is useful when your data is in a simple tabular format, like a list of rows.

# We create a list where each inner list represents a single ROW in the DataFrame.
list_of_lists = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# We also need to define the column headers separately.
columns = ["Name", "Age", "City"]

# Use the pd.DataFrame() constructor to convert the list of lists into a DataFrame.
# The `data` parameter takes the list of lists, and the `columns` parameter takes the list of column headers.
df = pd.DataFrame(data=list_of_lists, columns=columns)

# Print the resulting DataFrame to display the structured data.
print("DataFrame created from a List of Lists:")
print(df)
