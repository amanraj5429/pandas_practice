import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

t = titles

# search for movies which starts with 'maa'
stMaa = t[t['title'].str.startswith('Maa')]
print(stMaa.head())