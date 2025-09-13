# Import the pandas library for creating and manipulating DataFrames.
import pandas as pd

# --- Extracting Rows from a DataFrame using .loc[] ---

# Define a list of student names to serve as the index (row labels).
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]

# Define the data for the DataFrame.
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
}

# Create the DataFrame with the specified data and custom index.
df = pd.DataFrame(data, index=students)

print("Original DataFrame:")
print(df)
print("\n" + "="*40 + "\n")


# The .loc[] accessor is the primary way to select rows and columns by their LABELS.
# The general syntax is: df.loc[row_labels, column_labels]

# --- 1. Extracting Specific Rows (and all their columns) ---

# To extract one or more specific rows, provide a list of their index labels.
# The colon ':' in the column position means "select all columns".
print("1. Extracting rows for 'Manav' and 'Mike' (all columns):")
specific_rows = df.loc[["Manav", "Mike"], :]
print(specific_rows)
print("\n" + "="*40 + "\n")

# If you are selecting all columns, you can omit the colon for slightly cleaner code:
# print(df.loc[["Manav", "Mike"]]) is equivalent to the above.


# --- 2. Extracting a Slice of Rows ---

# You can also select a range of rows using slicing with their labels.
# This will select all rows from 'Manav' to 'Mike', inclusive.
print("2. Extracting a slice of rows from 'Manav' to 'Mike':")
row_slice = df.loc["Manav":"Mike"] # The second argument (:) is implied
print(row_slice)
print("\n" + "="*40 + "\n")


# --- 3. Extracting Specific Rows AND Specific Columns ---

# To get a subset of the data based on both row and column labels,
# provide lists of labels for both arguments of .loc[].
print("3. Extracting the 'marks' column for 'Manav' and 'Mike':")
specific_data = df.loc[["Manav", "Mike"], ["marks"]]
print(specific_data)
print("\n" + "="*40 + "\n")

# You can also select multiple columns.
print("4. Extracting 'marks' and 'SPORTS' for 'Neha' and 'Jamal':")
more_specific_data = df.loc[["Neha", "Jamal"], ["marks", "SPORTS"]]
print(more_specific_data)