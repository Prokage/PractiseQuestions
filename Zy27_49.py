# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:44:02 2023

@author: Mayk Al-Ghrawi
"""

def DigitToChar(singleDigit):
    digitAsChar = '0'
    # We know 1's ASCII code is 1 more than 0's, 2's is 2 more, etc. So we initialize digitAsChar to 0's ASCII code.
    # Then we increase by the amount of the digit, so we add 0, 1, 2, etc.
    digitAsChar = chr(ord(digitAsChar) + singleDigit)
    return digitAsChar

def NumToStringWithCommas(userNum):
    currNum = userNum
    posCount = 0  # Every 3, insert a comma
    numAsString = ''
    
    while currNum > 0:
        if posCount == 3:
            numAsString = ',' + numAsString
            posCount = 1  # 1 (not 0), because we're going to add a digit
        else:
            posCount += 1
            
        currDigit = currNum % 10  # Gets the rightmost digit. Ex: 569 % 10 is 9.
        currDigitAsChar = DigitToChar(currDigit)  # Ex: 9 becomes character '9'
        numAsString = currDigitAsChar + numAsString
        currNum //= 10  # Shifts the number right one digit. Ex: 569 // 10 is 56.
    
    if userNum == 0:  # 0 is a special case. Above loop never entered.
        numAsString = '0'
    
    return numAsString


# Main function
userNum = int(input())

print(NumToStringWithCommas(userNum))
