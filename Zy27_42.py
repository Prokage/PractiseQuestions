# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:37:56 2023

@author: Mayk Al-Ghrawi
"""

def SimulateLine(customerArrivals):
    lineLength = 0
    for i in range(len(customerArrivals)):
        if lineLength > 0:
            lineLength -= 1  # Each minute, the clerk finishes serving 1 customer
        lineLength += customerArrivals[i]  # This many new customers arrived into line
        print(lineLength, end=" ")
    print()

if __name__ == "__main__":
    customerArrivals = list(map(int, input().split()))

    SimulateLine(customerArrivals)
