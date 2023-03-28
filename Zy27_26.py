# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:28:22 2023

@author: Mayk Al-Ghrawi
"""

listSize = int(input())

isSorted = True
prevNum = int(input())
for i in range(1, listSize):
    currNum = int(input())
    if currNum <= prevNum:
        isSorted = False
    prevNum = currNum

if isSorted:
    print("Sorted")
else:
    print("Unsorted")
