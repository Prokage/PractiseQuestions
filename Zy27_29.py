# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:28:56 2023

@author: Mayk Al-Ghrawi
"""

listInts = []
for i in range(6):
    listInts.append(int(input()))

listNegInts = []
for num in listInts:
    if num < 0:
        listNegInts.append(num)

print(len(listNegInts))
for num in listNegInts:
    print(num)
