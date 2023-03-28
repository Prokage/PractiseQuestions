# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:59:12 2023

@author: Mayk Al-Ghrawi
"""

passenger_age = int(input())
carry_ons = int(input())
checked_bags = int(input())

air_fare = 0

if passenger_age >= 60:
    air_fare = 290  # Senior
elif passenger_age <= 2:
    air_fare = 0  # Lap child
else:  # Regular: 2 < age < 60
    air_fare = 300

if carry_ons > 0:
    air_fare += 10

if checked_bags == 2:
    air_fare += 25
elif checked_bags >= 3:
    air_fare += 25 + (checked_bags - 2) * 50  # 2nd bag is $25. Each bag beyond 2nd is $50 
# Note: 0 or 1 bags is $0, so no adjustment to airfare

print(air_fare)
