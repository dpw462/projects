'''
## get econ stats: GDP, CPI, Debt, M2...
## needs: getfred.py
author: dw
date: 20211110
updated: 20230227
'''
import datetime
from getfred import GetFred as GF
##################################################
if __name__ == '__main__':
    ''' call the main class here and pass dates '''
    print('\n[***] Welcome to FRED Analysis Package (FREDAP) [***]')
    redo = 'y' # initialize main program loop here
    while (redo.lower().strip() == 'y'):
        ## define periods
        beg_yr = input('\n[+] Enter initial year: ')
        start = datetime.datetime(int(beg_yr),1,1)
        end_yr = input('[+] Enter terminal year: ')
        end = datetime.datetime(int(end_yr),12,31)
        ## get FRED data and analysis
        fred_data = GF(start,end)
        fred_data.fetch_fred_data()
        ## restart program if desired
        redo = input('\n[+] Start over (y, else any key): ')
    print('\n[*] Exiting... bye!')
    exit
##################################################