# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:38:19 2023

@author: Mayk Al-Ghrawi
"""

def cost_for_miles_gas(miles_driven):
    MILES_PER_GAL = 30
    CENTS_PER_GAL = 400
    cents_gas = (miles_driven * CENTS_PER_GAL) // MILES_PER_GAL
    return cents_gas

def cost_for_miles_maintenance(miles_driven):
    TIRES_CENTS = 50000
    TIRES_MILES = 20000
    SERVICE_CENTS = 30000
    SERVICE_MILES = 10000
    cents_maintenance = ((miles_driven * TIRES_CENTS) // TIRES_MILES) + ((miles_driven * SERVICE_CENTS) // SERVICE_MILES)
    return cents_maintenance

def cost_for_miles(miles_driven):
    return cost_for_miles_gas(miles_driven) + cost_for_miles_maintenance(miles_driven)

miles_driven = int(input())
print(str(cost_for_miles(miles_driven)) + " cents")
