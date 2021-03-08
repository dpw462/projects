'''
author: d. wells
year:2021
purpose: 
- use with portfolio.py to get financial portfolio data & analysis
'''
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
from datetime import date
from portplot import PortPlot as Plt
from metrics import GetMetrics as Metrics

class PortfolioReturns:
    ''' methods for getting all the portfolio data and analysis '''
    def __init__(self, today):
        self.today = today

    def get_yahoo_data(self, pfolio, start_term, end_term):
        ''' fetch from Yahoo Finance API '''
        portfolio = pd.DataFrame()
        for s in pfolio:
            portfolio[s] = pdr.DataReader(s, data_source='yahoo', start=start_term, end=end_term)['Adj Close']
        return portfolio
    
    def get_portfolio_return(self, b, portfolio, start, end):
        ''' section for CALCULATING and DISPLAYING returns '''
        # calculate historical simple returns (i.e. rtrn = (current/previous) - 1)
        # weights (i.e. allocation) need to sum to 1 (i.e. [0.5,0.5] for two funds/tickers)
        
        ## portfolio weights
        weights = []
        weighting = input('\n[+] Allocation (in decimal percentage, or default, "d", for equal allocation)(separate by ";") ?: ')
        if (weighting.lower().strip() == 'd'):
            wght = 1 / b
            for w in range(int(b)):
                w = wght
                weights.append(w)
        elif ';' in weighting:
            for w in weighting.split(';'):
                w = w.strip(' ')
                w = float(w)
                weights.append(w)
        else:
            weights.append(float(weighting))
        weights = np.array(weights)
        
        ## calculate returns        
        returns = (portfolio / portfolio.shift(1)) - 1 # simple, daily returns
        annual_returns = (returns.mean() * 252) # annualized returns ~ 252 trading days
        tot_return = np.dot(annual_returns, weights)
       
        ## print results of respective portfolio returns
        pfolio = (tot_return * 100).round(3)
        print(f'\n[*] Historical returns: {pfolio}%')
    
        ## use CAPM model analysis for portfolios 
        want_capm = input('\n[+] CAPM Analysis (output to CSV) <"y", else any key> ?: ')
        if (want_capm.lower().strip() == 'y'):
            filename = input('[+] Name file: ')
            met = Metrics(portfolio, weights, tot_return, start, end, filename)
            met.get_metrics()
        
    def show_portfolio_data(self):
        ''' get the portfolio from user and process '''
        pfolio = [] # create portfolio
        confirm = 'n'
        try:
            while confirm.lower().strip() == 'n':
                ## input basket of tickers
                investment = input('\n[+] Add investment(s) to portfolio (separate by ";"): ')
                if ';' in investment:
                    for stock in investment.split(';'):
                        stock = stock.strip(' ')
                        pfolio.append(stock)
                else:
                    pfolio.append(investment)
                confirm = input(f'\n{pfolio} \n\n[+] Enter "n" to re-enter, else any key to continue with portfolio: ')
            basket = float(len(pfolio)) # store number of stocks in portfolio
            
            date_err = True
            while date_err:
                try:
                    start_term = input('\n[+] Enter START for historical prices (yyyy-mm-dd), or default, "d", from current year: ')
                    if start_term.lower().strip() == 'd':
                        start_year_now = date.today().year
                        current_year = date(start_year_now, 1, 1)
                        start_term = str(current_year)
                    end_term = input('[+] Enter END for terminal date (yyyy-mm-dd), or default, "d", for today: ')
                    if end_term.lower().strip() == 'd':
                        end_term = self.today
                    dt.datetime.strptime(start_term, '%Y-%m-%d')
                    dt.datetime.strptime(end_term, '%Y-%m-%d')
                    date_err = False
                except ValueError:
                    print('\n[*] Error: date format should be YYYY-MM-DD !')
                                        
            ## get Yahoo info
            portfolio_data = self.get_yahoo_data(pfolio, start_term, end_term)
                
            ## call plotting of portfolio
            plot_port = input('\n[+] Plot graph (output to PDF) <"y", else any key> ?: ')
            if (plot_port.lower().strip() == 'y'):
                try:
                    output = input('[+] Name file: ')
                    plot_ret = Plt(portfolio_data, output)
                    plot_ret.plot_portfolio()
                except:       
                    print('\n[*] Error: invalid filename !')
        
            ## get return on portfolio
            self.get_portfolio_return(basket, portfolio_data, start_term, end_term)
        except:
            print('\n[*] Error: input errors !')
            exit