import matplotlib.pyplot as plt

class StockPlot:
    ''' use for plotting data on futres vs etf'''
    def __init__(self,first_ticker,X,second_ticker,y):
        self.first_ticker = first_ticker
        self.X = X
        self.second_ticker = second_ticker
        self.y = y

    def plot_charts(self):
        plt.figure(figsize=(15,5))
        plt.xlabel(f'{self.first_ticker}')
        plt.ylabel(f'{self.second_ticker}')
        plt.title(f'{self.second_ticker} vs {self.first_ticker}')
        plt.scatter(self.X, self.y)
        plot_file = f'{self.second_ticker}_vs_{self.first_ticker}.pdf'
        plt.savefig(plot_file)
        print(f'\n[*] Graph saved to {plot_file}')
        plt.show()