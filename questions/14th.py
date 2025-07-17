import pandas as pd

d = {'one': pd.Series([1,2,3],index=['a','b','c']),'two': pd.Series([1,2,3],index=['a','b','c'])}

df = pd.DataFrame(d)
df1 = pd.DataFrame(d,index=['d','b','a'])
df2 = pd.DataFrame(d,index=['d','a'], columns=['two','three'])
print(df)
print(df1)
print(df2)