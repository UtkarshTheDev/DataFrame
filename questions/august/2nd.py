import pandas as pd

scores = {
    "Name": ["Sunil Pillai", "Gaurav Sharma", "Karthik Thakur"],
    "Score1": [100, 120,130],
    "Score2": [200, 220,230]
}
df = pd.DataFrame(scores)
print(df)
print("\n" + "="*30 + "\n")

# (i)
df["Total"] = df["Score1"] + df["Score2"]
print(df)
print("\n" + "="*30 + "\n")

# (ii)
print("Maximum Score1",df["Score1"].max())
print("Maximum Score2",df["Score2"].max())
print("\n" + "="*30 + "\n")

# (iii)
print(df)

print("\n" + "="*30 + "\n")
