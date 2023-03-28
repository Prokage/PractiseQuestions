# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:07:58 2023

@author: Mayk Al-Ghrawi
"""

runway_num = int(input())

runway_deg = runway_num * 10

# Determine closest direction. Ranges are heading +/- 22.5.
if (0 - 22.5) <= runway_deg < (0 + 22.5):
    runway_direction = "north"
elif (45 - 22.5) <= runway_deg < (45 + 22.5):
    runway_direction = "northeast"
elif (90 - 22.5) <= runway_deg < (90 + 22.5):
    runway_direction = "east"
elif (135 - 22.5) <= runway_deg < (135 + 22.5):
    runway_direction = "southeast"
elif (180 - 22.5) <= runway_deg < (180 + 22.5):
    runway_direction = "south"
elif (225 - 22.5) <= runway_deg < (225 + 22.5):
    runway_direction = "southwest"
elif (270 - 22.5) <= runway_deg < (270 + 22.5):
    runway_direction = "west"
elif (315 - 22.5) <= runway_deg < (315 + 22.5):
    runway_direction = "northwest"

print(f"{runway_deg} degrees ({runway_direction})")
