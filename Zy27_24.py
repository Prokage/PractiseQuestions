# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:27:59 2023

@author: Mayk Al-Ghrawi
"""

import math

tvDiagonal = int(input())
for tvWidth in range(1, tvDiagonal):
    tvHeight = math.sqrt(tvDiagonal ** 2 - tvWidth ** 2)
    if tvWidth > tvHeight:
        print(tvWidth, tvHeight)
