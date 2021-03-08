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
import yfinance as yf

class GetMetrics:
    ''' use the CAPM financial theory for portfolios '''
    def __init__(self, portfolio, weights, tot_return, start_term, end_term, output_file):
        self.portfolio = portfolio
        self.weights = weights
        self.tot_return = tot_return
        self.start_term = start_term
        self.end_term = end_term
        self.output_file = output_file

    def get_metrics(self):        
        filename = f'{self.output_file}.csv' # create file to save data
        
        ## need to create a MARKET index & add to portfolio in order to compute covariance
        sp_data = pd.DataFrame()
        print('\n[*] Using S&P 500 as benchmark...')
        t = '^GSPC'
        sp_data[t] = pdr.DataReader(t, data_source='yahoo', start=self.start_term, end=self.end_term)['Adj Close']  
        add_sp = pd.concat([self.portfolio, sp_data],axis=1)
        market_returns = np.log( add_sp / add_sp.shift(1) )
        p_return = np.log( self.portfolio / self.portfolio.shift(1) ) # log returns of the portfolio
        data = np.dot(p_return, self.weights) # returns with weights
        add_returns = pd.DataFrame(data) # tabulated portfolio returns
        
        '''
        ## also get data for 10-yr treasury yield (i.e. risk-free rate)
        # useful if you wish to adjust performance parameters relative to this benchmark
        rf_data = pd.DataFrame()
        treasury = '^TNX' # if another rate is desired, modify here or below
        rf_data[treasury] = pdr.DataReader(treasury, data_source='yahoo', start=self.start_term, end=self.end_term)['Adj Close']
        '''
        
        cov = market_returns.cov() * 252
        cov_with_market = cov.iloc[0,1]
        corr = market_returns.corr()
        print(f'\nCorrelation matrix: \n{corr}')
        with open(filename,'w',newline='') as csvfile:
            csvfile.write('Correlation Matrix\n\n')
        corr.to_csv(filename, mode='a')        
        market_var = market_returns[t].var() * 252
                
        ## get risk-free rate
        rf_val = True
        while rf_val:
            try:
                rf = input('\n[+] Risk free rate (as %) (or default, "d", for current 10-year Treasury Yield): ')
                if (rf.lower().strip() == 'd'):
                    t = yf.Ticker('^TNX')
                    current_t = t.history(period='1d')
                    t_yield = round(current_t['Close'][0],3)
                    rf = float(t_yield)
                    rf /= 100.00
                    print(f'[*] Current T-Yield = {t_yield}')
                    rf_val = False
                else:
                    rf = float(rf)
                    rf /= 100.00
                    rf_val = False
            except ValueError:
                print('[*] Error: not a number !')

        ## beta = sigma_(p,m) / (sigma_m)^2
        beta = cov_with_market / market_var
        beta = beta.round(4)
        print(f'\nBeta = {beta}')
        
        ## CAPM return: r_p = r_f + beta_p(r_m - r_f)
        ## compute Jensen Alpha: alpha = actual_return - r_p
        # market premium is appx. 5.4% based on compounded market return and treasury yield
        capm_er = rf + (beta * 0.054)
        capm_er = capm_er.round(4)
        print(f'CAPM Return = {capm_er}')
        alpha = (self.tot_return - capm_er).round(4)
        print(f'Alpha = {alpha}')

        ## Sharpe: (r_p - r_f) / sigma_p
        sharpe_r = (capm_er - rf) / (add_returns.std() * 252 ** 0.5)
        sharpe_r = sharpe_r.round(4)
        sharpe_ratio =  float(sharpe_r)
        print(f'Sharpe Ratio = {sharpe_ratio}')
        
        metrics = [beta, capm_er, alpha, sharpe_ratio]
        capm_metrics = pd.Series(metrics, index = ['Beta', 'CAPM Return', 'Alpha', 'Sharpe Ratio'])
        capm_metrics = capm_metrics.to_frame()
                
        ## take metrics & write to file
        with open(filename, 'a', newline='') as csvfile:
            wr = csv.writer(csvfile)
            wr.writerows('\r')
        capm_metrics.to_csv(filename, mode='a', header=False)