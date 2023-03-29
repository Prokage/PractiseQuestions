# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:46:08 2023

@author: Mayk Al-Ghrawi
"""

eString = "e|-"
BString = "B|-"
GString = "G|-"
DString = "D|-"
AString = "A|-"
EString = "E|-"
numChords = int(input())
for i in range(numChords):
    userChord = input()
    if userChord == "G":
        eString += "3-"
        BString += "0-"
        GString += "0-"
        DString += "0-"
        AString += "2-"
        EString += "3-"
    elif userChord == "C":
        eString += "0-"
        BString += "1-"
        GString += "0-"
        DString += "2-"
        AString += "3-"
        EString += "--"
    elif userChord == "D":
        eString += "2-"
        BString += "3-"
        GString += "2-"
        DString += "0-"
        AString += "--"
        EString += "--"
print(eString)
print(BString)
print(GString)
print(DString)
print(AString)
print(EString)
