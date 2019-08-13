import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

#groupby with custom field
# decade 1985//10= 198, 198*10= 1980, decade = year//10*10
decade = c['year']//10*10
c_dec = c.groupby(decade).size()
print(c_dec.head())