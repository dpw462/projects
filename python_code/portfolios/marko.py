import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
'%matplotlib inline'
assets = ['PG', '^GSPC']
pf_data = pd.DataFrame()
for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'yahoo', start = '2010-1-1')['Adj Close']
#print(pf_data.head())
#print(pf_data.tail())
(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10, 5))
log_returns = np.log(pf_data / pf_data.shift(1))
log_returns.mean() * 250
log_returns.cov() * 250
log_returns.corr()
num_assets = len(assets)
print(num_assets)
arr = np.random.random(2)
#print(arr)
arr[0] + arr[1]
weights = np.random.random(num_assets)
weights /= np.sum(weights)
print(weights)
weights[0] + weights[1]

#Expected Portfolio Return:
alpha = np.sum(weights * log_returns.mean()) * 250
print(alpha)
#Expected Portfolio Variance:
variance = np.dot(weights.T, np.dot(log_returns.cov() * 250, weights))
print(variance)
#Expected Portfolio Volatility:
beta = np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights)))
print(beta)
pfolio_returns = []
pfolio_volatilities = []
for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)
portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})
#print(portfolios.head())
#print(portfolios.tail())
portfolios.plot(x='Volatility', y='Return', kind='scatter', figsize=(10, 6))
plt.xlabel('Expected Volatility')
plt.ylabel('Expected Return')
plt.show()