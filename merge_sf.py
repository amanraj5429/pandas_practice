import pandas as pd
import matplotlib.pyplot as plt

casts = pd.read_csv('cast.csv', index_col = None)
titles = pd.read_csv('titles.csv', index_col = None)

#Suppose, we want see the list of co-actors in the movies. For this, we need to merge the table with itself based on
#the title and year, as shown below. In the below code, co-star for actor ‘Aaron Abrams’ are displayed

c = casts[casts['name'] == 'Aaron Abrams']
print(c.head())

#to find the co-stars, merge the DataFrame with itself based on ‘title’ and ‘year’ i.e. for being a co-star,
#the name of the movie and the year must be same

c_costar = c.merge(casts, on = ['title', 'year']) # notice here casts is in parenthesis
print(c_costar.head(2))

#The problem with above joining is that it displays the ‘Aaron Abrams’ as his co-actor as well . 
#This problem can be avoided as below

c_costar = c_costar[c_costar['name_y'] != 'Aaron Abrams']
print(c_costar.head(2))
