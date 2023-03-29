# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:44:14 2023

@author: Mayk Al-Ghrawi
"""

def FindNextCharInString(s, startIndex, c):
    for i in range(startIndex, len(s)):
        if s[i] == c:
            return i
    return -1


# Main function
inputString = input()
startIndex = int(input())
searchChar = input()

print(FindNextCharInString(inputString, startIndex, searchChar))
