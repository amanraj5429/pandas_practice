import pandas as pd

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts
# to see that in row 3 &4 there is null values
print(c.ix[3:4])

# finding index of rows which has null values using isnull()
print(c['n'].isnull().head())

#finding index of rows which has null values using notnull()
print(c['n'].notnull().head())

# for finding rows and printing them which has null values
has_null = c[c['n'].isnull()]
print(has_null.head())

# filling of null values by using fillna with 'NA'
c_fill = c[c['n'].isnull()].fillna('NA')
print(c_fill.head())
