# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:14:05 2023

@author: Mayk Al-Ghrawi
"""

n = int(input("Enter an integer:\n"))
print("Sequence: ", end="")
if n < 0:
   n = -n 
for i in range(-n, n+1):
   print(i, end=" ")
print()
