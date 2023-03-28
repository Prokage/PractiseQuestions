# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:16:35 2023

@author: Mayk Al-Ghrawi
"""

rocket_height = 0
initial_velocity = 0
time_since_launch = 0

initial_velocity = int(input())

while rocket_height >= 0:
    print(time_since_launch, rocket_height)
    time_since_launch = time_since_launch + 1
    rocket_height = (initial_velocity * time_since_launch) - (5 * time_since_launch * time_since_launch)
