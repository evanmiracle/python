# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:18:26 2019

@author: evmira
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches #for custom legends
import seaborn as sns
from lifelines import KaplanMeierFitter #survival analysis library
from lifelines.statistics import logrank_test #survival statistical testing
from IPython.display import Image
from IPython.core.display import HTML 

def display_all(df):
    with pd.option_context("display.max_rows", 1000): 
        with pd.option_context("display.max_columns", 1000): 
            display(df)
            

url="https://community.watsonanalytics.com/wp-content/uploads/2015/03/WA_Fn-UseC_-Telco-Customer-Churn.csv?cm_mc_uid=51304980933215218170416&cm_mc_sid_50200000=92178841521817041648&cm_mc_sid_52640000=98592221521817041652"
df = pd.read_csv(url)
print(df.shape)
display_all(df.tail().transpose()) 

print(df.head())

#data for survival needs to be in long form
#survival_data_prod   

df["b_Churn"] = df.Churn.apply(lambda x: 1 if x == "Yes" else 0) #recode churn var

df.MultipleLines.value_counts()

#drop "No phone service"
df[df.MultipleLines != "No phone service"]

#recode MultipleLines var to get our two comparison cohorts
df["b_MultipleLines"] = df.MultipleLines.apply(lambda x: 1 if x == "Yes" else 0)

df.tenure.describe()

kmf = KaplanMeierFitter()
T2 = df['tenure'] #duration
C2 = df["b_Churn"] #censorship - 1 if death/churn is seen, 0 if censored


palette = ["windows blue", "amber"]
sns.set_palette(sns.xkcd_palette(palette))

##SET UP PLOT
ax = plt.subplot(111)
plt.title('Kaplan-Meier Estimate of Driver Retention by Multiple Lines')
sns.set_context("talk")

d={} #to store the models
vlines = []
i=0

##PLOT FITTED GRAPH
#loop through segmentation variable, plot on same axes
for segment in df.b_MultipleLines.unique(): 
    ix = df.b_MultipleLines == segment
    d['kmf{}'.format(i+1)] = kmf.fit(T.loc[ix],C.loc[ix], label=segment)
    ax = kmf.plot(ax=ax, figsize=(12,6))

    ax.set_xlim([T.min(),T.max()])
    ax.set_ylim([0.5,1])
    
    y_ = kmf.survival_function_[kmf.survival_function_.round(2) ==.75].dropna().index[0]
    ymax_ = kmf.survival_function_[kmf.survival_function_.round(2) ==.75].dropna()[i][y_]
    
    vlines.append([y_, ymax_])
    i+=1

#output graph  ****************************************
    
#try with my data
    
# Assign spreadsheet filename: file
file = 'C:\warehouse\case_study\survival.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
# Load a sheet into a DataFrame by name: df_s

df_s = xl.parse('survival_na')
 
#may be throwing an error
#churn already coded correctly in data   
df_s["b_churn"] = df_s.churn.apply(lambda x: 1 if x == 1 else 0) #recode churn var

list(df_s)
df_s.describe()

df_s.prd_cd.value_counts()


#drop "4"  not dropping values
df_s[df_s.prd_cd != 4]

#this recoding is flawed

#recode MultipleLines var to get our two comparison cohorts
df_s["b_product"] = df_s.prd_cd.apply(lambda x: 1 if x == 2 else 0)
df_s["b_product"].value_counts()

df_s.tenure.describe()

df_s.churn.describe()

kmf = KaplanMeierFitter()
T = df_s['tenure'] #duration
C = df_s["b_churn"] #censorship - 1 if death/churn is seen, 0 if censored


palette = ["windows blue", "amber", "red"]
sns.set_palette(sns.xkcd_palette(palette))

##SET UP PLOT
ax = plt.subplot(111)
plt.title('Kaplan-Meier Estimate of Customer Retention by Product')
sns.set_context("talk")

d={} #to store the models
vlines = []
i=0

##PLOT FITTED GRAPH
#loop through segmentation variable, plot on same axes
#for segment in df_s.b_product.unique(): 
#    ix = df_s.b_product == segment
#try with prd_cd
for segment in df_s.prd_cd.unique(): 
    ix = df_s.prd_cd == segment
    d['kmf{}'.format(i+1)] = kmf.fit(T.loc[ix],C.loc[ix], label=segment)
    ax = kmf.plot(ax=ax, figsize=(12,6))
