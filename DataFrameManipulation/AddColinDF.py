import pandas as pd

data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        "Students": ["Neha","Manav","Mitu","Mike","Jamal"]
        }

df = pd.DataFrame(data)

df["Book"] = [100,234,453,123,234]

print(df)

