# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:28:32 2023

@author: Mayk Al-Ghrawi
"""

numItems = int(input())
listItems = []
for i in range(numItems):
    currItem = int(input())
    listItems.append(currItem)

maxItem = listItems[0]
for i in range(numItems):
    if listItems[i] > maxItem:
        maxItem = listItems[i]

print(maxItem)
