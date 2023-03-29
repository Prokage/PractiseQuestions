# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:46:30 2023

@author: Mayk Al-Ghrawi
"""

year = int(input())
isLeapYear = False

if year % 4 == 0:
    isLeapYear = True
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False

if isLeapYear:
    print("true")
else:
    print("false")
