# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:50:50 2023

@author: Mayk Al-Ghrawi
"""

import math

# Input format: (x1,y1) (x2,y2)
input_str = input()

# Extracting values from the input string
x1, y1, x2, y2 = map(float, input_str.replace('(', '').replace(')', '').replace(',', '').split())

dist_points = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(dist_points)
