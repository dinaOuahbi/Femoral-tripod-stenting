#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# READ
df = pd.read_excel('../data/Trepied endo stats.xlsx')


# In[3]:


# DROP
df.drop([j for j in [str(i) for i in df.columns] if j.startswith('Unnamed')][0],
        axis=1,
       inplace=True)


# In[4]:


# check NAN
df.isna().sum().sort_values(ascending=False)[:40]


# In[5]:


# set ID as INDEX
df.set_index('ID', inplace=True)


# In[6]:


# subsets
int_df = df.select_dtypes('int64') #
float_df = df.select_dtypes('float64') #
object_df = df.select_dtypes('object')
dt_df = df.select_dtypes('datetime64')


# ### INT 

# In[7]:


to_int = ['Age', 'Créatinine', 'DFG', 'Durée procédure']
for col in int_df:
    if col not in to_int:
        int_df[col]=int_df[col].astype('object')


# ### FLOAT

# In[8]:


to_obj = ['Rutherford M12',
          '12ECHEC = PSVr > 2,4',
          '12PERMEABLE',
          'Rutherford M2',
          '2ECHEC = PSVr > 2,4',
          '2PERMEABLE',
          2,
         '3a',
         '3b',
          '3c',
         '4a',
          '4b',
         '4c']

for col in float_df:
    if col in to_obj:
        float_df[col]=float_df[col].astype('object')


# ### OBJECT 

# In[9]:


def to_nan(col, data):
    temp = []
    for val in data[col]:
        if val in ('NC','PERDU DE VU', 'DC', 'Récupérer CD'):
            temp.append(np.nan)
        else:
            temp.append(val)
    return temp


# In[10]:


for col in object_df:
    object_df[col]=to_nan(col, object_df)


# In[11]:


to_float = ['IPS M12',
           'IPS M2',
           'IPS1',
           'PDS',
           'IPS',
           'HbA1c',
           'PSV',
           'Contraste',
           'Durée scopie']


# In[12]:


for col in object_df:
    if col in to_float:
        object_df[col]=object_df[col].astype('float')


# ### MERGE

# In[13]:


dt_df.reset_index(inplace=True)
float_df.reset_index(inplace=True)
object_df.reset_index(inplace=True)
int_df.reset_index(inplace=True)


# In[14]:


import functools
dfs = [dt_df, float_df, object_df, int_df]
final_df = functools.reduce(lambda left, right: pd.merge(left,right,on='ID'), dfs)


# In[16]:


#final_df.set_index('ID', inplace=True)


# In[15]:





# In[16]:


# CHECK FOR INTEREKSTING GROUPES
pd.crosstab(final_df['Sur ballon'], final_df['Autoexpansible'])


# In[17]:


# dep variable
final_df['stenting_method'] = final_df['Sur ballon'].map({1:'SB', 0:'AE'})


# In[18]:


# drop
final_df.drop(['Sur ballon','Autoexpansible'], axis=1, inplace=True)


# In[26]:


#final_df.to_csv('/work/shared/ptbc/Dina/prestations/Stenting_CCB/Donnees/processed_df.csv', index=False)


# In[19]:


to_drop = ['2PERMEABLE','1PERMEABLE','12PERMEABLE', 'Procédure', 'Azema1']
final_df.drop(to_drop, axis=1, inplace=True)


# In[20]:


final_df['1ECHEC = PSVr > 2,4']=final_df['1ECHEC = PSVr > 2,4'].map({1:'ECHEC', 0:'PERMEABLE'})
final_df['2ECHEC = PSVr > 2,4']=final_df['2ECHEC = PSVr > 2,4'].map({1.0:'ECHEC', 0.0:'PERMEABLE'})
final_df['12ECHEC = PSVr > 2,4']=final_df['12ECHEC = PSVr > 2,4'].map({1.0:'ECHEC', 0.0:'PERMEABLE'})


# In[21]:


final_df.dtypes.value_counts()


# In[22]:


final_df.set_index('ID', inplace=True)


# In[23]:


for col in final_df.select_dtypes('int64'):
    final_df[col] = final_df[col].astype('float')


# In[25]:


final_df.head()


# In[35]:


plt.figure(figsize=(17, 8))
mask = np.triu(np.ones_like(final_df.corr(), dtype=np.bool))
heatmap = sns.heatmap(final_df.select_dtypes('float').corr(), mask=mask, vmin=-1, vmax=1, annot=False, cmap='BrBG')
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=16)
plt.savefig('../results/heatmap.jpeg', dpi=300, bbox_inches='tight')


# In[88]:


# feature correlated with groupes
dataframe.corr()[['stenting_method']].sort_values(by='Sale Price', ascending=False)


# In[40]:


88/2


# In[41]:


import missingno as msno
import matplotlib.pyplot as plt
#msno.matrix(final_df)
msno.matrix(final_df.iloc[:, :47])
plt.savefig('../results/nan1.jpeg')
msno.matrix(final_df.iloc[:, 47:])
plt.savefig('../results/nan2.jpeg')


# In[51]:


objects = final_df.select_dtypes('object').reset_index()
floats = final_df.select_dtypes('float').reset_index()


# In[57]:


to_save = pd.merge(objects, floats, on='ID').set_index('ID')


# In[58]:


to_save.to_csv('../data/processed_df.csv', index=True)


# In[ ]:




