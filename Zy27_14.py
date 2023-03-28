# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:18:18 2023

@author: Mayk Al-Ghrawi
"""

num_ints = int(input())
while num_ints > 0:
    ints_sum = 0
    for i in range(num_ints):
        user_int = int(input())
        ints_sum += user_int
    print(ints_sum)
    num_ints = int(input())
