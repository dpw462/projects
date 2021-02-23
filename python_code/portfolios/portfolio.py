import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import date

def get_portfolio_data(today):
    pfolio_1 = []
    pfolio_2 = []
    try:
        ## basket 1
        investment_1 = input('\n[+] Add investment(s) to first portfolio (separate by ";"): ')
        if ';' in investment_1:
            for stock in investment_1.split(';'):
                stock = stock.strip(' ')
                pfolio_1.append(stock)
        else:
            pfolio_1.append(investment_1)
        start_term_1 = input('[+] Enter START for historical prices (yyyy-mm-dd): ')
        end_term_1 = input('[+] Enter END for terminal date (yyyy-mm-dd), or default, "d", for today: ')
        if end_term_1.lower() == 'd':
            end_term_1 = today
        print(pfolio_1)
        basket1 = float(len(pfolio_1))
        #print(basket_1)
        portfolio_1_data = get_yahoo_data(pfolio_1, start_term_1, end_term_1)
        
        ## basket 2
        investment_2 = input('\n[+] Add investment(s) to second portfolio (separate by ";"): ')
        if ';' in investment_2:
            for stock in investment_2.split(';'):
                stock = stock.strip(' ')
                pfolio_2.append(stock)
        else:
            pfolio_2.append(investment_2)
        start_term_2 = input('[+] Enter START for historical prices (yyyy-mm-dd): ')
        end_term_2 = input('[+] Enter END for terminal date (yyyy-mm-dd), or default, "d", for today: ')
        if end_term_2.lower() == 'd':
            end_term_2 = today
        print(pfolio_2)
        basket2 = float(len(pfolio_2))
        #print(basket_2)
        portfolio_2_data = get_yahoo_data(pfolio_2, start_term_2, end_term_2)
        
        ## call plotting of portfolios
        #plot_portfolios(portfolio_1_data, portfolio_2_data)
        ## get returns on portfolios
        get_portfolio_return(basket1, portfolio_1_data, basket2, portfolio_2_data)
    except:
        print('\n[*] Error: input errors!')
        exit
    
def get_yahoo_data(pfolio, start_term, end_term):
    portfolio = pd.DataFrame()
    for s in pfolio:
        portfolio[s] = pdr.DataReader(s, data_source='yahoo', start=start_term, end=end_term)['Adj Close']
    
    return portfolio
    
def plot_portfolios(portfolio1, portfolio2):
    ## section for PLOTTING prices
    port1 = portfolio1.iloc[0]
    (portfolio1 / port1 * 100).plot(figsize=(15,10))
    port2 = portfolio2.iloc[0]
    (portfolio2 / port2 * 100).plot(figsize=(15,10))
    plt.show()

def get_portfolio_return(b1, portfolio1, b2, portfolio2):
    ## (3) section for CALCULATING and DISPLAYING returns
    # returns all simple returns i.e. rtrn = (current/previous) - 1
    # weights (i.e. allocation) need to sum to 1 (i.e. [0.5,0.5] for two funds/tickers)
    # portfolio 1 weights
    weights1 = []
    returns1 = (portfolio1 / portfolio1.shift(1)) - 1
    weighting_1 = input('\n[+] Portfolio 1: Allocation (in decimal percentage, or "e" for equal distribution)(separate by ";")?: ')
    if (weighting_1.lower() == 'e'):
        w1 = 1 / b1
        for w in range(int(b1)):
            w = w1
            weights1.append(w)
    elif ';' in weighting_1:
        for w in weighting_1.split(';'):
            w = w.strip(' ')
            w = float(w)
            weights1.append(w)    
    else:
        weights1.append(float(weighting_1))
    weights_1 = np.array(weights1)
    #portfolio 2 weights    
    weights2 = []
    returns2 = (portfolio2 / portfolio2.shift(1)) - 1
    weighting_2 = input('[+] Portfolio 2: Allocation (in decimal percentage, or "e" for equal distribution)(separate by ";")?: ')
    if (weighting_2.lower() == 'e'):
        w2 = 1 / b2
        for w in range(int(b2)):
            w = w2
            weights2.append(w)
    elif ';' in weighting_2:
        for w in weighting_2.split(';'):
            w = w.strip(' ')
            w = float(w)
            weights2.append(w)    
    else:
        weights2.append(float(weighting_2))
    weights_2 = np.array(weights2)
    # calculate returns        
    annual_returns1 = returns1.mean() * 250
    annual_returns2 = returns2.mean() * 250
    tot_return1 = np.dot(annual_returns1, weights_1)
    tot_return2 = np.dot(annual_returns2, weights_2)
    # print results of respective portfolio returns
    pfolio1 = str(tot_return1.round(4) * 100) + ' %'
    pfolio2 = str(tot_return2.round(4) * 100) + ' %'
    print(f'\n[*] Return of Portfolio 1: {pfolio1}')
    print(f'[*] Return of Portfolio 2: {pfolio2}')

''' main portfolio program here '''
if __name__ == '__main__':
    today = str(date.today())
    print('\n*** PORTFOLIO ANALYSIS ***')
    redo = 'y'
    try:
        while redo.lower() == 'y':
            ## get portfolio data, plot and show returns
            get_portfolio_data(today)
            redo = input('\n[+] Repeat <Y, else any key>?: ')
            redo.strip(' ')
    except:
        print('[*] Error: input error!')
        exit