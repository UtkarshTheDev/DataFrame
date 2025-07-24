import pandas as pd

students =["Neha","Manav","Mitu","Mike","Jamal"] 
data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        }

df = pd.DataFrame(data,index=students)

# Renaming Index
df = df.rename(index={"Manav":"Milkha"})

# Renaming Columns
df = df.rename(columns={"marks":"Marks"})

print(df)