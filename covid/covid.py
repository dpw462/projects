import numpy as np
import pandas as pd

df = pd.read_csv('us-states.csv')
states = ['California','Florida','Texas','South Dakota','New York','Iowa','Washington']
state_pop = {'California':40000000,'Florida':22000000,'Texas':30000000,'South Dakota':1000000,'New York':20000000,'Iowa':3000000,'Washington':8000000}

for state in states:
    case_delta = df[df['state']==state]['cases'].pct_change()
    case_rate = round(100*case_delta.mean(),2)
    case_rate_med = round(100*case_delta.median(),2)
    print(f'\n{state} mean case rate (i.e. pct chg): {case_rate}')
    print(f'{state} median case rate (i.e. pct chg): {case_rate_med}')
    
    inc_delta = (df[df['state']==state]['cases'] - df[df['state']==state]['cases'].shift(1)) / state_pop[state]
    incidence = round(100000*inc_delta.mean())
    inc_med = round(100000*inc_delta.median())
    print(f'{state} mean incidence (per 100k): {incidence}')
    print(f'{state} median incidence (per 100k): {inc_med}')
    
    death_delta = df[df['state']==state]['deaths'].pct_change() 
    death_rate = round(100*death_delta.mean(),2)
    death_rate_med = round(100*death_delta.median(),2)
    print(f'{state} mean death rate (i.e. pct chg): {death_rate}')
    print(f'{state} median death rate (i.e. pct chg): {death_rate_med}')

print(df.groupby(['state']).median())
