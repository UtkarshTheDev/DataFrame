# Creating a Pandas DataFrame

A DataFrame is the most fundamental data structure in the [Pandas](https://pandas.pydata.org/) library. It's a 2-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Think of it as a spreadsheet or a SQL table, but with the full power of Python.

This guide covers the most common methods for creating a DataFrame from scratch.

---

## 1. From a Dictionary of Lists

This is arguably the most common and intuitive way to create a DataFrame. You start with a Python dictionary where each key-value pair represents a column.

-   **Keys** become the **column names**.
-   **Values** (which are lists) become the **data for each column**.

**Key Requirement:** All lists must have the same number of elements to ensure the DataFrame is rectangular.

### Code Example:

```python
# Import the pandas library
import pandas as pd

# Define the data as a dictionary of lists
student_data = {
    "Roll No": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Math": [88, 76, 95, 69, 85],
    "Science": [91, 82, 89, 74, 90]
}

# Create the DataFrame
df = pd.DataFrame(student_data)

# Print the result
print(df)
```

### Output:

```
   Roll No     Name  Math  Science
0        1    Alice    88       91
1        2      Bob    76       82
2        3  Charlie    95       89
3        4    Diana    69       74
4        5    Ethan    85       90
```

---

## 2. From a List of Dictionaries

This method is very useful when your data is structured as a collection of records, where each record is a dictionary.

-   Each **dictionary** in the list represents a **row**.
-   The **keys** of the dictionaries become the **column names**.
-   The **values** of the dictionaries populate the cells for that row.

**Flexible Feature:** Pandas handles missing data gracefully. If one dictionary is missing a key that others have, the corresponding cell in the DataFrame will be filled with `NaN` (Not a Number).

### Code Example:

```python
# Import the pandas library
import pandas as pd

# Define the data as a list of dictionaries
exam_scores = [
    {"Subject": "Math", "Score": 92, "Hours_Studied": 10},
    {"Subject": "Science", "Score": 88}, # Missing 'Hours_Studied'
    {"Subject": "English", "Score": 95, "Hours_Studied": 8}
]

# Create the DataFrame
df = pd.DataFrame(exam_scores)

# Print the result
print(df)
```

### Output:

```
   Subject  Score  Hours_Studied
0     Math     92           10.0
1  Science     88            NaN  <-- NaN where data was missing
2  English     95            8.0
```

---

## 3. From a Dictionary of Dictionaries (or Series)

This method allows you to specify labels for both columns and rows (the index) right at creation.

-   The **keys** of the outer dictionary become the **column names**.
-   The **inner dictionaries** (or Pandas Series) provide the data for each column.
-   The **keys** of the inner dictionaries become the **row index labels**.

Pandas will align the data based on the inner dictionary keys (the index). If a row label exists in one inner dictionary but not another, `NaN` will be used to fill the gap.

### Code Example:

```python
# Import the pandas library
import pandas as pd

# Define the data as a dictionary of dictionaries
quarterly_sales = {
    "Product_A": {"Q1": 1500, "Q2": 1600, "Q3": 1800},
    "Product_B": {"Q1": 2100, "Q2": 2400, "Q4": 2900} # Note Q3 is missing, Q4 is extra
}

# Create the DataFrame
df = pd.DataFrame(quarterly_sales)

# Print the result
print(df)
```

### Output:

```
    Product_A  Product_B
Q1     1500.0     2100.0
Q2     1600.0     2400.0
Q3     1800.0        NaN  <-- NaN because Q3 is missing for Product_B
Q4        NaN     2900.0  <-- NaN because Q4 is missing for Product_A
```

---

## 4. From a List of Lists

This method is useful when your data is in a simple tabular format, like a list of rows.

-   Each **inner list** represents a **row**.
-   You must provide a separate list of **column names**.

### Code Example:

```python
# Import the pandas library
import pandas as pd

# Define the data as a list of lists
list_of_lists = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Define the column headers
columns = ["Name", "Age", "City"]

# Create the DataFrame
df = pd.DataFrame(data=list_of_lists, columns=columns)

# Print the result
print(df)
```

### Output:

```
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
```

---

## 5. From a CSV File

This is one of the most common and powerful ways to create a DataFrame. The `pd.read_csv()` function is highly versatile.

-   Pandas automatically uses the **first row** of the CSV as the **column headers**.
-   It infers data types automatically.

### Code Example:

First, create a sample CSV file named `sample_data.csv` in the `creation/data` directory:

```csv
Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago
```

Now, read the CSV file using pandas:

```python
# Import the pandas library
import pandas as pd

# Specify the path to the CSV file
csv_file_path = "creation/sample_data.csv"

# Create the DataFrame using read_csv()
df = pd.read_csv(csv_file_path)

# Print the result
print(df)
```

### Output:

```
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
```
