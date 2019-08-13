import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)
#for filtering of data
after85 = titles[titles['year'] > 1985]
print(after85.head())

movies90 = titles[(titles['year']>= 1990) & (titles['year'] < 2000)]
print(movies90)