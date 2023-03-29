# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:44:26 2023

@author: Mayk Al-Ghrawi
"""

def FindNextSubstr(s, startIndex, substr):
    for i in range(startIndex, len(s)-len(substr)+1):
        if s[i:i+len(substr)] == substr:
            return i
    return -1


# Main function
inputString = input()
startIndex = int(input())
searchStr = input()

print(FindNextSubstr(inputString, startIndex, searchStr))
