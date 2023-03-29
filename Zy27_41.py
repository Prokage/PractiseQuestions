# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:37:37 2023

@author: Mayk Al-Ghrawi
"""

def GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear):
    currAge = currYear - birthYear
    # Determine if need to reduce by 1 if birthday not yet reached
    if currMonth < birthMonth:  # Birth month not yet reached, reduce by 1
        currAge -= 1
    elif currMonth == birthMonth and currDay < birthDay:  # In birth month, but birthday not yet reached
        currAge -= 1
    
    return currAge

if __name__ == "__main__":
    birthMonth, birthDay, birthYear = map(int, input().split())
    currMonth, currDay, currYear = map(int, input().split())

    print(GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear))
