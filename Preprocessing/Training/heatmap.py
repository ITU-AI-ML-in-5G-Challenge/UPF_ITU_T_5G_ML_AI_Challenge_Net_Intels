# -*- coding: utf-8 -*-
"""HeatMap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C72TJw3Ka1vZMwS2tfLrVBahRbKu9pjX
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.read_csv("Combined_rssi_corrected_proper_sinr_row_fixed.csv", delimiter = ",", skiprows =0,usecols = [i for i in range(0, 7)])
labels = pd.read_csv("Combined_rssi_corrected_proper_sinr_row_fixed.csv", delimiter = ",", skiprows =1, header = None, usecols = [7])

def heat_map(df):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(20, 20))
    colormap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
    
    plt.xticks(range(len(corr.columns)), corr.columns);
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.show()

heat_map(dataset)

print(dataset.shape)
print(labels.shape)