# Import the pandas library to work with DataFrames.
import pandas as pd

# --- Deleting Rows and Columns from a DataFrame ---

# Define a list of student names to be used as the DataFrame index.
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]

# Define the data for the DataFrame.
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
}

# Create the DataFrame with the specified data and index.
df = pd.DataFrame(data, index=students)

# Print the original DataFrame to see its initial state.
print("Original DataFrame:")
print(df)
print("-" * 30)

# --- Deleting Columns ---

# Method 1: Using the 'del' keyword (Python's standard delete operator).
# This is a simple and direct way to remove a column.
# The change happens in-place, meaning the original DataFrame is modified directly.
print("Deleting the 'marks' column using 'del'...")
del df['marks']

# After this line, the 'marks' column is permanently removed from df.
print("DataFrame after deleting 'marks' column:")
print(df)
print("-" * 30)

# Method 2: Using the df.drop() method for columns.
# This is a more flexible method provided by pandas.
# To delete columns, you must specify axis=1.
# By default, drop() returns a *new* DataFrame. To modify the original, use inplace=True.
#
# Example:
# df.drop('SPORTS', axis=1, inplace=True)
# print("\nDataFrame after dropping 'SPORTS' column with drop():")
# print(df)


# --- Deleting Rows ---

# To delete rows, you use the df.drop() method.
# By default, drop() works on rows (axis=0), so you just need to provide the index label of the row to delete.
print("Deleting the row with index 'Manav' using drop()...")

# The drop() method returns a new DataFrame without the specified row.
# We need to assign the result back to 'df' to update it.
df = df.drop('Manav')

# Alternatively, you could use inplace=True to modify the DataFrame directly without reassignment:
# df.drop('Mitu', inplace=True)

# You can also drop multiple rows at once by passing a list of index labels:
# df = df.drop(['Mitu', 'Jamal'])

# Print the final DataFrame after all deletions.
print("Final DataFrame after deleting the 'Manav' row:")
print(df)
