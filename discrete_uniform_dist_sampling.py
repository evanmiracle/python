# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:37:41 2019

@author: evmira
"""

import numpy as np

sample = np.random.uniform(1,1000,8)
print(sample)

sample_int = np.random.randint(1000,size=8)
si_mean= np.mean(sample_int)

#deprecated
#sample_int_discrete = np.random.random_integers(1,1000)

sample_int_discrete = np.random.randint(1,1000 +1, size=8)


sample_size = 8
sample_int_discrete_auto = np.random.randint(1,1000 +1, size=sample_size)
estimate_max = np.max(sample_int_discrete_auto)+np.max(sample_int_discrete_auto)/sample_size-1

#because the mean is the same as the mode in a discrete uniform distribution (1,2,3,4,5 for instance)
#if we can find the mean then subtract 1 we'd have a good chance of hitting the true max
estimate_from_mean = np.mean(sample_int_discrete_auto)*2-1

#add items to a list

estimate_list = []
estimate_mean_list = []
number_of_loops = 10
for i in range(number_of_loops):
    sample_int_discrete_auto = np.random.randint(1,1000 +1, size=sample_size)
    estimate_max = round((np.max(sample_int_discrete_auto)+np.max(sample_int_discrete_auto)/sample_size-1),0)
    estimate_list.append(estimate_max)
    estimate_from_mean = np.mean(sample_int_discrete_auto)*2-1
    estimate_mean_list.append(estimate_from_mean)

import pandas as pd

#give a trials number could just use index but is nice to have
trials = list(range(10))
#print(trials)

#this is not the inteded result
estimate_dict = dict(zip(estimate_list,estimate_mean_list))
#this sets the index as the first list so could do (trials,estimate_list, estimate_mean_list)
#df = pd.DataFrame(estimate_list, estimate_mean_list)

#build a dictionary to build a dataframe
my_dict= {'trials':trials,'estimate_mve':estimate_list,'mean_double':estimate_mean_list}
df_est = pd.DataFrame(my_dict)

df_est.describe()