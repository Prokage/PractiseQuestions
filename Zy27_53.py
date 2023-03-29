# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:46:19 2023

@author: Mayk Al-Ghrawi
"""

def RotateRight3(p1, p2, p3):
    tmp = p3
    p3 = p2
    p2 = p1
    p1 = tmp
    return p1, p2, p3

n1 = int(input())
n2 = int(input())
n3 = int(input())

n1, n2, n3 = RotateRight3(n1, n2, n3)

print(n1, n2, n3)
