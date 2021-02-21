'''
author: d. wells
year:2021
purpose: 
track prices and correlation in stocks, futures
program needs stock_track.py & stock_plot.py
'''
from stock_track import StockTrack as st
from datetime import date

'''main program with inputs'''
if __name__ == '__main__':
    today = str(date.today())
    print('\n*** PRICE & CORRELATION TRACKING ***')
    redo = 'y'
    while redo.lower().strip() == 'y':
        ##store symbols to fetch data via Yahoo Finance API
        tickers = []
        #examples...
        #tickers = ['CL=F','USO'] will give FUTURE and ETF
        #tickers = ['^GSPC','SPY'] will give INDEX and ETF
        #tickers = ['MSFT','IBM'] will give EQUITITES
        try:
            start_term = input('\n[+] Enter START date for regression (yyyy-mm-dd): ')
            term = input('[+] Enter terminal date for regression (yyyy-mm-dd), or "d" for today: ')
            if term.lower() == 'd':
                term = today
                print(term)
            ticker1_price = input('[+] Enter TICKER 1: ')
            tickers.append(ticker1_price)
            ticker2_price = input('[+] Enter TICKER 2: ')
            tickers.append(ticker2_price)
            target_price = float(input(f'[+] Enter price target on {tickers[0]} for expected {tickers[1]}: '))
        except:
            print("\n[*] Error: input errors!")
            exit
        ##main program here
        try:
            tick1_tick2 = st(tickers,start_term,term,target_price)
            tick1_tick2.create_data()
        except:
            print('[*] Error: nothing to process!')
            exit
        try:
            redo = input('\n[+] Repeat <Y,N>?: ')
            tickers.clear()
        except:
            print('\n[*] Error: input error!')
            exit