# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:27:39 2023

@author: Mayk Al-Ghrawi
"""

user_text = input()
length_ok = False
has_letter = False
has_number = False
has_special = False

if len(user_text) >= 8:
    length_ok = True

for c in user_text:
    if c.isalpha():  # At least one letter found
        has_letter = True
    elif c.isdigit():  # At least one number found
        has_number = True
    elif c in "!#%":
        has_special = True

if length_ok and has_letter and has_number and has_special:
    print("OK")
else:
    if not length_ok:
        print("Too short")
    if not has_letter:
        print("Missing letter")
    if not has_number:
        print("Missing number")
    if not has_special:
        print("Missing special")
