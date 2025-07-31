import pandas as pd

# Question1: Create a DataFrame from a dictionary where each key-value pair represents a cricketer's name and their total runs in ODI and Test matches.

# Solution

sampleData = {
    "Name": ["Sunil Pillai", "Gaurav Sharma", "Karthik Thakur"],
    "ODI": [100, 120,130],
    "Test": [200, 220,230]
}
df = pd.DataFrame(sampleData)
print(df)
print("\n" + "="*30 + "\n")

# (i) Add a new column named "Total" that contains the sum of ODI and Test runs for each cricketer. 
df["Total"] = df["ODI"] + df["Test"]
print(df)
print("\n" + "="*30 + "\n")

# (ii) Access the value at the second row and third column (i.e., ODI runs for the second cricketer).

print(df.at[2,"ODI"])

print("\n" + "="*30 + "\n")

# (iii) Add a new column named "City" that contains the city names for each cricketer.

df["City"] = ["New York", "Chicago", "Phoenix"]
print(df)
print("\n" + "="*30 + "\n")

# (iv) Update the Phoenix City Name with Delhi

df.at[2,"City"] = "Delhi"
print(df)
print("\n" + "="*30 + "\n")

# (v) Delete the "City" column.
# Only comment out when below code is commented because of mismatch of indexes and values due to deletion of column

# del df["City"]
# print(df)
# print("\n" + "="*30 + "\n")

# (vi) Delete the row with city Delhi
# Only comment out when below code is commented because of mismatch of indexes and values due to deletion of row

# df = df.drop("Delhi")
# print(df)
# print("\n" + "="*30 + "\n")

# (vii) Rename the column "Name" to "Crickter Name".

df.rename(columns={"Name":"Crickter Name"},inplace=True)
print(df)
print("\n" + "="*30 + "\n")

# (viii) Change the index of the DataFrame to "One", "Two", and "Three".

df.index = ["One","Two","Three"]
print(df)
print("\n" + "="*30 + "\n")