import pandas as pd

data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        "Students": ["Neha","Manav","Mitu","Mike","Jamal"]
        }


df = pd.DataFrame(data)

# Normal Extraction
print(df["SPORTS"])


# Multiple Column Extraction

print(df[["SPORTS","Students"]])

# Multiple Column Extraction with Range

# print(df["marks":"SPORTS"])