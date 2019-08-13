import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

# we have to see the movies done by an actor 'Aaron Abram' yearwise

cf = c[c['name'] == 'Aaron Abrams']
cfa = cf.groupby(['year']).size()
print(cfa)


# for knowing the name of each movie also

cng = cf.groupby(['year', 'title']).size()
print(cng)