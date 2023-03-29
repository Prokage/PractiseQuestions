# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:29:40 2023

@author: Mayk Al-Ghrawi
"""

listNums = []

while True:
    try:
        currNum = int(input())
        listNums.append(currNum)
    except:
        break


listSize = len(listNums)
for i in range(listSize // 2):
# Swap item from first half with item from second half
    tmp = listNums[i]
    listNums[i] = listNums[listSize - i - 1]
    listNums[listSize - i - 1] = tmp

for i in range(listSize):
    print(listNums[i], end=" ")
print()