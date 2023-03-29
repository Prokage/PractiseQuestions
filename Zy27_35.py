# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:29:23 2023

@author: Mayk Al-Ghrawi
"""

numItems = int(input())
listItems = []

# Get items
for i in range(numItems):
    currItem = input()
    listItems.append(currItem)

# Find longest sequence of complete passes
longestSeqLength = 0
currSeqLength = 0
for i in range(numItems):
    if listItems[i] == "I":  # Either reached end of sequence, or no sequence yet
        currSeqLength = 0  # Reset for the next sequence
    else:  # Either starting a sequence, or in the middle of a sequence
        currSeqLength += 1
        if currSeqLength > longestSeqLength:  # If current sequence is longest seen so far, update longest
            longestSeqLength = currSeqLength

print(longestSeqLength)
