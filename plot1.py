import pandas as pd
import matplotlib.pyplot as plt


casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

t = titles

# counting number of films yearwise
ct = t['year'].value_counts()
print(ct.head())

ct.sort_index().plot()
plt.show()
