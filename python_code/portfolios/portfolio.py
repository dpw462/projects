'''
author: d. wells
year:2021
purpose: 
- create & analyze portfolios with CAPM
- program needs: metrics.py, portplot.py, returns.py
'''
from datetime import date
from returns import PortfolioReturns as PR

#############################################################################################################

if __name__ == '__main__':
    ''' call the main class here and pass today's date as argument '''
    today = str(date.today())
    print('\n****************************************')
    print('********** PORTFOLIO ANALYSIS **********')
    print('****************************************')
    redo = 'y'
    while redo.lower().strip() == 'y':
        ## get portfolio data, plot and show results
        returns = PR(today)
        returns.show_portfolio_data()
        redo = input('\n[+] Repeat <"y", else any key>?: ')            
    print('\n[*] Exiting... bye!')
    exit

#############################################################################################################