import numpy as np
import pandas as pd
import datetime
from pandas_datareader import data as pdr

start = datetime.datetime(1960,1,1)
end = datetime.datetime(2020,12,31)

gdp = pdr.DataReader('fygdp','fred',start,end)
gdp.index = pd.to_datetime(gdp.index)
gdp['year'] = gdp.index.year
gdp_ann = gdp.groupby(['year']).mean().round(3)

cpi = pdr.DataReader('cpiaucns','fred',start,end)
cpi.index = pd.to_datetime(cpi.index)
cpi['year'] = cpi.index.year
cpi_ann = cpi.groupby(['year']).mean().round(3)

tax_rates = pdr.DataReader('iittrhb','fred',start,end)
tax_rates.index = pd.to_datetime(tax_rates.index)
tax_rates['year'] = tax_rates.index.year
tax_rates_ann = tax_rates.groupby(['year']).mean().round(3)

tax_receipt_corp = pdr.DataReader('fctax','fred',start,end)
tax_receipt_corp.index = pd.to_datetime(tax_receipt_corp.index)
tax_receipt_corp['year'] = tax_receipt_corp.index.year
tax_receipt_corp_ann = tax_receipt_corp.groupby(['year']).mean().round(3)

govt_tot_exp = pdr.DataReader('W068RC1A027NBEA','fred',start,end)
govt_tot_exp.index = pd.to_datetime(govt_tot_exp.index)
govt_tot_exp['year'] = govt_tot_exp.index.year
govt_tot_exp_ann = govt_tot_exp.groupby(['year']).mean().round(3)

tot_nonfarm = pdr.DataReader('paynsa','fred',start,end)
tot_nonfarm.index = pd.to_datetime(tot_nonfarm.index)
tot_nonfarm['year'] = tot_nonfarm.index.year
tot_nonfarm_ann = tot_nonfarm.groupby(['year']).mean().round(3)

unrate = pdr.DataReader('unratensa','fred',start,end)
unrate.index = pd.to_datetime(unrate.index)
unrate['year'] = unrate.index.year
unrate_ann = unrate.groupby(['year']).mean().round(3)

debt = pdr.DataReader('gfdebtn','fred',start,end)
debt.index = pd.to_datetime(debt.index)
debt['year'] = debt.index.year
debt_ann = debt.groupby(['year']).mean().round(3)

pipc = pdr.DataReader('A792RC0A052NBEA','fred',start,end)
pipc.index = pd.to_datetime(pipc.index)
pipc['year'] = pipc.index.year
pipc_ann = pipc.groupby(['year']).mean().round(3)

psave = pdr.DataReader('A071RC1A027NBEA','fred',start,end)
psave.index = pd.to_datetime(psave.index)
psave['year'] = psave.index.year
psave_ann = psave.groupby(['year']).mean().round(3)

fed_funds = pdr.DataReader('fedfunds','fred',start,end)
fed_funds.index = pd.to_datetime(fed_funds.index)
fed_funds['year'] = fed_funds.index.year
fed_funds_ann = fed_funds.groupby(['year']).mean().round(3)

libor = pdr.DataReader('USD3MTD156N','fred',start,end)
libor.index = pd.to_datetime(libor.index)
libor['year'] = libor.index.year
libor_ann = libor.groupby(['year']).mean().round(3)

home_owner = pdr.DataReader('RHORUSQ156N','fred',start,end)
home_owner.index = pd.to_datetime(home_owner.index)
home_owner['year'] = home_owner.index.year
home_owner_ann = home_owner.groupby(['year']).mean().round(3)

retail_inv_rev = pdr.DataReader('RETAILIRNSA','fred',start,end)
retail_inv_rev.index = pd.to_datetime(retail_inv_rev.index)
retail_inv_rev['year'] = retail_inv_rev.index.year
retail_inv_rev_ann = retail_inv_rev.groupby(['year']).mean().round(3)

manu_inv_rev = pdr.DataReader('MNFCTRIRNSA','fred',start,end)
manu_inv_rev.index = pd.to_datetime(manu_inv_rev.index)
manu_inv_rev['year'] = manu_inv_rev.index.year
manu_inv_rev_ann = manu_inv_rev.groupby(['year']).mean().round(3)

