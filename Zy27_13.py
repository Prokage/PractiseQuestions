# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:16:44 2023

@author: Mayk Al-Ghrawi
"""

valid_sum = 0
valid_num = 0
invalid_num = 0
user_int = int(input())
average_num = 0.0

while user_int != 0:
    if 2 <= user_int <= 12:  # Valid
        valid_sum += user_int
        valid_num += 1
    elif user_int != 0:  # Invalid
        invalid_num += 1
    user_int = int(input())

if valid_num > 0:  # Avoid dividing by 0
    average_num = valid_sum / valid_num

print(f"Average: {average_num}")
print(f"Valid: {valid_num}")
print(f"Invalid: {invalid_num}")
