# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:29:54 2023

@author: Mayk Al-Ghrawi
"""

num_ints = int(input())
for i in range(num_ints):
    if i > 0:
        print(", ", end="")
    curr_int = int(input())
    print(curr_int, end="")
print(".")
