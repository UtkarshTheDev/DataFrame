# Import the pandas library, which is essential for working with DataFrames.
import pandas as pd

# --- Adding a New Column to a DataFrame ---

# First, let's create an initial DataFrame to work with.
# We'll use a dictionary of lists, a common method for DataFrame creation.
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
    "Students": ["Neha", "Manav", "Mitu", "Mike", "Jamal"]
}

# Create the DataFrame from the dictionary.
df = pd.DataFrame(data)

# Print the original DataFrame to see its initial state.
print("Original DataFrame:")
print(df)
print("-" * 30) # Separator for clarity

# To add a new column to an existing DataFrame, you can use dictionary-like assignment syntax.
# df['NewColumnName'] = [list_of_values]

# The list of values must have the same number of elements as the number of rows in the DataFrame.
# In this case, our DataFrame has 5 rows, so we need a list with 5 values.

# Let's add a new column named "Book" with a list of book IDs or numbers.
df["Book"] = [100, 234, 453, 123, 234]

# Now, the DataFrame 'df' is updated in place with the new "Book" column.

# Print the modified DataFrame to see the newly added column.
print("DataFrame after adding the 'Book' column:")
print(df)

# --- Alternative ways to add columns ---
# 1. Using df.assign(): This method creates a *new* DataFrame with the added column,
#    leaving the original DataFrame unchanged. It's useful for chaining operations.
#
#    df_new = df.assign(Gadgets=[5, 4, 3, 2, 1])
#    print("\nNew DataFrame created with df.assign():")
#    print(df_new)
#    print("\nOriginal df remains unchanged:")
#    print(df)

# 2. Using df.insert(): This allows you to add a new column at a specific location (index).
#
#    # df.insert(loc, column_name, values)
#    # Let's insert a 'City' column at the second position (index 1)
#    df.insert(1, "City", ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"])
#    print("\nDataFrame after inserting 'City' column at index 1:")
#    print(df)