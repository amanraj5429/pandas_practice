import pandas as pd
import matplotlib.pyplot as plt

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

# at first group these data for actor and actress separately
c_dec = c.groupby(['type', c['year']//10*10]).size()
print(c_dec)

# now use unstack to create a new DataFrame based on index
c_unstk = c_dec.unstack()
print(c_unstk)

# now plot this on graph
c_unstk.plot(kind = 'bar')
plt.show()