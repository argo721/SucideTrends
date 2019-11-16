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
);

plt.title("Correlation between numerical values")
plt.show()
