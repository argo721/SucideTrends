# Project: Suicide Data set
# Author: Arghya Biswas

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns

# to check if things were successfully imported
print("Hello")

# importing data set from csv file
completeDataSet = pd.read_csv("C:\Hult\data analytics resources\Suicide.csv")

# Uncomment print statement to check if data set has been loaded
# print(completeDataSet.head())


# DataFrame loaded from the pandas
df_DataSet = pd.DataFrame(completeDataSet)

corr = completeDataSet.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)

ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

plt.title("Correlation between numerical values")
plt.show()


#Selecting unique countries list

df_countries = df_DataSet['country'].unique().tolist()
print("No. of available countries:"+ str(len(df_countries)))
print("\n list of countries:")
print(df_countries)
completeDataSet.set_index(keys=['country'], drop=False, inplace=True)

print(completeDataSet.loc[completeDataSet.country=='Albania'])

#creating dictionary. Spliting data set country wise
dict_countryWise={"Albania":""}


for i in range (0,len(df_countries)):
    #print(df_countries[i])
    dict_countryWise[df_countries[i]] =completeDataSet.loc[completeDataSet.country == df_countries[i]]

print(len(dict_countryWise))
