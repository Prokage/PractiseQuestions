# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:28:29 2023

@author: Mayk Al-Ghrawi
"""

throwValues = [0] * 21
frameScores = [0] * 10
t = 0  # Throw index
f = 0  # Frame index
frameScore = 0

# Read in the 21 possible throw values for the 10 frames
for t in range(21):
    throwValues[t] = int(input())

# Compute score of each of first 9 frames
t = 0
for f in range(9):
    frameScore = 0
    frameScore = throwValues[t]  # Add first throw of this frame
    if frameScore == 10:  # Strike
        frameScore += throwValues[t + 1] + throwValues[t + 2]  # Add next two throws
    else:  # Not a strike
        t += 1
        frameScore += throwValues[t]  # Add second throw of this frame
        if frameScore == 10:  # Spare
            frameScore += throwValues[t + 1]  # Add next throw
    t += 1

    if f > 0:  # Not first frame, so add previous frame's score
        frameScore += frameScores[f - 1]  # Add previous frame's score

    frameScores[f] = frameScore

# 10th frame
frameScores[f] = frameScores[f - 1] + throwValues[t] + throwValues[t + 1] + throwValues[t + 2]
# Note: If only two throws in 10th frame, the t+2 value will be 0, so OK to add. Keeps code simpler.

# Note that above, frame 1 is at element 0, frame 2 at element 1, ..., and frame 10 at element 9.

for f in range(10):
    print(frameScores[f], end=" ")
print()
