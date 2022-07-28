# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 16:46:49 2022

@author: mabou
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("equil-dual-resistance-A-D-run4.csv")
dataRHT = pd.read_csv("equil-humidity-run4.csv")
data.columns = ("t","VA","IA","VB","IB")

plt.subplots()
sns.scatterplot(data=data,x="t",y="IA")
sns.scatterplot(data=data,x="t",y="IB")

data = pd.read_csv("equil-dual-resistance-A-D-run2.csv")
data.columns = ("t","VA","IA","VB","IB")

plt.subplots()
sns.scatterplot(data=data,x="t",y="IA")
sns.scatterplot(data=data,x="t",y="IB")

#plt.subplots()
#sns.scatterplot(data=dataRHT,x="t ",y="HB")
#plt.subplots()
#sns.scatterplot(data=dataRHT,x="t ",y="TB")

plt.show()