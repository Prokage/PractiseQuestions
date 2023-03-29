# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:38:32 2023

@author: Mayk Al-Ghrawi
"""

def cents_to_dollars_cents(user_cents):
    num_dollars = user_cents // 100  # Ex: 752 // 100 is 7 (integer division ignores fraction)
    num_cents = user_cents % 100  # Ex: 752 % 100 is 52, because 752/100 is 7 remainder 52.
    return num_dollars, num_cents


user_cents = int(input())  # Ex: 752
num_dollars, num_cents = cents_to_dollars_cents(user_cents)

print(num_dollars, "dollars", num_cents, "cents")
