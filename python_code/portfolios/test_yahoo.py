import yfinance as yf

msft = yf.Ticker('MSFT')
msft.info
hist = msft.history(period='5d')
print(hist['Close'])
print(msft.institutional_holders)
print(msft.balance_sheet)