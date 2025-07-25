import pandas as pd

batsman = {
    "Name":["Sunil Pillai","Gaurav Sharma","Piyush Goal","Karthik Thakur"],
    "Score1":[90,65,70,80],
    "Score2": [80,45,90,76]
}

df = pd.DataFrame(batsman)
# df.to_excel('question.xlsx', index=False)


name = {
    1:"Laggan",
    2:"Tarre Zameen Par",
    3: "3 IDIOTS",
    4: "Dangal",
    5:"Andhadhun"
}
year = {
    1:2001,
    2:2007,
    3: 2009,
    4: 2016,
    5:2018
}
rating = {
    1:8.4,
    2:8.5,
    3: 8.4,
    4: 8.4,
    5:8.3
}
movie = {"Title":name,"Year":year,"rating":rating}
movieDf = pd.DataFrame(movie)
print(df)
print(movieDf)