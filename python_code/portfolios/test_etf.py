import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from sklearn import linear_model

''''''
##section for FETCHING data via API (e.g. Yahoo Finance) or file (e.g. csv)
#df = pandas.read_csv('C:/Users/kinak/Desktop/Finance/oil_market_analysis_1.csv')
#tickers = []
'''
#ex. below
'''
tickers = ['CL=F','USO']
'''
tickers = ['NG=F','UNG']
tickers = ['GC=F','GLD']
tickers = ['SI=F','SLV']
'''
print('*** CORRELATION BETWEEN FUTURE & ETF TRACKING ***')
#futures = input('[+] Enter FUTURE symbol: ')
#tickers.append(futures)
#etf = input('[+] Enter ETF symbol: ')
#tickers.append(etf)
mydata = pd.DataFrame()
for t in tickers:
    mydata[t] = wb.DataReader(t, data_source='yahoo', start='2021-1-1')['Adj Close']
''''''
''''''
##section for PLOTTING data
X = mydata[[tickers[0]]]
y = mydata[tickers[1]]

''' 
##plotting below if needed
plt.figure(figsize=(10,10))
plt.xlabel(f'{tickers[0]} Futures')
plt.ylabel(f'{tickers[1]}')
plt.title(f'{tickers[1]} vs {tickers[0]} Futures')
plt.scatter(X, y)
plt.show()
'''
''''''
''''''
##section for regression
regr = linear_model.LinearRegression()
regr.fit(X, y)
#input the price you want to predict and display
future_price = float(input('[+] Enter FUTURES price for expected ETF price? '))
predict_price = regr.predict([[future_price]])
print(predict_price) 
#print(regr.coef_)
''''''