# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 13:59:50 2018

@author: codept
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pit
from matplotlib import style
style.use ('fivethirtyeight') 


data = {'A':[1,2,np.nan],
        'B':[5,np.nan,2],
        'C':[1,2,3]}
data

df = pd.DataFrame(data)
df
df.dropna(axis=0)
df

df.fillna(df.mad())                     #min hai  max hain n mad hai#
pit.plot(df['Open'])
pit.show()


df = pd.read_csv("Desktop/pandas/indiacencesdata.csv")
df.set_index('Year',inplace=True)
pit.plot(df['Population'])
pit.show()

df = pd.read_csv("Desktop/pandas/Salaries.csv")
df.set_index('',inplace=True)
pit.plot(df['Agency'])
pit.show()

df[df['BasePay'] == df['BasePay'].max()][['EmployeeName','BasePay']] #min()


df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()][['EmployeeName','TotalPayBenefits']] #min()

ecom = pd.read_csv("Desktop/pandas/Ecommerce Purchases.csv")
ecom.info()

ecom['AM or PM'].value_counts()

ecom['Job'].value_counts().head(6)


ecom[ecom['Lot'] == '90WT']['Purchase Price']

ecom[ecom['Credit Card']==4926535242672853]['Email']













