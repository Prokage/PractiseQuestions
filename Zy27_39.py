# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:37:10 2023

@author: Mayk Al-Ghrawi
"""

def ActivityCalories(activityDone, minutesSpent):
    caloriesPerMinute = 0.0

    if activityDone == "sit":
        caloriesPerMinute = 1.4
    elif activityDone == "walk":
        caloriesPerMinute = 5.4
    elif activityDone == "run":
        caloriesPerMinute = 13.0
    elif activityDone == "bike":
        caloriesPerMinute = 6.8
    elif activityDone == "swim":
        caloriesPerMinute = 8.7

    return caloriesPerMinute * minutesSpent

if __name__ == "__main__":
    userActivity = input()
    userMinutes = int(input())

    print(ActivityCalories(userActivity, userMinutes))
