# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:34:05 2023

@author: Mayk Al-Ghrawi
"""

userText = input("Enter some text: ")
wordCount = 0
inWord = False

for char in userText:
    if char == ' ':
        inWord = False
    elif not inWord:
        wordCount += 1
        inWord = True
    else:
        pass

print(wordCount)
