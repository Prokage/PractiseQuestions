# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:37:28 2023

@author: Mayk Al-Ghrawi
"""

def absVal(a):
    if a < 0:
        return -a
    else:
        return a

# All x, y coordinates are in miles from the origin 0, 0.
def PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y):
    # Compute distances
    dist1 = absVal(userX - d1X) + absVal(userY - d1Y)
    dist2 = absVal(userX - d2X) + absVal(userY - d2Y)
    dist3 = absVal(userX - d3X) + absVal(userY - d3Y)

    # Determine minimum distance
    minDist = dist1
    if dist2 < minDist:
        minDist = dist2
    if dist3 < minDist:
        minDist = dist3

    # Calculate and return time (2 min per mile)
    return 2 * minDist

if __name__ == "__main__":
    userX, userY = map(int, input().split())
    d1X, d1Y = map(int, input().split())
    d2X, d2Y = map(int, input().split())
    d3X, d3Y = map(int, input().split())

    print(PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y))
