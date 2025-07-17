import pandas as pd

yr1 = {"Qtr1":4500,"Qtr2":465,"Q3":5700}
yr2 = {"Qtr2":4000,"A":892,"Qtr4":5700}

sales = {"one":yr1,"two":yr2}

df = pd.DataFrame(sales)

# print(sales[yr1,yr2])
print(df)