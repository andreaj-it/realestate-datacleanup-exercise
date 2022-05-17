import pandas as pd

df=pd.read_csv('assets/real_estate.csv',sep=';')
df.info()
#df.head()
#df.tail()
#df.sample(5)

max_expensive_home = df.price.max()
max_index = df.price.idxmax()
print('Most expensive Home : '+str(max_expensive_home)+' index : '+str(max_index))

cheapest_home = df.price.min()
min_index = df.price.idxmin()
print('Cheapest Home : '+str(cheapest_home)+' index : '+str(min_index))

biggest_home = df.surface.max()
big_index = df.surface.idxmax()
smaller_home = df.surface.min()
small_index = df.surface.idxmin()
print('The biggest House has a '+str(biggest_home)+' of surface (index : '+str(big_index)+'), and smaller has a '+str(smaller_home)+' of surface  (index : '+str(small_index)+')')

#population_level5 = df.level5.count()
population_level5 = df.level5.unique().size
print('The population level5 is : '+str(population_level5))

#df.dropna()
if df.isnull().values.any():
    stripped_df = df.dropna()
    print(stripped_df)
else:
    print(df)

filter_level5 = df[df['level5'] == "Arroyomolinos (Madrid)"]
print('Mean of prices : '+str(filter_level5['price'].mean()))

import pandas as pd
import matplotlib.pyplot as plt
filter_level5 = df[df['level5'] == "Arroyomolinos (Madrid)"]
plt.hist(filter_level5['price'])
plt.show()

filter_level5 = df[df['level5'].isin(("Fuenlabrada", "Leganés", "Getafe", "Alcorcón"))]
print(filter_level5)

