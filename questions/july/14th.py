# Import the pandas library, which is essential for working with Series and DataFrames.
import pandas as pd

# --- Exploring DataFrame Creation with Series and Custom Indexes/Columns ---

# This script demonstrates how the pandas DataFrame constructor behaves when given:
# 1. A dictionary of pandas Series.
# 2. Custom 'index' and 'columns' arguments that can realign, subset, or expand the data.

# First, create a dictionary 'd' where the values are pandas Series.
# A Series is a one-dimensional labeled array. Notice that both Series share the same index ('a', 'b', 'c').
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([1, 2, 3], index=['a', 'b', 'c'])
}

# --- Example 1: Default DataFrame Creation ---
# When we create a DataFrame from a dictionary of Series without specifying an index,
# pandas aligns the data based on the Series' indexes.
print("--- Example 1: Default DataFrame ---")
df = pd.DataFrame(d)
# Expected Output: The DataFrame will have columns 'one' and 'two',
# and the index will be the union of the Series indexes ('a', 'b', 'c').
print(df)
print("\n" + "="*30 + "\n")


# --- Example 2: Creating a DataFrame with a Custom Index ---
# Here, we provide a custom 'index' argument: ['d', 'b', 'a'].
# pandas will now create a DataFrame using ONLY the labels specified in this new index.
print("--- Example 2: DataFrame with Custom Index ['d', 'b', 'a'] ---")
df1 = pd.DataFrame(d, index=['d', 'b', 'a'])
# Expected Output:
# - Row 'd': This label does not exist in the original Series' indexes, so all values in this row will be NaN (Not a Number).
# - Row 'b': This label exists, so its data (2 for 'one', 2 for 'two') will be pulled in.
# - Row 'a': This label exists, so its data (1 for 'one', 1 for 'two') will be pulled in.
# - Row 'c' from the original Series is completely ignored because it's not in the new index list.
print(df1)
print("\n" + "="*30 + "\n")


# --- Example 3: Creating a DataFrame with Custom Index AND Columns ---
# Here, we provide both a custom 'index' and a custom 'columns' list.
print("--- Example 3: DataFrame with Custom Index and Columns ---")
df2 = pd.DataFrame(d, index=['d', 'a'], columns=['two', 'three'])
# Expected Output:
# - Index: The DataFrame will only have rows for labels 'd' and 'a'.
# - Columns: The DataFrame will only have columns for labels 'two' and 'three'.

# Let's analyze the result cell by cell:
# - Row 'd', Column 'two': 'd' is not in the original index, so the value is NaN.
# - Row 'd', Column 'three': 'd' is not in the original index AND 'three' is not an original column, so the value is NaN.
# - Row 'a', Column 'two': Row 'a' exists and column 'two' exists. The value from the 'two' Series at index 'a' is 1.
# - Row 'a', Column 'three': 'three' is a new column that doesn't exist in the input dictionary 'd', so all its values will be NaN.
print(df2)
