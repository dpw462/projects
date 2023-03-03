'''
## get econ stats: GDP, CPI, Debt, M2...
## use with: fred.py
author: dw
date: 20211110
updated: 20230301
'''
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
##################################################
class GetFred:
    def __init__(self, start, end):
        self.start = start
        self.end = end
##################################################
    def fetch_fred_data(self):
        ## GET ECONOMIC STATS OF INTEREST HERE 
        '''
        NEED CODES (e.g. "Reap GDP" is given by "gdpca", etc.). 
        FIND ON FRED SITE: https://fred.stlouisfed.org 
        '''
        fredcodes = {
            'TotPop (k)':'pop', # INDEX [0]: total population; (k) persons, not seasonal adjusted
            'NonFarm (k)':'paynsa', # [2]: total non-farm payroll i.e. ~80% working employment; (k) of persons, not seasonal adjusted 
            'UnEmployRate (%)':'unratensa', # [4]: unemployment rate; %, not seasonal adjusted 
            'Employ2Pop (%)':'LNU02300000', # [6]: employment to population ratio; %, not seasonal adjusted
            'Inc/Cap ($)':'A792RC0A052NBEA', # [8]: personal income per capita; USD, not seasonal adjusted
            'Savings ($B)':'A071RC1A027NBEA', # [10]: personal savings; (B) USD, not seasonal adjusted
            'HomeOwners (%)':'RHORUSQ156N', # [12]: homeownership rate; %, not seasonal adjusted
            'M2 ($B)':'m2ns', # [14]: money supply (M2); (B) USD, not seasonal adjusted
            'RealGDP ($B)':'gdpca', # [16]: real GDP; (B) USD, not seasonal adjusted
            'NomGDP ($B)':'fygdp', # [18]: nominal GDP; (B) USD, not seasonal adjusted
            'Debt ($M)':'gfdebtn', # [20]: total public debt; (M) USD, not seasonal adjusted
            'GovtExpenditures ($B)':'W068RC1A027NBEA', # [22]: total government expenditures; (B) USD, not seasonal adjusted
            'TaxRev ($B)':'W006RC1A027NBEA', # [24]: current tax receipts; (B) USD, not seasonal adjusted 
            'CorpTaxRev ($B)':'fctax', # [26]: tax receipts on corporate income; (B) USD, not seasonal adjusted
            'TaxRate (%)':'iittrhb', # [28]: individual income tax rate, highest bracket; %, not seasonal adjusted
            'CPI (1982-1984=100)':'cpiaucns', # [30]: all items CPI; Index: 1982-1984 = 100, not seasonal adjusted
            'IntRate (%)':'fedfunds', # [32]: fed funds rate; %, not seasonal adjusted
            'Retail_Inv2Rev':'RETAILIRNSA', # [34]: retailers inventory to sales ratio; ratio = Inv/Rev, not seasonal adjusted
            'Manuf_Inv2Rev':'MNFCTRIRNSA', # [36]: manufacturers inventory to sales ratio; ratio = Inv/Rev, not seasonal adjusted
            'NatGas (Bcf)':'NATURALGASD11', # [38]: nat gas consumption; Bcf, seasonal adjusted
            'WTI ($/brl)':'WTISPLC', # [40]: oil spot prices (WTI); USD per barrel, not seasonal adjusted 
            'NASDAQ (1971=100)':'nasdaqcom', # [42]: nasdaq composite index; Index: 1971 = 100, not seasonal adjusted
            'VIX':'vixcls', # [44]: cboe volatility index; not seasonal adjusted
            'Consumer Sentiment (1966=100)':'umcsent' # [46]: umich consumer sentiment; Index: 1966Q1 = 100, not seasonal adjusted
        }   
        stats = [] # we will need to store and update the dataframes as we loop through the different codes
        # loop through FRED and get the data here
        for code in fredcodes:
            stat = pdr.DataReader(fredcodes[code],'fred',self.start,self.end)
            stat.index = pd.to_datetime(stat.index)
            stat['year'] = stat.index.year
            stat_ann = stat.groupby(['year']).median().round(3)
            stat_ann.columns = [code]
            pct_chg_code = f'%_chg-{code}'
            stat_ann[pct_chg_code] = 100*(stat_ann.pct_change())
            stats.append(stat_ann)
        stats = pd.concat(stats,axis=1)
        # store data in Excel files
        stats.to_excel('us-econ.xlsx',sheet_name='us-econ')
        us_econ_corr = stats.corr()
        us_econ_corr.to_excel('us-econ_corr.xlsx',sheet_name='us-econ_corr')
        print(f'\n[*] Data saved as: \n\t[>] us-econ.xlsx\n\t[>] us-econ_corr.xlsx')
        ##################################################
        ## RATIO/METRIC CALCULATION AND ANALYSIS HERE 
        '''
        SOME RATIOS OF INTEREST:
            Savings/Capita, Savings/Income, TaxRev/Capita, CorpTaxRev/TaxRev, Debt/GDP, Debt/Capita, 
            GDP/Capita, TaxRev/Debt, Inflation (as pct chg of CPI), etc.
        Need to use proper index for iloc calc and remember to standardize the units!
        '''
        ratios = input('\n[+] Continue to calculate ratios/metrics of interest (y, else any key): ')
        if ratios.lower().strip() == 'y':
            rat_matrix = pd.DataFrame(index=stats.index) # initiate ratio matrix with same x-axis i.e. YEARS
            # metric calculations done here
            alpha = 1000000*(stats.iloc[:,10] / stats.iloc[:,0])
            alpha_chg = alpha.pct_change()*100
            beta = 100*(alpha / stats.iloc[:,8])
            beta_chg = beta.pct_change()*100
            gamma = 1000000*(stats.iloc[:,24] / stats.iloc[:,0])
            gamma_chg = gamma.pct_change()*100
            delta = 100*(stats.iloc[:,26] / stats.iloc[:,24])
            delta_chg = delta.pct_change()*100
            epsilon = 100*(stats.iloc[:,20] / (stats.iloc[:,16]*1000))
            epsilon_chg = epsilon.pct_change()*100
            zeta = 1000*(stats.iloc[:,20] / stats.iloc[:,0])
            zeta_chg = zeta.pct_change()*100
            eta = 1000000*(stats.iloc[:,16] / stats.iloc[:,0])
            eta_chg = eta.pct_change()*100
            theta = 100000*(stats.iloc[:,24] / stats.iloc[:,20])
            theta_chg = theta.pct_change()*100
            iota = 100*stats.iloc[:,30].pct_change()
            iota_chg = iota.pct_change()*100
            kappa = stats.iloc[:,32]
            kappa_chg = kappa.pct_change()*100
            lamb = stats.iloc[:,22] / stats.iloc[:,24]
            lamb_chg = lamb.pct_change()*100
            mu = 1000000*(stats.iloc[:,22] / stats.iloc[:,0])
            mu_chg = mu.pct_change()*100
            nu = 100*(stats.iloc[:,22] / stats.iloc[:,16])
            nu_chg = nu.pct_change()*100
            xi = 100*(stats.iloc[:,14] / stats.iloc[:,16])
            xi_chg = xi.pct_change()*100
            rat_dict = {
                'savings/capita_$':alpha.values,
                '%_chg-sav_cap':alpha_chg.values,
                'savings/income_%':beta.values,
                '%_chg-sav_inc':beta_chg.values,
                'taxrev/capita_$':gamma.values,
                '%_chg-taxrev_cap':gamma_chg.values,
                'corptaxrev/taxrev_%':delta.values,
                '%_chg-corptax_tax':delta_chg.values,
                'm2/gdp_%':xi.values,
                '%_chg-m2_gdp':xi_chg.values,
                'debt/gdp_%':epsilon.values,
                '%_chg-debt_gdp':epsilon_chg.values,
                'debt/capita_$':zeta.values,
                '%_chg-debt_cap':zeta_chg.values,
                'gdp/capita_$':eta.values,
                '%_chg-gdp_cap':eta_chg.values,
                'govtexpend/taxrev_x':lamb.values,
                '%_chg-govtexpend_taxrev':lamb_chg.values,
                'govtexpend/capita_$':mu.values,
                '%_chg-govtexpend_capita':mu_chg.values,
                'govtexpend_gdp_%':nu.values,
                '%_chg-govtexpend_gdp':nu_chg.values,
                'taxrev/debt_%':theta.values,
                '%_chg-tax_debt':theta_chg.values,
                'inflation_%':iota.values,
                '%_chg-inflation':iota_chg.values,
                'interest_rate_%':kappa,
                '%_chg-int_rate':kappa_chg.values        
            }
            rats = []
            for rat in rat_dict:
                rat_matrix[rat] = rat_dict[rat]
                rats.append(rat_matrix)
            rats = pd.concat(rats,axis=1)
            # save results to Excel
            rat_matrix.to_excel('us-econ_metrics.xlsx',sheet_name='us-econ_metrics')
            us_econ_rat_corr = rat_matrix.corr()
            us_econ_rat_corr.to_excel('us-econ_metrics_corr.xlsx',sheet_name='us-econ_metrics_corr')
            print(f'\n[*] Results saved to: \n\t[>] us-econ_metrics.xlsx\n\t[>] us-econ_metrics_corr.xlsx')
            ##################################################
            ## PLOTTING GRAPHS HERE
            graphs = input('\n[+] Continue to graph ratios/metrics of interest (y, else any key): ')
            if graphs.lower().strip() == 'y':
                ## two plots. useful to graph stats/ratios with same units to same, respective plot.
                ## plot 1
                f1 = plt.figure(1,figsize=(10,6))
                plt.title('Key Capita Metrics')
                plt.xlabel('Year')
                plt.ylabel('$USD / Capita')
                ticks = np.arange(0, 500000, 10000)
                plt.yticks(ticks)
                # plt.plot(<stat/ratio of interest>,label='<name of stat/ratio of interest')
                plt.plot(alpha,label='Savings per Capita')
                plt.plot(gamma,label='Tax Rev per Capita')
                plt.plot(zeta,label='Debt per Capita')
                plt.plot(eta,label='GDP per Capita')
                plt.plot(mu,label='Govt Expenditure per Capita')
                # ... add more plots as desired
                plt.legend(loc=0)
                plt.savefig('capita_metrics.pdf') # to file
                ## plot 2
                # use same logic in all places as above f1 plot
                f2 = plt.figure(2,figsize=(10,6))
                plt.title('Key Percentage Metrics')
                plt.xlabel('Year')
                plt.ylabel('%')
                ticks = np.arange(0, 200, 10)
                plt.yticks(ticks)
                plt.plot(beta,label='Savings to Income (%)')
                plt.plot(epsilon,label='Debt to GDP (%)')
                plt.plot(nu,label='Govt Expenditure to GDP (%)')
                plt.plot(xi,label='M2 to GDP (%)')
                plt.plot(iota,label='Inflation (%)')
                plt.plot(kappa,label='Interest Rate (%)')                                
                plt.legend(loc=0)
                plt.savefig('percent_metrics.pdf') # to file
                # ... add f3 if more graphs desired, etc.
                ## plot to screen; can also save to file from UI
                plt.show() 
                print('\n[*] Graphs saved to: \n\t[>] capita_metrics.pdf\n\t[>] percent_metrics.pdf')
                print('\n[*] Done!')                
            else:
                print('\n[*] Done!')                
        else:
            print('\n[*] Done!')            
##################################################