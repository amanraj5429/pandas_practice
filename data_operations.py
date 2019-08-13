import pandas as pd
# for selecting a row
casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)



ct = casts['title']
print(type(ct))
print(ct.head())
ctr = casts.ix[0]
print(type(ctr))
print(ctr)
