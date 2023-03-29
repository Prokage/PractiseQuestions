# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:38:10 2023

@author: Mayk Al-Ghrawi
"""

def digit_to_word(digit_in):
    if digit_in == 0:
        return ""
    elif digit_in == 1:
        return "one"
    elif digit_in == 2:
        return "two"
    elif digit_in == 3:
        return "three"
    elif digit_in == 4:
        return "four"
    elif digit_in == 5:
        return "five"
    elif digit_in == 6:
        return "six"
    elif digit_in == 7:
        return "seven"
    elif digit_in == 8:
        return "eight"
    elif digit_in == 9:
        return "nine"
    else:
        return "error"

def tens_digit_to_word(digit_in):
    if digit_in == 0:
        return "error"
    elif digit_in == 1:
        return "error"
    elif digit_in == 2:
        return "twenty"
    elif digit_in == 3:
        return "thirty"
    elif digit_in == 4:
        return "forty"
    elif digit_in == 5:
        return "fifty"
    elif digit_in == 6:
        return "sixty"
    elif digit_in == 7:
        return "seventy"
    elif digit_in == 8:
        return "eighty"
    elif digit_in == 9:
        return "ninety"
    else:
        return "error"

def two_digit_num_to_words(num_in):
    ones_digit = num_in % 10
    tens_digit = num_in // 10
    
    return tens_digit_to_word(tens_digit) + " " + digit_to_word(ones_digit)

user_num = int(input())

print(two_digit_num_to_words(user_num))
