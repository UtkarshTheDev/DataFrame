import pandas as pd

students =["Neha","Manav","Mitu","Mike","Jamal"] 
data = {
        "marks":[79.5,83.75,74,88.5,89],
        "SPORTS": ["CRICKET","BADMINTON","FOOTBALL","FOOTBALL","CRICKET"],
        }

df = pd.DataFrame(data,index=students)

# Provide Indexes of DF
indexes = df.index


# Provide Columns of DF
columns = df.columns

# Provides Both Rows and Columns of DF
axes = df.axes
# Provide DataTypes of DF
dtypes = df.dtypes

# Provide Size of DF
size = df.size

# Provide No. of Rows,Columns of DF
shape = df.shape

# Provide Values of DF
values = df.values

# True/False for DF is Empty or not
empty = df.empty

# Provide Dimension of DF
ndim = df.ndim

# Give the Transpose of DF
transpose = df.T


print(indexes,columns,axes,dtypes,size,shape,values,empty,ndim,transpose)