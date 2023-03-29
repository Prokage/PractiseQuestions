# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:29:09 2023

@author: Mayk Al-Ghrawi
"""

chptList = [False] * 16  # Valid chapters are 1-15. 1 means include, 0 exclude. Element 0 unused.
includeChpt = False
atLeastOne = False

# Get the chapter selections
for i in range(1, 16):
    includeChpt = bool(int(input()))
    if includeChpt:
        chptList[i] = True
        atLeastOne = True
    else:
        chptList[i] = False

# Output the chapter selections, using ranges like 2-4 for ranges of 3-or-more
for i in range(1, 16):
    if chptList[i]:  # Output this number
        print(i, end="")
        if (i <= 13) and (chptList[i + 1] and chptList[i + 2]):  # Possible 3-or-more range
            # Find end of range
            j = i + 2  # Last 1 seen so far in the range
            while (j <= 14) and (chptList[j + 1]):  # Range continues...
                j += 1  # ...so extend the range
            print("-", j, end=" ")
            i = j  # Set i to end of range, so next for loop iteration will start at the next number
        else:
            print(" ", end="")  # No 3-or-more range, so just output a space after the number

if not atLeastOne:  # No chapters were selected
    print("None", end=" ")
print()
