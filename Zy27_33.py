# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:28:57 2023

@author: Mayk Al-Ghrawi
"""

userValues = [0] * 10
i = 0
curVal = 0  # Improves code readability below
valCounts = [0] * 100
maxCount = 0
maxCountIndex = 0

for i in range(10):
    userValues[i] = int(input())

# valCounts list was auto-initialized to all 0's. No need to explicitly initialize here
for i in range(10):
    curVal = userValues[i]
    if (curVal < 0) or (curVal > 99):
        print("Invalid input: " + str(curVal) + " is not in 0-99")
        exit()

    valCounts[curVal] += 1

maxCount = valCounts[0]  # Max count seen so far
maxCountIndex = 0  # Index of max count seen so far
for i in range(100):  # Note to 100, not 10
    if valCounts[i] > maxCount:
        maxCount = valCounts[i]
        maxCountIndex = i

print(maxCountIndex, maxCount)
