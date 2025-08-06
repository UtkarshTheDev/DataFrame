# Import the pandas library for DataFrame functionality.
import pandas as pd

# --- Accessing Individual Values (Scalars) in a DataFrame ---

# Set up the sample DataFrame with a custom index.
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
}
df = pd.DataFrame(data, index=students)

print("Original DataFrame:")
print(df)
print("\n" + "="*40 + "\n")


# There are several ways to access a single value from a DataFrame.
# These methods are highly optimized for retrieving just one element.

# --- Method 1: Chained Indexing (less recommended) ---
# You can select a column first (which returns a Series) and then select an item from that Series by its index label.
# While this works, it can be less efficient than .at or .iat because it involves creating an intermediate Series object.
print("1. Accessing 'Manav's marks using chained indexing:")
indValue = df['marks']['Manav']
print(f"Value: {indValue}")
print(f"Type: {type(indValue)}") # Note: The type is a numpy float, not a pandas object.
print("\n" + "="*40 + "\n")


# --- Method 2: Using the .at[] Accessor (Label-Based) ---
# This is the standard, recommended way to access a single value by its LABEL.
# It is very fast and explicit.
# Syntax: df.at[row_label, column_label]
print("2. Accessing 'Manav's marks using .at[]:")
at_value = df.at['Manav', "marks"]
print(f"Value: {at_value}")
print(f"Type: {type(at_value)}")
print("\n" + "="*40 + "\n")


# --- Method 3: Using the .iat[] Accessor (Integer-Position-Based) ---
# This is the recommended way to access a single value by its INTEGER POSITION (like in a 2D array).
# It is also extremely fast.
# Syntax: df.iat[row_position, column_position]
# Remember that positions are 0-indexed.
print("3. Accessing the value at row 0, column 1 using .iat[]:")
# Row 0 is 'Neha', Column 1 is 'SPORTS'.
iat_value = df.iat[0, 1]
print(f"Value at position (0, 1) is: {iat_value} (Neha's sport)")

# Let's get Manav's marks using .iat[]
# Manav is at row position 1, marks is at column position 0.
iat_value_marks = df.iat[1, 0]
print(f"Value at position (1, 0) is: {iat_value_marks} (Manav's marks)")
print(f"Type: {type(iat_value)}")
print("\n" + "="*40 + "\n")

# Summary:
# - Use .at[row_label, col_label] for fast, explicit access by label.
# - Use .iat[row_pos, col_pos] for fast, explicit access by integer position.
# - Avoid chained indexing (like df['col']['row']) in performance-critical code, although it works for simple cases.
