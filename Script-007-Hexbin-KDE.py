#!/usr/bin/env python
# coding: utf-8

# In[53]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfB = pd.read_csv("Tab-Bathy.csv")
df = dfB.melt(id_vars=['observ'], 
              value_vars=['profile1', 'profile2', 'profile3', 'profile4', 
                          'profile5', 'profile6', 'profile7', 'profile8',
                         'profile9', 'profile10', 'profile11', 'profile12',
                         'profile13', 'profile14', 'profile15', 'profile16', 
                          'profile17', 'profile18', 'profile19', 'profile20',
                         'profile21', 'profile22', 'profile23', 'profile24','profile25'],
              var_name='Profiles', value_name='Depths')
#print(df.head)
sb.set(style="white")
sb.set_color_codes()
#sb.jointplot(x='Profiles',y='Depths',data=df,kind='kde')
#sb.pairplot(df,diag_kind="hex",kind="scatter",palette="husl")
sb.jointplot(x='observ',y='Depths',data=df,kind='kde', dropna=True, color="m")
sb.jointplot("observ", "Depths", data=df, kind="hex", dropna=True)
#plt.title('Mariana Trench', fontsize=10, fontfamily='serif')
plt.subplots_adjust(bottom=0.15,top=0.85, right=0.90, left=0.10)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




