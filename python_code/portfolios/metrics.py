'''
author: d. wells
year:2021
purpose: 
- get the CAPM metrics & use with portfolio.py
'''
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import csv

class GetMetrics:
    ''' use the CAPM financial theory for portfolios '''
    def __init__(self, portfolio, start_term, end_term, output_file):
        self.portfolio = portfolio
        self.start_term = start_term
        self.end_term = end_term
        self.output_file = output_file

    def get_metrics(self):        
        filename = f'{self.output_file}.csv' # create file to save data
        
        ## need to create a MARKET index in order to compute covariance and add it to portfolio
        sp_data = pd.DataFrame()
        print('\n[*] Using S&P 500 as benchmark...')
        t = '^GSPC'
        sp_data[t] = pdr.DataReader(t, data_source='yahoo', start=self.start_term, end=self.end_term)['Adj Close']  
        add_sp = pd.concat([self.portfolio,sp_data],axis=1)
        market_returns = np.log( add_sp / add_sp.shift(1) )
        p_return = np.log( self.portfolio / self.portfolio.shift(1) )
        cov = market_returns.cov() * 252
        cov_with_market = cov.iloc[0,1]
        corr = market_returns.corr()
        print(f'\nCorrelation matrix: \n{corr}')
        with open(filename,'w',newline='') as csvfile:
            csvfile.write('Correlation Matrix\n\n')
        corr.to_csv(filename, mode='a')        
        market_var = market_returns[t].var() * 252
                
        ## get risk-free rate
        rf = float(input('\n[+] Risk free rate (as %): '))
        rf /= 100.00

        ## beta = sigma_(p,m) / (sigma_m)^2
        beta = cov_with_market / market_var
        beta = beta.round(4)
        print(f'\nBeta = {beta}')
        
        ## CAPM return: r_p = r_f + beta_p(r_m - r_f)
        capm_er = rf + beta * 0.05
        capm_er = capm_er.round(4)
        print(f'CAPM Return = {capm_er}')
        metrics = [beta, capm_er]
        capm_metrics = pd.Series(metrics, index = ['Beta','CAPM Return'])
        capm_metrics = capm_metrics.to_frame()
        
        ## Sharpe: (r_p - r_f) / sigma_p
        sharpe_r = (capm_er - rf) / (p_return.std() * 252 ** 0.5)
        sharpe_r = sharpe_r.round(4)
        sharpe_val = sharpe_r.to_frame()
        print(f'\nSharpe Ratio: \n{sharpe_r.to_string()}')

        ## take metrics & write to file
        with open(filename, 'a', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerows('\r')
        capm_metrics.to_csv(filename, mode='a', header=False)
        with open(filename, 'a', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerows('\r')
            csvfile.write('Sharpe Ratio\n')
        sharpe_val.to_csv(filename, mode='a', header=False)