# Import the pandas library, which is fundamental for DataFrame operations.
import pandas as pd

# --- Extracting Columns from a DataFrame ---

# First, create a sample DataFrame to demonstrate column extraction.
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
    "Students": ["Neha", "Manav", "Mitu", "Mike", "Jamal"]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "="*40 + "\n")


# --- Method 1: Basic Extraction using Bracket Notation ---

# To extract a single column, you can use dictionary-like key access.
# The result is a pandas Series, which is like a single column of data.
print("1. Extracting a single column ('SPORTS'):")
sports_column = df["SPORTS"]
print(type(sports_column)) # This will show <class 'pandas.core.series.Series'>
print(sports_column)
print("\n" + "="*40 + "\n")


# --- Method 2: Extracting Multiple Columns ---

# To extract multiple columns, you pass a list of column names inside the brackets.
# The result is a new DataFrame containing only the specified columns.
print("2. Extracting multiple columns ('SPORTS' and 'Students'):")
subset_df = df[["SPORTS", "Students"]]
print(type(subset_df)) # This will show <class 'pandas.core.frame.DataFrame'>
print(subset_df)
print("\n" + "="*40 + "\n")


# --- Method 3: Extraction using the .loc[] Accessor ---
# .loc is a powerful label-based accessor for selecting data.
# The syntax is df.loc[row_labels, column_labels]

# To select all rows and specific columns:
# The colon ':' means "select all" for the rows.
# The list of strings specifies the columns you want.
print("3. Extracting 'marks' and 'SPORTS' columns using .loc[]:")
loc_extract = df.loc[:, ["marks", "SPORTS"]]
print(loc_extract)
print("\n" + "="*40 + "\n")

# A common mistake is trying to slice columns by name directly like df["marks":"SPORTS"].
# This syntax does NOT work for selecting a range of columns like it does for rows with .loc.
# The line below will result in a KeyError because pandas tries to find a row label named "marks"
# and slice up to a row named "SPORTS", which doesn't work this way for columns.
try:
    print("4. Attempting to slice columns by name (this will fail):")
    df["marks":"SPORTS"]
except KeyError as e:
    print(f"As expected, this failed with a KeyError: {e}")
    print("This syntax is for slicing rows by label, not columns.")

# The correct way to select a range of columns is with .loc:
print("\nCorrect way to select a range of columns using .loc:")
# This selects all rows (:) and columns from 'marks' through to 'Students'
column_range = df.loc[:, 'marks':'Students']
print(column_range)
