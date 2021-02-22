import numpy as np
import pandas as pd
from stock_plot import StockPlot as sp
from pandas_datareader import data as pdr     
from sklearn import linear_model

class StockTrack:
    ''' futures and etf tracker '''
    def __init__(self, tickers, start_term, term, target_price):
        self.tickers = tickers
        self.start_term = start_term
        self.term = term
        self.target_price = target_price

    def create_data(self):
        ## (1) section to create data
        mydata = pd.DataFrame()
        try:
            for t in self.tickers:
                mydata[t] = pdr.DataReader(t, data_source='yahoo', start=self.start_term, end=self.term)['Adj Close']
            file_out = f'{self.tickers[0]}_{self.tickers[1]}.csv'
            try:
                mydata.to_csv(file_out)
                print(f'\n[*] Data output to {file_out}')
            except:
                print('\n[*] File out error!')
            X = mydata[[self.tickers[0]]]
            x_corr = mydata[self.tickers[0]]
            y = mydata[self.tickers[1]] 
        except:
            print('[*] Error: no symbols or values found!')
            exit    
        ## (2) section to plot graphs
        do_plot = input('\n[+] Plot data <Y/N>?: ')
        if do_plot.lower() == 'y':
            try:
                plotting = sp(self.tickers[0],X,self.tickers[1],y)
                plotting.plot_charts()
            except:
                print('[*] Error: input error!')
                exit             
        ## (3) section to do regression
        try:
            correlation = y.corr(x_corr).round(4)
            regr = linear_model.LinearRegression()
            regr.fit(X, y)
            predict_price = regr.predict([[self.target_price]]).round(2)
            print(f'\n[*] Expected price {self.tickers[1]} = {predict_price}') 
            print(f'[*] Correlation = {correlation}')
            #print(regr.coef_)
        except:
            print('[*] Error: no input to process!')
            exit    