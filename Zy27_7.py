# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:04:52 2023

@author: Mayk Al-Ghrawi
"""

hour_ampm, min_ampm, am_pm = input().split()

hour24 = int(hour_ampm)
if am_pm == "am" and hour24 == 12:  # Special case for first hour
    hour24 = 0
elif am_pm == "pm" and hour24 != 12:  # Add 12 for 1 pm and higher (not for 12 pm)
    hour24 += 12  # Ex: 2 pm becomes 14

hour24_str = str(hour24).zfill(2)  # Prepend 0 if hour < 10

min_ampm_str = min_ampm.zfill(2)  # Prepend 0 if min < 10

print(hour24_str + ":" + min_ampm_str)
