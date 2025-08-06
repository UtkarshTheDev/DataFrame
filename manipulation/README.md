# Manipulating a Pandas DataFrame

Once a DataFrame is created, the next step is often to modify it to fit your analysis needs. This can involve adding, deleting, or renaming columns and rows. This guide covers these fundamental manipulation techniques.

---

## 1. Adding a New Column

You can easily add a new column to an existing DataFrame. The new column must have the same number of elements as the number of rows in the DataFrame.

### Code Example: Assigning a List to a New Column

This is the most direct method. You specify the new column name as if it were a dictionary key and assign a list of values to it.

```python
import pandas as pd

# Initial DataFrame
data = {
    "Student": ["Neha", "Manav", "Mitu", "Mike", "Jamal"],
    "Marks": [79, 83, 74, 88, 89]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Add a new 'Sports' column
df["Sports"] = ["Cricket", "Badminton", "Football", "Football", "Cricket"]

print("\nDataFrame after adding 'Sports' column:")
print(df)
```

### Output:

```
Original DataFrame:
   Student  Marks
0     Neha     79
1    Manav     83
2     Mitu     74
3     Mike     88
4    Jamal     89

DataFrame after adding 'Sports' column:
   Student  Marks     Sports
0     Neha     79    Cricket
1    Manav     83  Badminton
2     Mitu     74   Football
3     Mike     88   Football
4    Jamal     89    Cricket
```

**Other useful methods for adding columns include:**
-   `df.assign()`: Creates a *new* DataFrame with the added column, leaving the original unchanged.
-   `df.insert()`: Adds a column at a specific integer location.

---

## 2. Deleting Rows and Columns

Removing unnecessary data is a critical step in data cleaning. Pandas provides the powerful `drop()` method for this.

### Deleting a Column

To remove a column, use `df.drop()` and specify the column name and `axis=1`.

```python
# Continuing with the previous DataFrame...

# Drop the 'Marks' column
# axis=1 tells pandas to look for a column label
# inplace=True modifies the DataFrame directly without needing reassignment
df.drop('Marks', axis=1, inplace=True)

print("\nDataFrame after dropping 'Marks' column:")
print(df)
```

### Output:
```
DataFrame after dropping 'Marks' column:
   Student     Sports
0     Neha    Cricket
1    Manav  Badminton
2     Mitu   Football
3     Mike   Football
4    Jamal    Cricket
```

### Deleting a Row

To remove a row, use `df.drop()` and specify the row\'s index label. The default axis is `0` (rows), so you don\'t need to specify it.

```python
# Let\'s create a DataFrame with student names as the index
data = {
    "Marks": [79, 83, 74],
    "Sports": ["Cricket", "Badminton", "Football"]
}
index = ["Neha", "Manav", "Mitu"]
df_row_del = pd.DataFrame(data, index=index)
print("\nOriginal DataFrame for row deletion:")
print(df_row_del)

# Drop the row with index 'Manav'
df_row_del.drop('Manav', inplace=True)

print("\nDataFrame after dropping 'Manav' row:")
print(df_row_del)
```

### Output:
```
Original DataFrame for row deletion:
       Marks     Sports
Neha      79    Cricket
Manav     83  Badminton
Mitu      74   Football

DataFrame after dropping 'Manav' row:
      Marks   Sports
Neha     79  Cricket
Mitu     74 Football
```

---

## 3. Renaming Columns and Index

You can rename columns or index labels to be more descriptive using the `rename()` method.

### Code Example: Renaming

The `rename()` method takes a dictionary where the keys are the old names and the values are the new names.

```python
import pandas as pd

students = ["Neha", "Manav", "Mitu"]
data = {
    "marks": [79, 83, 74],
    "SPORTS": ["Cricket", "Badminton", "Football"]
}
df_rename = pd.DataFrame(data, index=students)
print("\nOriginal DataFrame for renaming:")
print(df_rename)

# Rename the index 'Mitu' to 'Meetu' and the column 'marks' to 'Final_Marks'
df_renamed = df_rename.rename(
    index={"Mitu": "Meetu"},
    columns={"marks": "Final_Marks", "SPORTS": "Favorite_Sport"}
)

print("\nDataFrame after renaming:")
print(df_renamed)
```

### Output:
```
Original DataFrame for renaming:
       marks     SPORTS
Neha      79    Cricket
Manav     83  Badminton
Mitu      74   Football

DataFrame after renaming:
        Final_Marks Favorite_Sport
Neha             79        Cricket
Manav            83      Badminton
Meetu            74       Football
```

```