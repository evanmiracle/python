# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:34:51 2019

@author: evmira
"""
#load data into pandas
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\warehouse\case_study\FF_Case_Data_Set_2014.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
# Load a sheet into a DataFrame by name: df_usage
df_usage = xl.parse('Usage_reform')

# Print the head of the DataFrame df_usage
print(df_usage.head())


#df1.merge(airports[airports.ident == 'KLAX'][['id']], left_on='airport_ref', right_on='id', how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]

#select two columns only
df_usage_10 = df_usage[['Customer_2010', 'transactions_2010']].rename(columns={'Customer_2010':'cust_id'})
#print(df_useage_10.head())
print(df_usage_10.shape)
df_usage_11 = df_usage[['Customer_2011', 'transactions_2011']].rename(columns={'Customer_2011':'cust_id'})
#print(df_useage_11.head())
print(df_usage_11.shape)
df_usage_12 = df_usage[['Customer_2012', 'transactions_2012']].rename(columns={'Customer_2012':'cust_id'})
print(df_usage_12.shape)
#merge one two column set at a time  issue of missing rows not all customers present in all years need to make a unique list first
#df_useage_merge= df_useage_10.merge(df_useage_11, left_on='Customer_2010', right_on='Customer_2011', how='left')

#stack customer columns then drop dups
#gapminder.rename(columns={'pop':'population'}, inplace=True)
df_cust_append = df_usage_10.append(df_usage_11.append(df_usage_12, ignore_index=True), ignore_index=True)
print(df_cust_append.head(10))
print(df_cust_append.shape)
df_cust_id = df_cust_append[['cust_id']].drop_duplicates(keep='first', inplace=False)

print(df_cust_id.shape)

df_cust_id2 = df_cust_id.dropna().reset_index(drop=True).sort_values(by=['cust_id'])
#print(df_useage_merge.head(n=20))
print(df_cust_id.tail(5))

df_usage_102 = df_usage[['Customer_2010', 'transactions_2010']]
#print(df_useage_10.head())
print(df_usage_102.shape)
df_usage_112 = df_usage[['Customer_2011', 'transactions_2011']]
#print(df_useage_11.head())
print(df_usage_112.shape)
df_usage_122 = df_usage[['Customer_2012', 'transactions_2012']]
print(df_usage_122.shape)

#df_usage_merge= df_cust_id2.merge(df_usage_102, left_on='cust_id', right_on='Customer_2010', how='left')
#print(df_usage_merge.shape)
#print(df_cust_append)

#we have duplicates in the usage data for the same year see 2010 899 

############cust id2 is 2286 rows after drop the nan
#but merge with 2061 row 2010 table is 2313
#print(df_usage_102['Customer_2010'].value_counts(dropna=False))
#print(df_usage_112['Customer_2011'].value_counts(dropna=False))
#print(df_usage_122['Customer_2012'].value_counts(dropna=False))
#highest is 3
#need to sum the duplicate rows here

#sum check
#print(df_usage_102[df_usage_102.Customer_2010 == 'CUSTOMER 1399' ].groupby('Customer_2010').transactions_2010.apply(lambda g: g.nlargest(4).sum()))
#print(df_usage_102[df_usage_102.Customer_2010 == 'CUSTOMER 1399' ].groupby('Customer_2010').transactions_2010.nlargest(4))

#create data frame from the series resulting from the groupby and sum of n largest values
dfu103 = pd.DataFrame(df_usage_102.groupby('Customer_2010').transactions_2010.apply(lambda g: g.nlargest(4).sum()))
df_usage_merge2= df_cust_id2.merge(dfu103, left_on='cust_id', right_index=True, how='left')
print(df_usage_merge2.shape)
#results in the correct number of rows (2286) and spot checked 1399
dfu113 = pd.DataFrame(df_usage_112.groupby('Customer_2011').transactions_2011.apply(lambda g: g.nlargest(4).sum()))
df_usage_merge3= df_usage_merge2.merge(dfu113, left_on='cust_id', right_index=True, how='left')
#2286 rows 3 columns
dfu123 = pd.DataFrame(df_usage_122.groupby('Customer_2012').transactions_2012.apply(lambda g: g.nlargest(4).sum()))
df_usage_merge4= df_usage_merge3.merge(dfu123, left_on='cust_id', right_index=True, how='left')
#2286 and 4 rows





df_usage_merge4['A_perc'] = df['A']/df['sum']
data['column_c'] = data['column_a'].where(data['column_a'] == 0, data['column_b'])
df_usage_merge4['d'] = df_usage_merge4['transactions_2010'].where(df_usage_merge4['transactions_2010'] > 0 , df_useage_merge4['transactions_2011']  )

def valuation_formula(x, y):
    return x * y * 0.5

df_usage_merge4['price'] = df_usage_merge4.apply(lambda row: valuation_formula(row['transactions_2010'], row['transactions_2011']), axis=1)
#define a function to create the derived values and a lambda function applied to the dataframe


import numpy as np

#could define scenarios as functions with def
def new_cust(x, y):
    if np.isnan(x)==True and y >= 0:
        new_2011 = 'True'
    else:
        new_2011 = 'False'
    return new_2011

df_usage_merge4['new_2011'] = df_usage_merge4.apply(lambda row: new_cust(row['transactions_2010'], row['transactions_2011']), axis=1)


#get summary stats
df_usage_merge4.describe()
#or as varaibles with np.logical this works for two varaible columns only
pick = np.logical_or(df_usage_merge4['transactions_2010'] == 0, 
                     df_usage_merge4['transactions_2011'] == 0)

df_usage_merge4[pick]

new_2012 = np.logical_and(df_usage_merge4['transactions_2010'] == 0, 
                     df_usage_merge4['transactions_2011'] >= 0)
#                     df_usage_merge4['transactions_2012'] == 354)
                     

df_usage_merge4[new_2012]

#This works for matching on values of the three columns and setting a new variable value
#True==0
#new_2012 if both 2010 and 2011 are missing and we have transactions in 2012
df_usage_merge4.loc[(np.isnan(df_usage_merge4['transactions_2010'])==True) & (np.isnan(df_usage_merge4['transactions_2011'])==True) & (df_usage_merge4['transactions_2012'] >= 0),'new_2012'] = 'True'


#new_2011 if 2010 is missing and we have transactions in 2011   this doesn't work think the function may be the easiest 
df_usage_merge4.loc[(np.isnan(df_usage_merge4['transactions_2010'])==True) & (df_usage_merge4['transactions_2011'] >= 0),'new_2011'] = 'True'


def new_cust_2011(x, y):
    if np.isnan(x)==True and y >= 0:
        new_2011 = 'True'
    else:
        new_2011 = 'False'
    return new_2011

df_usage_merge4['new_2011'] = df_usage_merge4.apply(lambda row: new_cust_2011(row['transactions_2010'], row['transactions_2011']), axis=1)

def new_cust_2012(x, y):
    if np.isnan(x)==True and np.isnan(y)==True:
        new_2012 = 'True'
    else:
        new_2012 = 'False'
    return new_2012


df_usage_merge4['new_2012'] = df_usage_merge4.apply(lambda row: new_cust_2012(row['transactions_2010'], row['transactions_2011']), axis=1)

#just using this works fine as we get no 
#df_usage_merge4.loc[df_usage_merge4['new_2012']=='True']
#df.loc[df['column_name'] == some_value]

#write out to excel
df_usage_merge4.to_excel('aggragated_usage2.xlsx')


def cancelled_2011(x, y):
    if x >= 0 and np.isnan(y)==True:
        cancel_2011 = 'True'
    else:
        cancel_2011 = 'False'
    return cancel_2011


df_usage_merge4['cancel_2011'] = df_usage_merge4.apply(lambda row: cancelled_2011(row['transactions_2010'], row['transactions_2011']), axis=1)


def cancelled_2012(x, y):
    if x >= 0 and np.isnan(y)==True:
        cancel_2012 = 'True'
    else:
        cancel_2012 = 'False'
    return cancel_2012


df_usage_merge4['cancel_2012'] = df_usage_merge4.apply(lambda row: cancelled_2012(row['transactions_2011'], row['transactions_2012']), axis=1)



def active_2010(x):
    if x > 0:
        active_2010 = 'True'
    else:
        active_2010 = 'False'
    return active_2010


df_usage_merge4['active_2010'] = df_usage_merge4.apply(lambda row: active_2010(row['transactions_2010']), axis=1)


def active_2011(x):
    if x > 0:
        active_2011 = 'True'
    else:
        active_2011 = 'False'
    return active_2011


df_usage_merge4['active_2011'] = df_usage_merge4.apply(lambda row: active_2011(row['transactions_2011']), axis=1)


def active_2012(x):
    if x > 0:
        active_2012 = 'True'
    else:
        active_2012 = 'False'
    return active_2012


df_usage_merge4['active_2012'] = df_usage_merge4.apply(lambda row: active_2012(row['transactions_2012']), axis=1)

#write out to excel
df_usage_merge4.to_excel('aggragated_usage3.xlsx')


#load data into pandas
# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\warehouse\case_study\FF_Case_Data_Set_2014.xlsx'

# Load spreadsheet: xl
xl2 = pd.ExcelFile(file)

# Print sheet names
print(xl2.sheet_names)
# Load a sheet into a DataFrame by name: df_usage
df_reform = xl2.parse('Revenue_reform')

# Print the head of the DataFrame df_usage
print(df_reform.head())

#select just product 2
df_reform_2 = df_reform.loc[df_reform['prod_grp_code']==2]

print(df_reform_2['Cust_ID'].value_counts(dropna=False))

df_usage_merge5= df_usage_merge4.merge(df_reform_2, left_on='cust_id', right_on='Cust_ID', how='right')

df_usage_merge5.loc[df_usage_merge5[0:][1]]
Is_gt_0 = df_usage_merge5["total_revenue_2010"] > 0

df_usage_merge5[Is_gt_0].total_revenue_2010.plot('hist', bins = 50)

#this syntax works to limit the min and max
trans_gt_0 = (df_usage_merge5["transactions_2010"] < 2.5e7) & (df_usage_merge5["transactions_2010"] > 1000)


df_usage_merge5[trans_gt_0].transactions_2010.plot('hist')

import matplotlib.pyplot as plt

plt.scatter(df_usage_merge5["transactions_2010"], df_usage_merge5["transactions_2011"])

# Put the x-axis on a logarithmic scale
#plt.xscale('log')

# Show plot
plt.show()

plt.scatter(df_usage_merge5["transactions_2010"], df_usage_merge5["transactions_2011"])

plt.show()

#easiest way to make a calculated column  malke revenue per transaction by year
df_usage_merge5['rpt_2010'] = df_usage_merge5['total_revenue_2010'] / df_usage_merge5['transactions_2010'] 
df_usage_merge5['rpt_2011'] = df_usage_merge5['total_revenue_2011'] / df_usage_merge5['transactions_2011']
df_usage_merge5['rpt_2012'] = df_usage_merge5['total_revenue_2012'] / df_usage_merge5['transactions_2012']
#df_usage_merge5['inactive_all'] = df_usage_merge5['active_2010'] +  df_usage_merge5['active_2011'] +  df_usage_merge5['active_2012'] 

df_usage_merge5.to_excel('aggragated_usage5.xlsx')

def inactive(x):
    if np.isnan(x)==True:
        inactive_all = 'True'
    else:
        inactive_all = 'False'
    return inactive_all


df_usage_merge5['inactive'] = df_usage_merge5.apply(lambda row: inactive(row['new_2011']), axis=1)

#def active_2011(x):
#    if x > 0:
#        active_2011 = 'True'
#    else:
#        active_2011 = 'False'
#    return active_2011
#
#
#df_usage_merge4['active_2011'] = df_usage_merge4.apply(lambda row: active_2011(row['transactions_2011']), axis=1)

df_usage_merge5.to_excel('aggragated_usage5.xlsx')

totals=[df_usage_merge5['transactions_2010'],df_usage_merge5['transactions_2011'],df_usage_merge5['transactions_2012']]
df_usage_merge5['total']=df_usage_merge5['transactions_2010'].fillna(0)+df_usage_merge5['transactions_2011'].fillna(0)+df_usage_merge5['transactions_2012'].fillna(0)

print(df_usage_merge5['inactive_all'].value_counts(dropna=False))
#TrueTrueTrue       880
#NaN                509
#FalseFalseTrue     476
#FalseTrueTrue      350
#FalseFalseFalse    246
#TrueTrueFalse      116
#TrueFalseFalse     104
#FalseTrueFalse      33
#TrueFalseTrue       11
print(df_reform_2['prod_grp_code'].value_counts(dropna=False))
#2    2725

print(df_reform['prod_grp_code'].value_counts(dropna=False))
#
#2    2725
#1    2544
#4     541

#slice original reform to get just grpcode and custID
df_sub = df_reform.loc[:,['prod_grp_code','Cust_ID']]
constant_column = "prod_grp_code"
#pivot to get three columns for the products each unique customer has
df_reform_pivot = df_sub.pivot(index='Cust_ID', columns=constant_column, values='prod_grp_code') 

df_reform_pivot['total_code']=df_reform_pivot[1].fillna(0)+df_reform_pivot[2].fillna(0)+df_reform_pivot[4].fillna(0)
print(df_reform_pivot['total_code'].value_counts(dropna=False))
#2.0    1386
#1.0    1288
#3.0     951
#5.0     220
#6.0     176
#4.0     137

#according to revenue numbers customers paying for 
#2.0    1386
#1.0    1288
#3.0     943
#6.0     220
#7.0     176
#5.0     137
#4.0       8

#check for trans with no revenue

#merge4 has the unique usage cust numbers
df_use_rev = df_usage_merge4.merge(df_reform_pivot, left_on='cust_id', right_index=True, how='left')
df_use_rev['check']= np.where(np.isnan(df_use_rev['total_code'])==True, 'yes', 'no')
#np.isnan(x)==True

print(df_use_rev['check'].value_counts(dropna=False))
df_rev_use = df_usage_merge4.merge(df_reform_pivot, left_on='cust_id', right_index=True, how='right')

print(df_rev_use['active_2012'].value_counts(dropna=False))
#asproxy for rev but no transactions
#NaN      1872
#True     1763
#False     523





df_reform_melt = pd.melt(frame=df_reform, id_vars=['Cust_ID', 'Product Group', 'cust_id_prod_grp', 'prod_grp_code'])
df_reform_melt.describe()

#write out to excel
df_reform_melt.to_excel('reform_melt.xlsx')

#need to reformat the date values in variable  chnaged to text number value
########## actually can avoid this step by excplitly setting type




import pandas as pd

# Assign spreadsheet filename: file
file = 'C:\\warehouse\\case_study\\reform_melt_format.xlsx'
#get error unless double escape the path
# Load spreadsheet: xl
x2 = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df_reform_melt_format
df_reform_melt_format = x2.parse('Sheet1')

# Print the head of the DataFrame df_usage
print(df_reform_melt_format.head())

#was getting errors witht eh datetime varaible value for the agg fucntion
#reformated in excel and reimported


df_reform_melt_format.dtypes
df_reform_melt_format2 = df_reform_melt_format.astype({"variable_reform": str, "variable": str})
df_reform_melt_format2.dtypes

#default agg is np.mean  we want sum
df_reform_agg = df_reform_melt_format2.pivot_table(values='value',
                                      index='Cust_ID',
                                      columns='variable',
#                                      columns='variable_reform',
                                      aggfunc=np.sum)

#join transactions to this

df_ra_use2 = df_reform_agg.merge(df_usage_merge4, left_index=True, right_on='cust_id', how='left')
#now join with reform_pivot index to index

df_ra_use_full = df_ra_use2.merge(df_reform_pivot, left_on='cust_id', right_index=True, how='left')