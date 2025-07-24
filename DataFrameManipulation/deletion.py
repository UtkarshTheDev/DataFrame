import pandas as pd

students =["Neha","Manav","Mitu","Mike","Jamal"] 
data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        }

df = pd.DataFrame(data,index=students)

# Deleting Columns
del df['marks']

# Deleting Rows
df = df.drop('Manav')

print(df)