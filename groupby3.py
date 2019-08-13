import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

# grouping based on maximum rating yearwise
crmx = c.groupby(['year']).n.max()
print(crmx.head())

# grouping based on minimum rating yearwise
crmn = c.groupby(['year']).n.min()
print(crmn.head())

# mean of ratings yearwise
crmean = c.groupby(['year']).n.mean()
print(crmean.head())