import pandas as pd
import matplotlib.pyplot as plt

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

c = casts

# at first group these data for actor and actress separately
c_dec = c.groupby(['type', c['year']//10*10]).size()
print(c_dec)

# to make another type of table in which values will be side by side and plotting like that also
# use unstack(0)

c_unstk2 = c_dec.unstack(0)
print(c_unstk2)

# for plotting
c_unstk2.plot(kind = 'bar')
plt.show()