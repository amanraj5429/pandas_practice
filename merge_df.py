import pandas as pd
import matplotlib.pyplot as plt

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)
release = pd.read_csv('release_dates.csv', index_col = None)

print(release.head())
print(casts.head())

# we want release date of movie 'Amelia' so for this we will filter first according to title in the cast DataFrame
# since we know title of film so we ll filter using this
c_Amelia = casts[casts['title'] == 'Amelia']
print(c_Amelia)

# now we ll filter the same title from release DataFrame(ie Amelia)
r_Amelia = release[release['title'] == 'Amelia']
print(r_Amelia)

# now we will have to merge these two DataFrames to create a third DataFrame which will contain columns of both
# since there is no 'Amelia' in casts for year 1966 so it will not merge that row

amelia_release = c_Amelia.merge(r_Amelia)
print(amelia_release) 