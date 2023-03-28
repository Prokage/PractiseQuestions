# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:25:51 2023

@author: Mayk Al-Ghrawi
"""

user_int = int(input())
divisor = user_int

while divisor != 0:
    print(divisor % 10)  # Outputs rightmost digit
    divisor = divisor // 10  # Shifts the integer right by one digit

