# python 3

import seaborn as sns
import os, re
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/processed_df.csv')

a=pd.crosstab(index=df['12ECHEC = PSVr > 2,4'],columns=df['stenting_method']).reindex(['PERMEABLE','ECHEC'])
a.plot.bar(color=('blue','orange'))
plt.grid('True')
plt.ylabel('Counts')
plt.xlabel('Permeability at 12 months')

def myBoxs(x, y, witch='p', p=0.1):
    plt.figure(figsize=(8,6))
    sns.boxplot(x = x,
                y = y,
                hue=x,
                palette= {'PERMEABLE':'green', 'ECHEC':'red'},
                notch=True,
                data = df,
                medianprops={"color": "coral"},
                dodge=False, order=['PERMEABLE','ECHEC'])
    sns.stripplot(x = x,y = y,data = df, color='black', size=5,dodge=False, order=['PERMEABLE','ECHEC'])
    plt.grid(True)
    plt.annotate(f'{witch}-value : {p}', (0.5,max(df[y])/2), fontsize=15)


dico = {'fig1:1ECHEC = PSVr > 2,4':['Densité UH max2', 'q',0.059],
       'fig2:1ECHEC = PSVr > 2,4':['Densité UH max3','q',0.036],
       'fig3:1ECHEC = PSVr > 2,4':['Densité UH moy3','q',0.059],
       'fig4:2ECHEC = PSVr > 2,4':['Densité UH max3','p',0.055],
       'fig5:2ECHEC = PSVr > 2,4':['Densité UH moy3','p',0.021],
       'fig6:12ECHEC = PSVr > 2,4':['Volume zone 3', 'p',0.058],
       'fig7:12ECHEC = PSVr > 2,4':['Densité UH min3','p',0.041],
       'fig8:12ECHEC = PSVr > 2,4':['Densité UH max3','p',0.072],
       'fig9:12ECHEC = PSVr > 2,4':['Densité UH moy3', 'p',0.037]}

for k, v in dico.items():
    x=k.split(':')[1].strip()
    y=v[0]
    witch = v[1]
    p = v[2]
    myBoxs(x, y, witch, p)
