import pandas as pd

students =["Neha","Manav","Mitu","Mike","Jamal"] 
data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        }

df = pd.DataFrame(data,index=students)


# Acess Individual value

indValue = df.marks['Manav']
print(indValue)

# Access Using at
df.at['Manav',"marks"]

# Accessin using iat
df.iat[0,1]