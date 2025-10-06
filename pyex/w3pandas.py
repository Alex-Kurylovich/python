import pandas as pd

pd.options.display.max_rows = 200
df = pd.read_csv('data.csv')
print(pd.options.display.max_rows)
print(df.info())
print(df.loc[[0, 1]])
print(df, end='\n\n')

df = pd.read_json('data.json')
print(df.to_string())

