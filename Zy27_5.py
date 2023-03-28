# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:03:01 2023

@author: Mayk Al-Ghrawi
"""

user_caption = input()

last_index = len(user_caption) - 1
last_char = user_caption[last_index]

if last_char in ['!', '?']:
    # Caption OK; do nothing
    pass
elif last_char == ',':
    user_caption = user_caption[:last_index] + '.'  # Replace ending , by .
elif last_char != '.':
    user_caption += '.'  # Not ! ? , . so append .
elif last_char == '.' and last_index > 0 and user_caption[last_index - 1] == '.':
    if last_index > 1 and user_caption[last_index - 2] == '.':  # Three periods
        # Caption OK (ends with elipses ...); do nothing
        pass
    else:  # Ends with two periods; remove one
        user_caption = user_caption[:-1]

print(user_caption)
