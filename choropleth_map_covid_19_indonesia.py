# -*- coding: utf-8 -*-
"""CHOROPLETH MAP COVID-19 INDONESIA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uy12k0JIQ4yUJiDmfph0j1tWY59cNd1I
"""

!pip install descartes
!pip install geopandas
!pip install matplotlib
!pip install numpy
!pip install pandas

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

geometryFile = './IDN_adm1.shp'
map_df = gpd.read_file(geometryFile)
display(map_df)
# plt.rcParams['figure.figsize'] = [50, 70]
# map_df.plot()

covid_df = pd.read_csv('./covid_19_indonesia_time_series_all.csv')
display(covid_df)

df_join = map_df.merge(covid_df, how='inner', left_on='NAME_1', right_on='Province')
df_join = df_join[['Province', 'geometry', 'Total Cases']]
df_join.head()

variable = 'Total Cases'
vmin, vmax = 0, 1412511
fig, ax = plt.subplots(1, figsize=(30,10))
ax.axis('off')
ax.set_title('Visualisasi Total Kasus Covid-19 Berdasarkan Provinsi', fontdict={'fontsize': '25', 'fontweight': '3'})
ax.annotate('By: Mhd. Zulfikar Pinem', xy=(0.6, .05), xycoords='figure fraction', fontsize=12, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Reds', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm.set_array([])
fig.colorbar(sm)
df_join.plot(column=variable, cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8')
df_join['coords'] = df_join['geometry'].apply(lambda x: x.representative_point().coords[:])
df_join['coords'] = [coords[0] for coords in df_join['coords']]
for idx, row in df_join.iterrows():
  plt.annotate(s=row['Province'], xy=row['coords'], horizontalalignment='center')

fig.savefig('map.png', dpi=300)