natgas = pdr.DataReader('NATURALGASD11','fred',start,end)
natgas.index = pd.to_datetime(natgas.index)
natgas['year'] = natgas.index.year
natgas_ann = natgas.groupby(['year']).mean().round(3)

employ_pop_ratio = pdr.DataReader('LNU02300000','fred',start,end)
employ_pop_ratio.index = pd.to_datetime(employ_pop_ratio.index)
employ_pop_ratio['year'] = employ_pop_ratio.index.year
employ_pop_ratio_ann = employ_pop_ratio.groupby(['year']).mean().round(3)

pop_20to24 = pdr.DataReader('LNU00000036','fred',start,end)
pop_20to24.index = pd.to_datetime(pop_20to24.index)
pop_20to24['year'] = pop_20to24.index.year
pop_20to24_ann = pop_20to24.groupby(['year']).mean().round(3)

pop_25to54 = pdr.DataReader('LNU00000060','fred',start,end)
pop_25to54.index = pd.to_datetime(pop_25to54.index)
pop_25to54['year'] = pop_25to54.index.year
pop_25to54_ann = pop_25to54.groupby(['year']).mean().round(3)

tot_pop = pdr.DataReader('pop','fred',start,end)
tot_pop.index = pd.to_datetime(tot_pop.index)
tot_pop['year'] = tot_pop.index.year
tot_pop_ann = tot_pop.groupby(['year']).mean().round(3)

df = pd.DataFrame(tot_pop_ann)
df.columns = ['total_population (k)']
df['%_chg1'] = tot_pop_ann.pct_change()
df['pop: 25 to 54 (k)'] = pop_25to54_ann
df['%_chg2'] = pop_25to54_ann.pct_change()
df['pop: 20 to 24 (k)'] = pop_20to24_ann
df['%_chg3'] = pop_20to24_ann.pct_change()
df['employ/pop ratio (%)'] = employ_pop_ratio_ann
df['%_chg4'] = employ_pop_ratio_ann.pct_change()
df['nat_gas_consumption (BCF)'] = natgas_ann
df['%_chg5'] = natgas_ann.pct_change()
df['manufacturing: inv/rev'] = manu_inv_rev_ann
df['%_chg6'] = manu_inv_rev_ann.pct_change()
df['retail: inv/rev'] = retail_inv_rev_ann
df['%_chg7'] = retail_inv_rev_ann.pct_change()
df['home_ownership (%)'] = home_owner_ann
df['%_chg8'] = home_owner_ann.pct_change()
df['three_month_LIBOR (% USD)'] = libor_ann
df['%_chg9'] = libor_ann.pct_change()
df['fed_funds_rate (%)'] = fed_funds_ann
df['%_chg10'] = fed_funds_ann.pct_change()
df['personal_savings ($B)'] = psave_ann
df['%_chg11'] = psave_ann.pct_change()
df['total_debt ($M)'] = debt_ann
df['%_chg12'] = debt_ann.pct_change()
df['income_percapita ($)'] = pipc_ann
df['%_chg13'] = pipc_ann.pct_change()
df['unemployment (%)'] = unrate_ann
df['%_chg14'] = unrate_ann.pct_change()
df['total_nonfarm (k persons)'] = tot_nonfarm_ann
df['%_chg15'] = tot_nonfarm_ann.pct_change()
df['govt_tot_exp ($B)'] = govt_tot_exp_ann
df['%_chg16'] = govt_tot_exp_ann.pct_change()
df['tax_receipts_corp ($B)'] = tax_receipt_corp_ann
df['%_chg17'] = tax_receipt_corp_ann.pct_change()
df['tax_rate (%)'] = tax_rates_ann
df['%_chg18'] = tax_rates_ann.pct_change()
df['gdp ($B)'] = gdp_ann 
df['%_chg19'] = gdp_ann.pct_change()
df['cpi (indx 1982-1984 = 100)'] = cpi_ann
df['%_chg20'] = cpi_ann.pct_change()

print(df)
#df.to_excel('us_econ.xlsx',sheet_name='us_econ')