'''
author: d. wells
year:2021
purpose: 
- track prices and correlation in markets
- program needs stock_track.py & stock_plot.py
'''
import yfinance as yf
from stock_track import StockTrack as st
from datetime import date

''' return the current price of input '''
def get_current_quote(symbol):
    quote = yf.Ticker(symbol)
    current_quote = quote.history(period='1d')
    return round(current_quote['Close'][0],3)

''' main program with inputs '''
if __name__ == '__main__':
    today = str(date.today())
    print('\n*** PRICE & CORRELATION TRACKING ***')
    redo = 'y'
    while redo.lower().strip() == 'y':
        ## store symbols to fetch data via Yahoo Finance API
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
            ticker1_price = input('[+] Enter TICKER 1: ')
            ticker1_quote = get_current_quote(ticker1_price)
            print(f'[*] Current price: {ticker1_quote}')
            tickers.append(ticker1_price)
            ticker2_price = input('[+] Enter TICKER 2: ')
            ticker2_quote = get_current_quote(ticker2_price)
            print(f'[*] Current price: {ticker2_quote}')
            tickers.append(ticker2_price)
            target_price = float(input(f'[+] Enter price target on {tickers[0]} for expected {tickers[1]}: '))
        except:
            print("\n[*] Error: input errors!")
            exit
        
        ## main program here
        try:
            tick1_tick2 = st(tickers,start_term,term,target_price)
            tick1_tick2.create_data()
        except:
            print('[*] Error: nothing to process!')
            exit
        try:
            redo = input('\n[+] Repeat <Y, else any key to exit>?: ')
            tickers.clear()
        except:
            print('\n[*] Error: input error!')
            exit