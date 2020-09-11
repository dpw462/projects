import numpy as np
import pandas as pd
#from pandas_datareader import data as wb
import pandas_datareader as pdr

ticker = input('Enter ticker: ')
rng = input('Enter range (e.g. "2019-1-1"): ') 

stock = pdr.DataReader(ticker,data_source='yahoo',start=rng)
stocks = str(stock)

stockFile = open("stocks.txt", "a")
stockFile.write(stocks)
stockFile.close()
#print (stock)


