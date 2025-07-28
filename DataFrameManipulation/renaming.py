# Import the pandas library for DataFrame operations.
import pandas as pd

# --- Renaming Index and Columns in a DataFrame ---

# Set up the initial data and index for the DataFrame.
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
}

# Create the DataFrame.
df = pd.DataFrame(data, index=students)

# Print the original DataFrame to show its state before any changes.
print("Original DataFrame:")
print(df)
print("-" * 30)

# --- Renaming an Index Label ---

# To rename one or more index labels, use the df.rename() method with the 'index' parameter.
# The 'index' parameter takes a dictionary where:
#   - The KEY is the OLD index name you want to change (e.g., "Manav").
#   - The VALUE is the NEW index name you want to use (e.g., "Milkha").

print("Renaming index 'Manav' to 'Milkha'...")
# By default, rename() returns a *new* modified DataFrame.
# We must assign the result back to 'df' to save the change.
df = df.rename(index={"Manav": "Milkha"})

# To modify the DataFrame in-place without reassignment, you can use the inplace=True argument:
# df.rename(index={"Mitu": "Meetu"}, inplace=True)

# Print the DataFrame after renaming the index.
print("\nDataFrame after renaming index:")
print(df)
print("-" * 30)


# --- Renaming a Column Label ---

# To rename columns, you use the same df.rename() method, but with the 'columns' parameter.
# The 'columns' parameter also takes a dictionary where:
#   - The KEY is the OLD column name (e.g., "marks").
#   - The VALUE is the NEW column name (e.g., "Marks").

print("Renaming column 'marks' to 'Marks'...")
# Again, we assign the result back to 'df' to keep the change.
df = df.rename(columns={"marks": "Marks"})

# You can rename multiple columns at once by adding more key-value pairs to the dictionary.
# Example:
# df = df.rename(columns={"marks": "Final Marks", "SPORTS": "Favorite Sport"})

# Print the final DataFrame with both the index and column renamed.
print("\nDataFrame after renaming column:")
print(df)
