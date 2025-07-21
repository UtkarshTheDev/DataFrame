import pandas as pd

data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        "Students": ["Neha","Manav","Mitu","Mike","Jamal"]
        }


df = pd.DataFrame(data)

# Row Extraction

print(df.loc[["marks","Students"],:])