# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 08:51:27 2021

@author: Administrator
"""

import pandas as pd
import numpy as np

bank_data = pd.read_csv("BankChurners.csv")

#Eliminate the first column
bank_data = bank_data.drop(columns = ['CLIENTNUM'])

#Transfer card category to integers, because there is a hierarical relationship
card_cate_map = {'Blue': 0, 'Silver': 1, 'Gold':2, 'Platinum': 3}
for i in range(len(bank_data['Card_Category'])):
    for j in card_cate_map:
        if bank_data['Card_Category'][i] == j:
            bank_data.at[i, 'Card_Category'] = card_cate_map[j]       

#Transfer education category to integers, because there is a hierarical relationship
education_cate_map = {'Unknown':-1,'Uneducated':0,'High School':1,'College':2,'Graduate':3,'Post-Graduate':4, 'Doctorate':5 }
for i in range(len(bank_data['Education_Level'])):
    for j in education_cate_map:
        if bank_data['Education_Level'][i] == j:
            bank_data.at[i, 'Education_Level'] = education_cate_map[j]   
            

#Method 2
one_hot_data = pd.get_dummies(bank_data, columns = ['Card_Category', 'Education_Level','Gender'])