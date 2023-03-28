# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:29:45 2023

@author: Mayk Al-Ghrawi
"""

binaryNum = []
for i in range(8):
    bit = int(input("Enter bit {}: ".format(7-i)))
    binaryNum.append(bit)

decimalSum = 0
digitWeight = 1
for bit in reversed(binaryNum):
    decimalSum += bit * digitWeight
    digitWeight *= 2

print(decimalSum)
