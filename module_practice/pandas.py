 import pandas as pd

# Creating a Series from a tuple
prices = pd.Series((99, 149, 199, 249))  # Default integer index
print("Series from tuple:\n", prices)

# Creating a Series with custom indices
marks = pd.Series([85, 90, 95], index=['Math', 'Physics', 'Chemistry'])
print("\nCustom index Series:\n", marks)

# Creating a Series from a dictionary with country population
pop = pd.Series({'India': 1400, 'USA': 331, 'Japan': 125})
print("\nPopulation Series:\n", pop)

# Creating a DataFrame from a dictionary with mixed types
info = {
    'Product': ['Laptop', 'Tablet', 'Phone'],
    'Price': [70000, 30000, 20000],
    'InStock': [True, False, True]
}
df1 = pd.DataFrame(info)
print("\nProduct DataFrame:\n", df1)

# Creating a DataFrame from list of dictionaries (slightly different format)
sales_data = [
    {'Employee': 'Raj', 'Sales': 50000},
    {'Employee': 'Simran', 'Sales': 65000},
    {'Employee': 'Aman', 'Sales': 48000}
]
df2 = pd.DataFrame(sales_data)
print("\nSales DataFrame:\n", df2)
