# Pandas DataFrame Resources 

Welcome to the Pandas DataFrame Resources! This project is a collection of beginner-friendly Python scripts designed to help you learn and practice the fundamentals of creating, manipulating, and inspecting [Pandas DataFrames](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe).

If you're new to data science or the Pandas library, this is the perfect place to start. Each script is a self-contained example focusing on a specific concept.

## 🚀 Getting Started

To use this project, you'll need Python and the Pandas library installed.

### Prerequisites

- Python 3.x
- Pandas

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/UtkarshTheDev/dataframe.git
    cd dataframe
    ```

2.  **Install Pandas:**
    If you don't have Pandas installed, you can install it using pip:
    ```bash
    pip install pandas
    ```

## 📂 Project Structure

This project is organized into several directories, each focusing on a different aspect of working with DataFrames.

```
.
├── attributes/         # Scripts demonstrating DataFrame attributes (properties)
├── creation/           # Scripts for creating DataFrames from various data structures
├── manipulation/       # Scripts for modifying DataFrames (adding, deleting, renaming)
│   └── extraction/     # Scripts for selecting and extracting data
└── questions/          # Solutions to specific data manipulation problems
```

## 📖 How to Use This Project

The best way to learn is by doing! Here’s a recommended path to follow:

### 1. Start with DataFrame Creation

Understanding how to get data *into* a DataFrame is the first step. The scripts in the `creation/` directory show you how to create a DataFrame from common Python objects.

-   **`creation/WithDict.py`**: Create a DataFrame from a dictionary of dictionaries.
-   **`creation/DictsofList.py`**: Create a DataFrame from a dictionary of lists (a very common method).
-   **`creation/ListOfDicts.py`**: Create a DataFrame from a list of dictionaries.

**For more details, see the [`creation/README.md`](creation/README.md).**

**Example from `DictsofList.py`:**
```python
import pandas as pd

# Data as a dictionary of lists
student_data = {
    "Roll No": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Math": [88, 76, 95, 69, 85],
}

# Create the DataFrame
df = pd.DataFrame(student_data)

print(df)
```

### 2. Explore DataFrame Attributes

Once you have a DataFrame, you'll want to know more about it—its size, shape, data types, etc. The `attributes/` directory contains a script that demonstrates how to access these properties.

-   **`attributes/attributes.py`**: Shows how to use attributes like `.shape`, `.columns`, `.index`, and `.dtypes`.

**For more details, see the [`attributes/README.md`](attributes/README.md).**

**Example from `attributes.py`:**
```python
# Assuming 'df' is the DataFrame from the previous example
print(f"The shape of the DataFrame is: {df.shape}")
print(f"The columns are: {df.columns}")
print(f"The data types are:\n{df.dtypes}")
```

### 3. Learn to Manipulate Data

This is where the real power of Pandas comes in. The scripts in the `manipulation/` directory show you how to modify your DataFrame.

-   **`manipulation/AddColinDF.py`**: Add a new column.
-   **`manipulation/deletion.py`**: Delete rows and columns.
-   **`manipulation/renaming.py`**: Rename columns and index labels.

**For more details, see the [`manipulation/README.md`](manipulation/README.md).**

### 4. Practice Data Extraction

A huge part of data analysis is selecting the specific data you need. The `manipulation/extraction/` subdirectory is dedicated to this.

-   **`extraction/extractingCol.py`**: Select one or more columns.
-   **`extraction/extractingRow.py`**: Select rows using `.loc[]` and `.iloc[]`.
-   **`extraction/individualExtraction.py`**: Get a single value using `.at[]` and `.iat[]`.

**For more details, see the [`manipulation/extraction/README.md`](manipulation/extraction/README.md).**

**Example from `extractingCol.py`:**
```python
# Assuming 'df' is our student DataFrame
# Extract the 'Name' and 'Math' columns
subset = df[['Name', 'Math']]

print(subset)
```

### 5. Test Your Knowledge

The `questions/` directory contains scripts that solve specific, practical problems. These are great for testing your understanding and learning new techniques. Feel free to try solving them yourself before looking at the solutions!

## 🤝 Contributing

Contributions are welcome! If you have an idea for a new example, find a bug, or want to improve the documentation, please feel free to open an issue or submit a pull request.

---

Happy learning!
