# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:03:49 2023

@author: Mayk Al-Ghrawi
"""

user_chord = input()

if user_chord == "G":
    print("e|-3-\nB|-0-\nG|-0-\nD|-0-\nA|-2-\nE|-3-")
    """
    e|-3-
    B|-0-
    G|-0-
    D|-0-
    A|-2-
    E|-3-
    """
elif user_chord == "C":
    print("e|-0-\nB|-1-\nG|-0-\nD|-2-\nA|-3-\nE|---")
    """
    e|-0-
    B|-1-
    G|-0-
    D|-2-
    A|-3-
    E|---
    """
elif user_chord == "D":
    print("e|-2-\nB|-3-\nG|-2-\nD|-0-\nA|---\nE|---")
    """
    e|-2-
    B|-3-
    G|-2-
    D|-0-
    A|---
    E|---
    """
else:
    print(user_chord, "is not a supported chord.")
    
