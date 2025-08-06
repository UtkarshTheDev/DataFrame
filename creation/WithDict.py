# Import the pandas library to use its DataFrame features.
import pandas as pd

# --- Creating a DataFrame from a Dictionary of Dictionaries ---

# This method is useful for creating a DataFrame where both the rows and columns
# have meaningful labels (indexes and column names).

# Create inner dictionaries. Each dictionary will represent a COLUMN in the DataFrame.
#   - The KEYS of the inner dictionaries ("Qtr1", "Qtr2", etc.) will become the ROW INDEX labels.
#   - The VALUES of the inner dictionaries (4500, 465, etc.) will be the data values.
yr1 = {"Qtr1": 4500, "Qtr2": 465, "Q3": 5700}
yr2 = {"Qtr2": 4000, "A": 892, "Qtr4": 5700} # Note the different keys here ("A", "Qtr4")

# Create an outer dictionary to hold the inner dictionaries.
#   - The KEYS of this outer dictionary ("one", "two") will become the COLUMN NAMES.
#   - The VALUES of this outer dictionary (the yr1, yr2 dictionaries) will provide the data for those columns.
sales = {"one": yr1, "two": yr2}

# Create the DataFrame using the pd.DataFrame() constructor.
# pandas aligns the data based on the keys from the inner dictionaries (which become the index).
# If a key (like "Qtr1") exists in one inner dictionary but not another,
# pandas will place NaN (Not a Number) in the corresponding cell for the column where it's missing.
df = pd.DataFrame(sales)

# The commented-out line below would cause an error because it's not the correct way to access dictionary values.
# print(sales[yr1,yr2])

# Print the resulting DataFrame.
# Observe how pandas handles the union of all keys from the inner dictionaries ("Qtr1", "Qtr2", "Q3", "A", "Qtr4")
# to form the final index, and fills missing values with NaN.
print("DataFrame created from a Dictionary of Dictionaries:")
print(df)

# Expected Output:
#       one     two
# A     NaN   892.0  <-- "A" was only in yr2, so it's NaN in column "one"
# Q3   5700.0     NaN  <-- "Q3" was only in yr1, so it's NaN in column "two"
# Qtr1 4500.0     NaN  <-- "Qtr1" was only in yr1
# Qtr2  465.0  4000.0  <-- "Qtr2" was in both, so it has values for both columns
# Qtr4    NaN  5700.0  <-- "Qtr4" was only in yr2
