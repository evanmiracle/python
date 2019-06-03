# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:57:39 2019

@author: evmira
"""

#looking at long_sample data set
import pandas as pd
import numpy as np

# Assign spreadsheet filename: file
file = 'C:\warehouse\case_study\FF_Case_Data_Set_2014.xlsx'

# Load spreadsheet: xl
ff_xl = pd.ExcelFile(file)

# Print sheet names
print(ff_xl.sheet_names)
# Load a sheet into a DataFrame by name: df_usage
df_ls = ff_xl.parse('long_sample')
df_ls2 = ff_xl.parse('long_sample')
#get list of column names
col_list = list(df_ls)

#loop through and add new column with difference between rows
for i in col_list:
    df_ls[i+'C'] = df_ls[i].diff()
#    did have whitespace that I was putting but also the import cloumn names have it too
    
#    print(df_ls)
#    adds new difference columns with ' C' added to the column name to df_ls 
    
#could sort or try to get > diff do it agian for < a certain value

df_ls['YearC'].idxmax()
#(df['Gold'] - df['Gold.1']).abs().idxmax()
#returns 12

df_ls.iloc[12,0]
           
#this returns the corresponding date value of max difference in the date column
df_ls.iloc[df_ls['YearC'].idxmax(),0]

#can't do whitespace in column name in the query interface which is really a nice to have 
#test = df_ls.query('Year` `C > 2012')
test = df_ls.query('YearC > 0')

#test2 = df_ls.query('3-FraudFinder2.0.C > 10')
#
#  File "<unknown>", line 1
#    3 -FraudFinder2 .0 .C >10
#                     ^
#SyntaxError: invalid syntax
#doesn't like these column names

#either rename columns or upgrade to pandas 0.25 currently have 0.22
for i in col_list:
    df_ls[i+'C'] = df_ls[i].diff()
    df_ls[i+'renew'] = df_ls.iloc[df_ls[i+'C'].idxmax(),0]
#    I've created new columns so the correct aren't in the column list
#    can't do this in one loop
    
    
df_ls_short = df_ls[['2-FraudFinderC']]
col_list_new = list(df_ls_short)

for i in col_list_new:   
    df_ls_short[i+'neg'] = df_ls_short.loc[df_ls[i].values <= -9]
#    df_ls[i+'test']= df_ls.query('i < -10')
#    doesn't work
#    df_ls[i+'test'] = df_ls.iloc[df_ls[i+'C'].where(df_ls[i+'C'] >= 10.0),0]
    #        raise TypeError("invalid type comparison")
#
#TypeError: invalid type comparison
    df_ls[i+'pc'] = df_ls[i].pct_change()
    df_ls[i+'cancel'] = df_ls.iloc[df_ls[i+'C'].idxmin(),0]    
    
#    df_reform_melt_format2 = df_reform_melt_format.astype({"variable_reform": str, "variable": str})
    
df_ls.info()

df_ls_dt = pd.to_datetime(df_ls)

print(col_list)

list(df_ls)

df_ls.loc[df_ls[i+'C'].value >= 10, 0]



