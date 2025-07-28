# Import the pandas library, which is essential for working with DataFrames.
import pandas as pd

# Define a list of student names that will be used as the index for our DataFrame.
# An index is like a label for each row, making data retrieval easier and more intuitive.
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]

# Create a dictionary to hold the data for our DataFrame.
# The keys of the dictionary will become the column names,
# and the values (lists of data) will populate the rows.
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],  # Column for student marks
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],  # Column for the sport each student plays
}

# Create a DataFrame using the pandas DataFrame constructor.
# We pass our 'data' dictionary and specify 'students' as the index.
df = pd.DataFrame(data, index=students)

# --- DataFrame Attributes ---
# Attributes are properties of the DataFrame that give us information about it.

# Get the index (row labels) of the DataFrame.
indexes = df.index
print("Index:", indexes)

# Get the columns (column labels) of the DataFrame.
columns = df.columns
print("Columns:", columns)

# Get a list containing both the index (rows) and columns.
# It returns a list where the first element is the index and the second is the columns.
axes = df.axes
print("Axes:", axes)

# Get the data types of each column. This is useful for understanding what kind of data each column holds (e.g., float, object).
dtypes = df.dtypes
print("DataTypes:", dtypes)

# Get the total number of elements in the DataFrame (rows * columns).
size = df.size
print("Size:", size)

# Get a tuple representing the dimensions of the DataFrame (number of rows, number of columns).
shape = df.shape
print("Shape:", shape)

# Get the actual data of the DataFrame as a NumPy array.
# This is useful when you need to perform numerical computations.
values = df.values
print("Values:", values)

# Check if the DataFrame is empty. Returns True if it has no data, False otherwise.
empty = df.empty
print("Is Empty:", empty)

# Get the number of dimensions of the DataFrame. For a DataFrame, this is always 2.
ndim = df.ndim
print("Number of Dimensions:", ndim)

# Get the transpose of the DataFrame.
# The transpose swaps the rows and columns. Rows become columns and columns become rows.
transpose = df.T
print("Transpose:\n", transpose)