#run up to here and it works
    
    ##LEGEND
#override default legend
patches = [ mpatches.Patch(color="xkcd:windows blue", label='FraudFinder 2.0'),
            mpatches.Patch(color="xkcd:amber", label='FraudFinder'),
            mpatches.Patch(color="xkcd:red", label='Other')
          ]
plt.legend(handles=[patches[0],patches[1],patches[2]], title="Product", loc='best');





# Assign spreadsheet filename: file
file = 'C:\warehouse\case_study\survival.xlsx'

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)
# Load a sheet into a DataFrame by name: df_s

df_nz = xl.parse('survival_na_nz')
df_a = xl.parse('active') 
#may be throwing an error
#churn already coded correctly in data   
df_nz["b_churn"] = df_nz.churn.apply(lambda x: 1 if x == 1 else 0) #recode churn var

list(df_nz)
df_nz.describe()

df_nz.prd_cd.value_counts()

df_nz.tenure.describe()

df_nz.churn.describe()

kmf = KaplanMeierFitter()
T = df_nz['tenure'] #duration
C = df_nz["b_churn"] #censorship - 1 if death/churn is seen, 0 if censored


palette = ["windows blue", "amber", "red"]
sns.set_palette(sns.xkcd_palette(palette))

##SET UP PLOT
ax = plt.subplot(111)
plt.title('Kaplan-Meier Estimate of Customer Retention by Product')
sns.set_context("talk")

d={} #to store the models
vlines = []
i=0

##PLOT FITTED GRAPH
#loop through segmentation variable, plot on same axes
#for segment in df_s.b_product.unique(): 
#    ix = df_s.b_product == segment
#try with prd_cd
for segment in df_nz.prd_cd.unique(): 
    ix = df_nz.prd_cd == segment
    d['kmf{}'.format(i+1)] = kmf.fit(T.loc[ix],C.loc[ix], label=segment)
    ax = kmf.plot(ax=ax, figsize=(12,6))
#run up to here and it works
    
    ##LEGEND
#override default legend
patches = [ mpatches.Patch(color="xkcd:windows blue", label='FraudFinder 2.0'),
            mpatches.Patch(color="xkcd:amber", label='FraudFinder'),
            mpatches.Patch(color="xkcd:red", label='Other')
          ]
plt.legend(handles=[patches[0],patches[1],patches[2]], title="Product", loc='best');


df_a.describe()

df_nz_a = df_nz.merge(df_a, left_on='id', right_on='cust_id', how='left')
   
kmf = KaplanMeierFitter()
T = df_nz_a['tenure'] #duration
C = df_nz_a["churn"] #censorship - 1 if death/churn is seen, 0 if censored


palette = ["windows blue", "amber", "red"]
sns.set_palette(sns.xkcd_palette(palette))

##SET UP PLOT
ax = plt.subplot(111)
plt.title('Kaplan-Meier Estimate of Customer Retention by Active Status within 3 years')
sns.set_context("talk")

d={} #to store the models
vlines = []
i=0

##PLOT FITTED GRAPH
#loop through segmentation variable, plot on same axes
#for segment in df_s.b_product.unique(): 
#    ix = df_s.b_product == segment
#try with prd_cd
for segment in df_nz_a.active_3_years.unique(): 
    ix = df_nz_a.active_3_years == segment
    d['kmf{}'.format(i+1)] = kmf.fit(T.loc[ix],C.loc[ix], label=segment)
    ax = kmf.plot(ax=ax, figsize=(12,6))    

patches = [ mpatches.Patch(color="xkcd:windows blue", label='Inactive'),
            mpatches.Patch(color="xkcd:amber", label='Active')
          ]
plt.legend(handles=[patches[0],patches[1]], title="Active Status", loc='best');

multi = (df_nz_a["active_3_years"] == 1)
results = logrank_test(T[multi], T[~multi], C[multi], C[~multi], alpha=0.99 ) #at 99% confidence level
results.print_summary()

Z = results.test_statistic
D = C.sum() #number of events observed

hazard_ratio = np.exp(Z*np.sqrt(4/D))
print(hazard_ratio)
       