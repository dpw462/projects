import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as pdr
from sklearn import linear_model


#yf.pdr_override()
##section for FETCHING data via API (e.g. Yahoo Finance) or file (e.g. csv)
#df = pandas.read_csv('C:/Users/kinak/Desktop/Finance/oil_market_analysis_1.csv')
#tickers = []
''''''
##ex. below
#tickers = ['CL=F','USO']
#tickers = ['NG=F','UNG']
#tickers = ['GC=F','GLD']
#tickers = ['SI=F','SLV']
'''
print('*** CORRELATION BETWEEN FUTURE & ETF TRACKING ***')
futures = input('[+] Enter FUTURE: ')
tickers.append(futures)
etf = input('[+] Enter ETF: ')
tickers.append(etf)
data = pdr.get_data_yahoo(tickers[0], tickers[1], start='2020-01-01')
'''
#msft = yf.Ticker('MSFT')
#nat_gas_fut = yf.Ticker('NG=F')
#nat_gas_etf = yf.Ticker('UNG')
oil_fut = yf.Ticker('VTSAX')
oil_etf = yf.Ticker('VFIAX')
dow = yf.Ticker('DIA')
#msft.info
#hist = msft.history(period='5d')
hist1 = oil_fut.history(period='5y')
hist2 = oil_etf.history(period='5y')
hist3 = dow.history(period='5y')
y1 = hist1['Close']
y2 = hist2['Close']
y3 = hist3['Close']
#print(y1,y2)
plt.figure(figsize=(15,5))
plt.plot(y1, color = 'r')
plt.plot(y2, color = 'g')
plt.plot(y3, color = 'b')
plt.show()
#print(msft.institutional_holders)
#print(msft.balance_sheet)