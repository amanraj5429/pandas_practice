import pandas as pd
casts = pd.read_csv('cast.csv', index_col = None)
print(casts.head(10))


titles = pd.read_csv('titles.csv', index_col = None)
print(titles.tail(10))


