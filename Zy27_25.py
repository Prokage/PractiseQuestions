# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:28:10 2023

@author: Mayk Al-Ghrawi
"""

listSize = int(input())

maxDiff = 0
prevNum = int(input())
for i in range(1, listSize):
    currNum = int(input())
    currDiff = abs(currNum - prevNum)
    if currDiff > maxDiff:
        maxDiff = currDiff
    prevNum = currNum

print(maxDiff)
