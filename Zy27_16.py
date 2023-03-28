# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:27:08 2023

@author: Mayk Al-Ghrawi
"""

user_text = input()
cleaned_text = ''

# Find first non-space character
i = 0
while i < len(user_text) and user_text[i] == ' ':
    i += 1
    
if i == len(user_text):
    print('')
    exit()

# Find last non-space character
j = len(user_text) - 1
while j >= 0 and user_text[j] == ' ':
    j -= 1

# Copy just characters from i to j to new string
for n in range(i, j + 1):
    cleaned_text += user_text[n]
         
print(cleaned_text)
