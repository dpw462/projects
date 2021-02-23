import numpy as np
import pandas as pd
from pandas_datareader import data as wb

tickers = ['PG', 'MSFT','^GSPC']
data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end='2016-12-31')['Adj Close']  

sec_returns = np.log( data / data.shift(1) )
cov = sec_returns.cov() * 250
print(cov)
corr = sec_returns.corr()
print(corr)
cov_with_market = cov.iloc[0,1]
#print(cov_with_market)
market_var = sec_returns['^GSPC'].var() * 250
#print(market_var)

#beta = sigma_(pg,m) / (sigma_m)^2
PG_beta = cov_with_market / market_var
print(f'Beta = {PG_beta}')

#CAPM return: r_pg = r_f + beta_pg(r_m - r_f)
PG_er = 0.025 + PG_beta * 0.05
print(f'CAPM Return = {PG_er}')

#Sharpe: (r_pg - r_f) / sigma_pg
Sharpe = (PG_er - 0.025) / (sec_returns['PG'].std() * 250 ** 0.5)
print(f'Sharpe Ratio: {Sharpe}')