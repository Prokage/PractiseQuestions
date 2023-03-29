# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:40:16 2023

@author: Mayk Al-Ghrawi
"""

def FirstRectangleSmaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr):
    r1Area = abs(r1xul - r1xbr) * abs(r1yul - r1ybr) # Area is width * height
    r2Area = abs(r2xul - r2xbr) * abs(r2yul - r2ybr)
    return r1Area < r2Area

# Main function
r1xul, r1yul, r1xbr, r1ybr = map(int, input().split()) # x upper-left, y upper-left, x bottom-right, y bottom-right
r2xul, r2yul, r2xbr, r2ybr = map(int, input().split())

print(FirstRectangleSmaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr))
