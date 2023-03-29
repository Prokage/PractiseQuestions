# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:36:47 2023

@author: Mayk Al-Ghrawi
"""

def MaxFive(a, b, c, d, e):
    maxFound = a  # Initializing to a is enough
    if b > maxFound:
        maxFound = b
    if c > maxFound:
        maxFound = c
    if d > maxFound:
        maxFound = d
    if e > maxFound:
        maxFound = e
    return maxFound

if __name__ == "__main__":
    v, w, x, y, z = map(int, input().split())
    maxVal = MaxFive(v, w, x, y, z)
    print(maxVal)
