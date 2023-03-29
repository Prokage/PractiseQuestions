# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:43:50 2023

@author: Mayk Al-Ghrawi
"""

def DigitsToNum(digitsList):
    currWeight = 1
    totalNum = 0
    
    for i in range(len(digitsList)):
        totalNum += digitsList[i] * currWeight
        currWeight *= 10
    return totalNum


# Main function
digitsList = []
while True:
    try:
        userDigit = int(input())
        digitsList.append(userDigit)
    except:
        break

resultNum = DigitsToNum(digitsList)

print(resultNum)
