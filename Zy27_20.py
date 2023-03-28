# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:31:12 2023

@author: Mayk Al-Ghrawi
"""

idToFind = input("Enter ID to find: ")
dbId = ""
dbFirstName = ""
dbLastName = ""

try:
    with open("CustomerDb.txt") as customerDb:
        # Loop through each line in the file
        for line in customerDb:
            # Split the line into a list of words
            words = line.split()
            # Get the ID, first name, and last name
            dbId = words[0]
            dbFirstName = words[1]
            dbLastName = words[2]
            # If the ID matches, print the first and last name and exit the loop
            if dbId == idToFind:
                print(dbFirstName, dbLastName)
                break
        else: # This block will execute if the loop completes without a break statement
            print("Not found")
except FileNotFoundError:
    print("Could not open CustomerDb.txt")
