'''
author: d. wells
year:2021
purpose: 
- use with portfolio.py to plot returns
'''
import matplotlib.pyplot as plt

class PortPlot:
    ''' plot simple annual returns on portfolio '''
    def __init__(self, portfolio, graph):
        self.portfolio = portfolio
        self.graph = graph

    def plot_portfolio(self):
        ''' section for PLOTTING performance '''
        port = self.portfolio.iloc[0]
        (self.portfolio / port * 100).plot(figsize=(15,10))
        plt.xlabel('Time', fontsize=18)
        plt.ylabel('Security Returns (Normalized)', fontsize=18)
        plt.title('Portfolio Performance', fontsize=24)
        plot_file = f'{self.graph}.pdf'
        plt.savefig(plot_file)
        plt.show()
        print(f'\n[*] Graph saved to {plot_file}')