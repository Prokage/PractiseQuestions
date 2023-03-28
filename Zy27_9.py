# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:12:23 2023

@author: Mayk Al-Ghrawi
"""

firstName1, lastName1 = input().split()
firstName2, lastName2 = input().split()
firstName3, lastName3 = input().split()

if firstName1 == "none":
    print("TBD")
elif firstName2 == "none":
    print(firstName1[0] + ". " + lastName1)
elif firstName3 == "none":
    print(lastName1 + " / " + lastName2)
else:
    print(lastName1 + " / " + lastName2 + " / ...")
