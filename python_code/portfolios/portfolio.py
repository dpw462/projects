import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

##section for FETCHING data
#indices = ['^GSPC','^IXIC','^DJI']
#ind_data = pd.DataFrame()
#for k in indices:
#    ind_data[k] = wb.DataReader(k,data_source='yahoo',start='2015-1-1')['Adj Close']
tickers1 = ['VFIAX']
mydata1 = pd.DataFrame()
for t in tickers1:
    mydata1[t] = wb.DataReader(t,data_source='yahoo',start='2010-1-1')['Adj Close']
#tickers2 = ['AAPL','GOOG','MSFT','AMZN','FB','PG','V','JPM','BRK-A','JNJ'] 
tickers2 = ['MSFT','INTC','NVDA','IBM']
mydata2 = pd.DataFrame()
for i in tickers2:
    mydata2[i] = wb.DataReader(i,data_source='yahoo',start='2010-1-1')['Adj Close']

##section for PLOTTING data
'''
ind_data.iloc[0]
(ind_data / ind_data.iloc[0] * 100).plot(figsize=(15,10))
mydata1.iloc[0]
(mydata1 / mydata1.iloc[0] * 100).plot(figsize=(15,10))
mydata2.iloc[0]
(mydata2 / mydata2.iloc[0] * 100).plot(figsize=(15,10))
plt.show()
'''

##section for CALCULATING and DISPLAYING returns
# returns all simple i.e. rtrn = (current/previous) - 1
# first portfolio & second portfolio
# weights need to sum to 1 i.e. [0.5,0.5] for two funds/tickers
returns1 = (mydata1 / mydata1.shift(1)) - 1
weights1 = np.array([1])
returns2 = (mydata2 / mydata2.shift(1)) - 1
weights2 = np.array([0.25,0.25,0.25,0.25])
# indices
#returns_index = (ind_data / ind_data.shift(1)) - 1
annual_returns1 = returns1.mean() * 250
annual_returns2 = returns2.mean() * 250
#annual_idxrtn = returns_index.mean() * 250
tot_return1 = np.dot(annual_returns1, weights1)
tot_return2 = np.dot(annual_returns2, weights2)
pfolio1 = str(round(tot_return1, 4) * 100) + ' %'
pfolio2 = str(round(tot_return2, 4) * 100) + ' %'
#index_return_tot = str(round(annual_idxrtn, 4) * 100) + ' %'
print('Return of Portfolio 1: '+pfolio1)
print('Return of Portfolio 2: '+pfolio2)
#print('\nComposite Index Return: \n'+index_return_tot)