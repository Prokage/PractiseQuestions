# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:13:23 2023

@author: Mayk Al-Ghrawi
"""

plateNumber = input()
c1 = plateNumber[0]
c2 = plateNumber[1]
c3 = plateNumber[2]
i1 = plateNumber[3]
i2 = plateNumber[4]
i3 = plateNumber[5]
carryNeeded = False

# Check each place starting from the right. If less than max, just increment it.
# If at max, set to start val, set carry true

# Place 6
if i3 < '9':
    i3 = chr(ord(i3) + 1)
    carryNeeded = False
else:
    i3 = '0'
    carryNeeded = True

# Place 5
if carryNeeded:
    if i2 < '9':
        i2 = chr(ord(i2) + 1)
        carryNeeded = False
    else:
        i2 = '0'
        carryNeeded = True

# Place 4
if carryNeeded:
    if i1 < '9':
        i1 = chr(ord(i1) + 1)
        carryNeeded = False
    else:
        i1 = '0'
        carryNeeded = True

# Place 3
if carryNeeded:
    if c3 < 'Z':
        c3 = chr(ord(c3) + 1)
        carryNeeded = False
    else:
        c3 = 'A'
        carryNeeded = True

# Place 2
if carryNeeded:
    if c2 < 'Z':
        c2 = chr(ord(c2) + 1)
        carryNeeded = False
    else:
        c2 = 'A'
        carryNeeded = True

# Place 1
if carryNeeded:
    if c1 < 'Z':
        c1 = chr(ord(c1) + 1)
        carryNeeded = False
    else:
        c1 = 'A'
        carryNeeded = True

print(c1 + c2 + c3 + i1 + i2 + i3)
