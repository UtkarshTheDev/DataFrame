# Extracting Data from a Pandas DataFrame

Extracting specific pieces of data—whether they are columns, rows, or individual values—is a core part of data analysis. Pandas provides a powerful and flexible set of tools for this purpose, primarily centered around indexing (`[]`) and the optimized accessors `.loc[]`, `.iloc[]`, `.at[]`, and `.iat[]`.

This guide will walk you through the essential methods for selecting data.

---

## 1. Extracting Columns

This is one of the most common operations. You might want to work with only a subset of the columns in your DataFrame.

### Extracting a Single Column

To select a single column, use bracket notation `[]` with the column's name. This returns a Pandas **Series**.

```python
import pandas as pd

data = {
    "Student": ["Neha", "Manav", "Mitu"],
    "Marks": [85, 92, 78],
    "Subject": ["Math", "Science", "English"]
}
df = pd.DataFrame(data)

# Extract the 'Marks' column
marks_series = df['Marks']

print(marks_series)
print(type(marks_series))
```
**Output:**
```
0    85
1    92
2    78
Name: Marks, dtype: int64
<class 'pandas.core.series.Series'>
```

### Extracting Multiple Columns

To select multiple columns, pass a **list of column names** inside the brackets `[]`. This returns a new **DataFrame**.

```python
# Extract 'Student' and 'Subject' columns
subset_df = df[['Student', 'Subject']]

print(subset_df)
print(type(subset_df))
```
**Output:**
```
  Student  Subject
0    Neha     Math
1   Manav  Science
2    Mitu  English
<class 'pandas.core.frame.DataFrame'>
```

---

## 2. Extracting Rows using `.loc[]`

The `.loc[]` accessor is the primary tool for **label-based** selection, meaning you select data based on the **index labels** (and column labels).

### Setting up a Labeled Index

For `.loc[]` to be most effective, it's best to have a meaningful index.

```python
# Set the 'Student' column as the index
df.set_index('Student', inplace=True)
print("DataFrame with 'Student' as index:")
print(df)
```
**Output:**
```
DataFrame with 'Student' as index:
         Marks  Subject
Student
Neha        85     Math
Manav       92  Science
Mitu        78  English
```

### Extracting a Single Row

Provide the index label to `.loc[]`. This returns a Series.
```python
# Extract the row for 'Manav'
manav_row = df.loc['Manav']
print("\nRow for Manav:")
print(manav_row)
```
**Output:**
```
Row for Manav:
Marks         92
Subject    Science
Name: Manav, dtype: object
```

### Extracting Multiple Rows

Provide a list of index labels to `.loc[]`. This returns a DataFrame.
```python
# Extract rows for 'Neha' and 'Mitu'
neha_mitu_rows = df.loc[['Neha', 'Mitu']]
print("\nRows for Neha and Mitu:")
print(neha_mitu_rows)
```
**Output:**
```
Rows for Neha and Mitu:
         Marks  Subject
Student
Neha        85     Math
Mitu        78  English
```

### Extracting a Slice of Rows
You can select a range of rows by label. The slice is inclusive of both the start and end labels.
```python
# Extract all rows from 'Manav' to 'Mitu'
row_slice = df.loc['Manav':'Mitu']
print("\nSlice of rows from Manav to Mitu:")
print(row_slice)
```
**Output:**
```
Slice of rows from Manav to Mitu:
         Marks  Subject
Student
Manav       92  Science
Mitu        78  English
```

---

## 3. Extracting Individual Values (Scalars)

When you need to get just a single value from a DataFrame, using the optimized accessors `.at[]` (for labels) or `.iat[]` (for integer positions) is the most efficient method.

### Using `.at[]` for Label-Based Selection

This is the fastest way to get a single value when you know the row and column labels.

```python
# Get the 'Marks' for the student 'Manav'
manav_marks = df.at['Manav', 'Marks']
print(f"\nManav's Marks: {manav_marks}")
```
**Output:**
```
Manav's Marks: 92
```

### Using `.iat[]` for Integer-Position-Based Selection

This is the fastest way to get a single value when you know the integer position (row and column number, starting from 0).

```python
# Get the value at row position 2, column position 1
# Row 2 -> 'Mitu', Column 1 -> 'Subject'
mitu_subject = df.iat[2, 1]
print(f"\nValue at (2, 1): {mitu_subject}")
```
**Output:**
```
Value at (2, 1): English
```
