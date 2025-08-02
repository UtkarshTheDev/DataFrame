import pandas as pd

# Question1: Create a DataFrame from a dictionary where each key-value pair represents a Student name and their marks in Score1 and Score2.

# Solution

scores = {
    "Name": ["Sunil Pillai", "Gaurav Sharma", "Karthik Thakur"],
    "Score1": [100, 120,130],
    "Score2": [200, 220,230]
}
df = pd.DataFrame(scores)
print(df)
print("\n" + "="*30 + "\n")

# (i) Add a new column named "Total" that contains the sum of Score1 and Score2 for each student.
df["Total"] = df["Score1"] + df["Score2"]
print(df)
print("\n" + "=k"*30 + "\n")

# (ii) Find the maximum score in Score1 and Score2.
print("Maximum Score1",df["Score1"].max())
print("Maximum Score2",df["Score2"].max())
print("\n" + "="*30 + "\n")

# (iii) Print the DataFrame after adding the "Total" column.
print(df)

print("\n" + "="*30 + "\n")
