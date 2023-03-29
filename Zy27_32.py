# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:28:46 2023

@author: Mayk Al-Ghrawi
"""

userValues = [0] * 10
i = 0
minVal = 0
maxVal = 0
sumVals = 0

for i in range(10):
    userValues[i] = int(input())

minVal = userValues[0]  # Smallest seen so far
maxVal = userValues[0]  # Largest seen so far
sumVals = 0
for i in range(10):
    curVal = userValues[i]

    if curVal < minVal:  # Keep track of min
        minVal = curVal

    if curVal > maxVal:  # Keep track of max
        maxVal = curVal

    sumVals += curVal  # Keep track of sum for computing average later

print(minVal, maxVal, sumVals / 10.0)
