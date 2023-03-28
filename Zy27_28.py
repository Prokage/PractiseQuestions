# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:28:46 2023

@author: Mayk Al-Ghrawi
"""

yearlyValues = []
for i in range(12):
    yearlyValues.append(int(input()))

for i in range(0, 12, 4):
    print(yearlyValues[i], yearlyValues[i+1], yearlyValues[i+2], yearlyValues[i+3])

