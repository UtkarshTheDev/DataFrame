import pandas as pd

students =["Neha","Manav","Mitu","Mike","Jamal"] 
data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        }

df = pd.DataFrame(data,index=students)

# Row Extraction
# Usage: df_name.loc[["Rows","Name"],["Column","Name"]] 
print(df.loc[["Manav","Mike"],:]) # For All Columns of Specific Rows

# Row and Column Extraction Both
print(df.loc[["Manav","Mike"],["marks"]]) # For Specific Columns