# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:51:22 2023

@author: Mayk Al-Ghrawi
"""

# Type your code here.
current_grade = float(input())

current_points = current_grade * 0.6
points_needed = 90 - current_points
grade_on_final = points_needed / 40

print("{:.1f}%".format(grade_on_final * 100))
