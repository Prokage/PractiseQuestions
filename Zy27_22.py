# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:27:36 2023

@author: Mayk Al-Ghrawi
"""

userText = input()
wordCount = 0
inWord = False

for char in userText:
    if char == ' ':  # Space, so we're not in a word
        inWord = False
    elif not inWord:  # First non-space char after a space (or at start of text)
        wordCount += 1  # So we found a new word, thus increment wordCount
        inWord = True
    else:  # Non-space char in the middle of word
        # Just skip this non-space char
        pass

print(wordCount)
