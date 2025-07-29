import pandas as pd

# Question1: Create a DataFrame from a list of dictionaries where each dictionary represents a product and its price.

# Solution
products = [
    {"Product": "Laptop","Price":60000},
    {"Product": "Mobile","Price":20000},
    {"Product": "Tablet","Price":15000},
    {"Product": "Monitor","Price":15000}
] 
df = pd.DataFrame(products,index=["Product","Price"])
print(df)
print("\n" + "="*30 + "\n")