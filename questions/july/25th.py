# Import the pandas library, which is necessary for creating and working with DataFrames.
import pandas as pd

# --- Question/Example 1: Creating a DataFrame from a Dictionary of Lists ---

# This is a common scenario where you have data organized by columns.
# We create a dictionary where:
#   - Each KEY represents a COLUMN NAME (e.g., "Name", "Score1").
#   - Each VALUE is a LIST containing the data for that column.
# It's crucial that all lists have the same length to ensure the DataFrame is rectangular.
batsman = {
    "Name": ["Sunil Pillai", "Gaurav Sharma", "Piyush Goal", "Karthik Thakur"],
    "Score1": [90, 65, 70, 80],
    "Score2": [80, 45, 90, 76]
}

# Create the DataFrame from the 'batsman' dictionary.
# pandas automatically assigns a default integer index (0, 1, 2, 3).
df = pd.DataFrame(batsman)

# The following line is commented out, but it shows how to export a DataFrame to an Excel file.
# df.to_excel('question.xlsx', index=False)
# - 'question.xlsx': This is the name of the file that will be created.
# - index=False: This argument prevents pandas from writing the DataFrame's index (0, 1, 2, 3) as a column in the Excel file.
# To run this, you would need to have a library like 'openpyxl' installed (pip install openpyxl).

print("--- Batsman Scores DataFrame ---")
print(df)
print("\n" + "="*30 + "\n")


# --- Question/Example 2: Creating a DataFrame from a Dictionary of Dictionaries ---

# This method is useful when your data is structured with meaningful row and column labels.
# Here, we have separate dictionaries for movie titles, release years, and ratings.
# The keys (1, 2, 3, 4, 5) in these inner dictionaries will become the ROW INDEX labels.
name = {
    1: "Laggan",
    2: "Taare Zameen Par",
    3: "3 IDIOTS",
    4: "Dangal",
    5: "Andhadhun"
}
year = {
    1: 2001,
    2: 2007,
    3: 2009,
    4: 2016,
    5: 2018
}
rating = {
    1: 8.4,
    2: 8.5,
    3: 8.4,
    4: 8.4,
    5: 8.3
}

# Now, we create an outer dictionary 'movie'.
# The KEYS of this dictionary ("Title", "Year", "rating") will become the COLUMN NAMES.
# The VALUES (the name, year, and rating dictionaries) provide the data for each column.
movie = {"Title": name, "Year": year, "rating": rating}

# Create the DataFrame. pandas will align the data based on the keys (1, 2, 3, 4, 5) from the inner dictionaries.
movieDf = pd.DataFrame(movie)

print("---" + " Movie Details DataFrame ---")
print(movieDf)
