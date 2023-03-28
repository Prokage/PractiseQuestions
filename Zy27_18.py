# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 11:29:19 2023

@author: Mayk Al-Ghrawi
"""

user_rows = int(input())
user_cols = int(input())

print("<table>")
for i in range(user_rows):
    print("<tr> ", end="")
    for j in range(user_cols):
        print("<td> c </td> ", end="")
    print("</tr>")
print("</table>")
