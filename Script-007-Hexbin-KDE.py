#!/usr/bin/env python
# coding: utf-8
#
import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
#
profiles_nrs = list(map(lambda x: x, range(25)))
profiles_list = []
for i in profiles_nrs:
    profiles_list.append('profile{}'.format(i + 1))
#
dfB = pd.read_csv("Tab-Bathy.csv")
df = dfB.melt(id_vars = ['observ'],
              value_vars = profiles_list,
              var_name = 'Profiles', value_name = 'Depths')
#print(df.head)
sb.set(style = "white")
sb.set_color_codes()
#
sb.jointplot(x = 'observ',y = 'Depths',data = df, kind='kde', dropna = True, color = "m")
sb.jointplot("observ", "Depths", data = df, kind = "hex", dropna = True)
plt.subplots_adjust(bottom = 0.15,top = 0.85, right = 0.90, left = 0.10)
plt.show()
