'''
author: d. wells
year:2021
purpose: 
- create & analyze portfolios with CAPM
- program needs metrics.py
'''
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import date
from metrics import GetMetrics as Metrics

def get_portfolio_data(today):
    pfolio = [] # create portfolio
    confirm = 'n'
    try:
        while confirm.lower().strip() == 'n':
            ## basket of tickers
            investment = input('\n[+] Add investment(s) to portfolio (separate by ";"): ')
            if ';' in investment:
                for stock in investment.split(';'):
                    stock = stock.strip(' ')
                    pfolio.append(stock)
            else:
                pfolio.append(investment)
            confirm = input(f'\n[+] Process portfolio {pfolio} <"N", else any key to proceed>?: ')
        
        start_term = input('\n[+] Enter START for historical prices (yyyy-mm-dd): ')
        end_term = input('[+] Enter END for terminal date (yyyy-mm-dd), or default, "d", for today: ')
        if end_term.lower().strip() == 'd':
            end_term = today
        basket = float(len(pfolio))
        portfolio_data = get_yahoo_data(pfolio, start_term, end_term)
                
        ## call plotting of portfolio
        plot_port = input('\n[+] Plot graph (output to PDF) <"Y", else any key>?: ')
        if (plot_port.lower().strip() == 'y'):
            plot_portfolio(portfolio_data, 'Portfolio')
        
        ## get return on portfolio
        get_portfolio_return(basket, portfolio_data, start_term, end_term)    
    except:
        print('\n[*] Error: input errors!')
        exit
    
def get_yahoo_data(pfolio, start_term, end_term):
    ''' fetch from Yahoo Finance API '''
    portfolio = pd.DataFrame()
    for s in pfolio:
        portfolio[s] = pdr.DataReader(s, data_source='yahoo', start=start_term, end=end_term)['Adj Close']
    return portfolio
    
def plot_portfolio(portfolio, filename):
    ''' section for PLOTTING performance '''
    port = portfolio.iloc[0]
    (portfolio / port * 100).plot(figsize=(15,10))
    plt.xlabel('Time', fontsize=18)
    plt.ylabel('Security Returns (Normalized)', fontsize=18)
    plt.title('Portfolio Performance', fontsize=24)
    plot_file = f'{filename}.pdf'
    plt.savefig(plot_file)
    plt.show()
    print(f'\n[*] Graph saved to {plot_file}')
    
def get_portfolio_return(b, portfolio, start, end):
    ''' section for CALCULATING and DISPLAYING returns '''
    # returns historical simple returns i.e. rtrn = (current/previous) - 1
    # weights (i.e. allocation) need to sum to 1 (i.e. [0.5,0.5] for two funds/tickers)
    ## portfolio weights
    weights = []
    returns = (portfolio / portfolio.shift(1)) - 1
    weighting = input('\n[+] Portfolio: Allocation (in decimal percentage, "e" for equal)(separate by ";")?: ')
    if (weighting.lower().strip() == 'e'):
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
    annual_returns = (returns.mean() * 252) # daily returns ~ 252 trading days
    tot_return = np.dot(annual_returns, weights)
       
    ## print results of respective portfolio returns
    pfolio = (tot_return * 100).round(3)
    print(f'\n[*] Portfolio - Historical return: {pfolio}%')
    
    ## use CAPM model analysis for portfolios 
    want_capm = input('\n[+] CAPM Analysis (output to CSV) <"Y", else any key>?: ')
    if (want_capm.lower().strip() == 'y'):
        filename = input('\n[+] Name file to write Portfolio: ')
        met = Metrics(portfolio, start, end, filename)
        met.get_metrics()
        
#############################################################################################################
''' main program here '''
if __name__ == '__main__':
    today = str(date.today())
    print('\n********** PORTFOLIO ANALYSIS **********')
    redo = 'y'
    while redo.lower().strip() == 'y':
        ## get portfolio data, plot and show results
        get_portfolio_data(today)
        redo = input('\n[+] Repeat <"Y", else any key>?: ')            
    print('\n[*] Exiting... bye!')
    exit
#############################################################################################################