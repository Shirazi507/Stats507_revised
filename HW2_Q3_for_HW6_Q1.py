#!/usr/bin/env python
# coding: utf-8

# ## HW2_Q3
# 
# __Note:__ in this question, cohorts 1 to 4 belong to the years 2011-2012, 2013-2014, 2015-2016 and 2017-2018, respectively.

# In[1]:


import numpy as np
import pandas as pd
from collections import defaultdict


# In[2]:


cols = ['SEQN','RIDAGEYR','RIDRETH3','DMDEDUC2','DMDMARTL',
        'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']

col_names=['unique ids','age','race and ethnicity','education','marital status',
           'exam_status','masked variance pseudo', 'masked variance pseudo-stratum',
           '2 year MEC exam weight','2 year interview weight']

files=['G','H','I','J']
demo_df=pd.DataFrame()

for i in range(1,5):
    read_path=r'https://wwwn.cdc.gov/Nchs/Nhanes/'+ str(2010+(2*i-1))+'-'+str(2010+2*i)+'/DEMO_'+files[i-1]+'.XPT'
    df = pd.read_sas(read_path)[cols]
    df.columns = col_names
    df["cohort"] = np.ones(len(df))*i
    df=df.convert_dtypes()
    demo_df = demo_df.append(df).reset_index(drop=True)

demo_df.to_pickle(r"DEMO_HW2.pkl")


# In[3]:


cols=['SEQN','OHDDESTS']+[
    'OHX0'+str(i)+'TC' for i in range(1,10)]+ [
    'OHX'+str(i)+'TC' for i in range(10,33)]+[
    'OHX0'+str(i)+'CTC' for i in range(2,10)]+[
    'OHX'+str(i)+'CTC' for i in range(10,32)]

cols.remove('OHX16CTC')
cols.remove('OHX17CTC')

col_names=['unique ids','status']+[
    'tooth Count #'+str(i) for i in range(1,10)]+ [
    'tooth Count #'+str(i) for i in range(10,33)]+[
    'coronal cavities #'+str(i) for i in range(2,10)]+[
    'coronal cavities #'+str(i) for i in range(10,32)]

col_names.remove('coronal cavities #16')
col_names.remove('coronal cavities #17')

files=['G','H','I','J']
oral_df=pd.DataFrame()

for i in range(1,5):
    read_path=r'https://wwwn.cdc.gov/Nchs/Nhanes/'+str(2010+(2*i-1))+'-'+str(2010+2*i)+'/OHXDEN_'+files[i-1]+'.XPT'
    df = pd.read_sas(read_path)[cols]
    df.columns = col_names
    df["cohort"] = np.ones(len(df))*i
    df=df.convert_dtypes()
    oral_df = oral_df.append(df).reset_index(drop=True)

oral_df.to_pickle(r"ORAL_HW2.pkl")

