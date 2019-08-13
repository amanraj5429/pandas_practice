import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

t = titles
macbeth = t[t['title'] == 'Macbeth'] #in this expression sort_index is by default

print(macbeth.head())

#using sort_index
m1 = t[t['title'] == 'Macbeth'].sort_index()
print(m1)

#using sort_values
m2 = t[t['title'] == 'Macbeth'].sort_values('year')
print(m2)