# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:47:05 2023

@author: Mayk Al-Ghrawi
"""

phone_number = input()
formatted_number = "({}) {}-{}".format(phone_number[:3], phone_number[3:6], phone_number[6:])
print(formatted_number)
