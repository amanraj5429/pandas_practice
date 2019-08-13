import pandas as pd
import matplotlib.pyplot as plt

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

# using groupby to count number of movies each year
cg = c.groupby(['year']).size()
print(cg)

# plotting the result

cg.plot()
plt.show()
