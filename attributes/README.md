# Understanding DataFrame Attributes in Pandas

A DataFrame in Pandas is a two-dimensional labeled data structure, similar to a spreadsheet or a SQL table. It has rows and columns, and each column can have a different data type.

Attributes of a DataFrame are like its properties. They don't perform any actions or calculations but provide useful information and metadata about the DataFrame itself. Think of them as asking the DataFrame, "What are you made of?" or "What do you look like?"

Below is a breakdown of the most common and useful DataFrame attributes, with examples based on the following sample DataFrame:

First, let's create a sample DataFrame to see these attributes in action.

```python
import pandas as pd

# Data for our DataFrame
data = {
    "marks": [79.5, 83.75, 74, 88.5, 89],
    "SPORTS": ["CRICKET", "BADMINTON", "FOOTBALL", "FOOTBALL", "CRICKET"],
}

# Row labels (index)
students = ["Neha", "Manav", "Mitu", "Mike", "Jamal"]

# Creating the DataFrame
df = pd.DataFrame(data, index=students)

print("Our Sample DataFrame:")
print(df)
```

This will output:
```
Our Sample DataFrame:
        marks     SPORTS
Neha    79.50    CRICKET
Manav   83.75  BADMINTON
Mitu    74.00   FOOTBALL
Mike    88.50   FOOTBALL
Jamal   89.00    CRICKET
```

---

## Core Attributes

### `df.index`
This attribute gives you the "row labels" of the DataFrame. It's like the names of the rows.

**Example:**
```python
print(df.index)
```
**Output:**
```
Index(['Neha', 'Manav', 'Mitu', 'Mike', 'Jamal'], dtype='object')
```

### `df.columns`
This attribute gives you the "column labels" of the DataFrame.

**Example:**
```python
print(df.columns)
```
**Output:**
```
Index(['marks', 'SPORTS'], dtype='object')
```

### `df.axes`
This returns a list containing both the row labels (`index`) and the column labels (`columns`).

**Example:**
```python
print(df.axes)
```
**Output:**
```
[Index(['Neha', 'Manav', 'Mitu', 'Mike', 'Jamal'], dtype='object'), Index(['marks', 'SPORTS'], dtype='object')]
```

### `df.dtypes`
This attribute tells you the data type of each column. This is very useful to check if your data is in the correct format (e.g., numbers are numeric, text is stored as objects).

**Example:**
```python
print(df.dtypes)
```
**Output:**
```
marks     float64
SPORTS     object
dtype: object
```
Here, `float64` means the `marks` column contains floating-point numbers, and `object` typically means the `SPORTS` column contains strings (text).

---

## Attributes for Size and Shape

### `df.size`
This gives you the total number of elements in the DataFrame. It's simply `(number of rows) * (number of columns)`.

**Example:**
```python
print(df.size)
```
**Output:**
```
10
```
(Our DataFrame has 5 rows and 2 columns, so 5 * 2 = 10)

### `df.shape`
This returns a tuple representing the dimensions of the DataFrame in the format `(rows, columns)`.

**Example:**
```python
print(df.shape)
```
**Output:**
```
(5, 2)
```
This tells us our DataFrame has 5 rows and 2 columns.

### `df.ndim`
This gives you the number of dimensions of the DataFrame. For any DataFrame, this will always be `2` (since it has rows and columns).

**Example:**
```python
print(df.ndim)
```
**Output:**
```
2
```

---

## Attributes for Data Inspection

### `df.values`
This attribute returns the actual data of the DataFrame as a NumPy array, without the row or column labels. This is useful when you need to perform numerical calculations that require a raw array of data.

**Example:**
```python
print(df.values)
```
**Output:**
```
[[79.5 'CRICKET']
 [83.75 'BADMINTON']
 [74.0 'FOOTBALL']
 [88.5 'FOOTBALL']
 [89.0 'CRICKET']]
```

### `df.empty`
This is a boolean attribute that returns `True` if the DataFrame is empty (has no data) and `False` otherwise.

**Example:**
```python
print(df.empty)
```
**Output:**
```
False
```
(Our DataFrame is not empty, so it returns `False`).

---

## Attribute for Reshaping

### `df.T`
The `.T` attribute transposes the DataFrame. This means it swaps the rows and columns. The rows of the original DataFrame become the columns of the new one, and vice versa.

**Example:**
```python
print(df.T)
```
**Output:**
```
             Neha      Manav      Mitu      Mike     Jamal
marks        79.5      83.75      74.0      88.5      89.0
SPORTS    CRICKET  BADMINTON  FOOTBALL  FOOTBALL   CRICKET
```
Notice how "marks" and "SPORTS" are now the row labels, and the student names are the column labels.

---
For a runnable script demonstrating all these attributes, you can still refer to the [attributes.py](attributes.py) file.