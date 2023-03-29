# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:52:21 2023

@author: Mayk Al-Ghrawi
"""

# Type your code here.
total_inches = int(input())

feet = total_inches // 12
inches = total_inches % 12

print(str(feet) + "'" + str(inches) + "\"")
