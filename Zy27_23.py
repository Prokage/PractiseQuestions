# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:27:50 2023

@author: Mayk Al-Ghrawi
"""

aisMinimum = float(input())
for rowGPA in [x / 10.0 + 3.0 for x in range(11)]:
    rowTestScore = 1600.0 * (aisMinimum / 100.0) - 1600.0 * 2.5 * (rowGPA / 4.0)
    print(rowGPA, rowTestScore)
