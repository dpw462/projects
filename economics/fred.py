import numpy as np
import pandas as pd
import datetime
from pandas_datareader import data as pdr

start = datetime.datetime(1960,1,1)
end = datetime.datetime(2020,12,31)

gdp = pdr.DataReader('fygdp','fred',start,end)
gdp.index = pd.to_datetime(gdp.index)
gdp['year'] = gdp.index.year
gdp_ann = gdp.groupby(['year']).mean().round()

cpi = pdr.DataReader('cpiaucns','fred',start,end)
cpi.index = pd.to_datetime(cpi.index)
cpi['year'] = cpi.index.year
cpi_ann = cpi.groupby(['year']).mean().round()

tax_returns = pdr.DataReader('tlinctx','fred',start,end)
tax_returns.index = pd.to_datetime(tax_returns.index)
tax_returns['year'] = tax_returns.index.year
tax_rtn_ann = tax_returns.groupby(['year']).mean().round()

tax_rates = pdr.DataReader('iittrhb','fred',start,end)
tax_rates.index = pd.to_datetime(tax_rates.index)
tax_rates['year'] = tax_rates.index.year
tax_rates_ann = tax_rates.groupby(['year']).mean().round()

tax_receipt_corp = pdr.DataReader('fctax','fred',start,end)
tax_receipt_corp.index = pd.to_datetime(tax_receipt_corp.index)
tax_receipt_corp['year'] = tax_receipt_corp.index.year
tax_receipt_corp_ann = tax_receipt_corp.groupby(['year']).mean().round()

govt_tot_exp = pdr.DataReader('W068RC1A027NBEA','fred',start,end)
govt_tot_exp.index = pd.to_datetime(govt_tot_exp.index)
govt_tot_exp['year'] = govt_tot_exp.index.year
govt_tot_exp_ann = govt_tot_exp.groupby(['year']).mean().round()

tot_nonfarm = pdr.DataReader('paynsa','fred',start,end)
tot_nonfarm.index = pd.to_datetime(tot_nonfarm.index)
tot_nonfarm['year'] = tot_nonfarm.index.year
tot_nonfarm_ann = tot_nonfarm.groupby(['year']).mean().round()

unrate = pdr.DataReader('unratensa','fred',start,end)
unrate.index = pd.to_datetime(unrate.index)
unrate['year'] = unrate.index.year
unrate_ann = unrate.groupby(['year']).mean().round()

debt = pdr.DataReader('gfdebtn','fred',start,end)
debt.index = pd.to_datetime(debt.index)
debt['year'] = debt.index.year
debt_ann = debt.groupby(['year']).mean().round()

pipc = pdr.DataReader('A792RC0A052NBEA','fred',start,end)
pipc.index = pd.to_datetime(pipc.index)
pipc['year'] = pipc.index.year
pipc_ann = pipc.groupby(['year']).mean().round()

psave = pdr.DataReader('A071RC1A027NBEA','fred',start,end)
psave.index = pd.to_datetime(psave.index)
psave['year'] = psave.index.year
psave_ann = psave.groupby(['year']).mean().round()

df = pd.DataFrame(psave_ann)
df.columns=['savings']
df['personal_income_per_capita'] = pipc_ann
df['unemployment'] = unrate_ann
df['total_nonfarm'] = tot_nonfarm_ann
df['govt_tot_exp'] = govt_tot_exp_ann
df['tax_receipts_corp'] = tax_receipt_corp_ann
df['tax_rate'] = tax_rates_ann
df['gdp'] = gdp_ann 
df['cpi'] = cpi_ann
df['tax_returns'] = tax_rtn_ann

print(df)

#df.to_excel('us_econ.xlsx')
