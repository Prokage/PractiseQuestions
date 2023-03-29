# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:36:55 2023

@author: Mayk Al-Ghrawi
"""

def Ascend3(a, b, c):
    lowVal, midVal, highVal = 0, 0, 0

    # 6 possible orderings of a, b, c exist. abc, acb, bac, bca, cab, cba.
    # Determine current ordering, then update to be ascending
    if (a <= b) and (b <= c):
        lowVal, midVal, highVal = a, b, c
    elif (a <= c) and (c <= b):
        lowVal, midVal, highVal = a, c, b
    elif (b <= a) and (a <= c):
        lowVal, midVal, highVal = b, a, c
    elif (b <= c) and (c <= a):
        lowVal, midVal, highVal = b, c, a
    elif (c <= a) and (a <= b):
        lowVal, midVal, highVal = c, a, b
    elif (c <= b) and (b <= a):
        lowVal, midVal, highVal = c, b, a

    return lowVal, midVal, highVal

if __name__ == "__main__":
    x, y, z = map(int, input().split())
    x, y, z = Ascend3(x, y, z)
    print(x, y, z)
