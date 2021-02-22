import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(f'{df}\n')
#dataframes are a bunch of series that share same index
series_1 = df['W']
#can also pass list of columns
series_2 = df[['W','X','Y']]
print(f'{series_1}\n')
print(f'{series_2}\n')
print(type(series_1))
print(type(df))
print('\n')
#create new column
df['new'] = df['W'] + df['Y']
print(df)

#to remove, need to specify axis & in-place
df.drop('new',axis=1,inplace=True)
print(df)
df.drop('E',inplace=True)
print(df)