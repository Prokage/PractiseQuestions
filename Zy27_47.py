# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:43:37 2023

@author: Mayk Al-Ghrawi
"""

def CalculateMonthElectricCost(monthKWh, tier1Cutoff, tier1Cost, tier2Cutoff, tier2Cost, tier3Cost):
    remainingKWh = monthKWh
    monthCost = 0.0
    
    # monthKWh can be considered as having 3 parts on a numberline: 1111122222222223333
    # (The number of 1's, 2's, and 3's above is arbitrary, for illustrative purposes only). 
    # The first branch below multiplies part 3 by tier3Cost
    # The second branch multiplies part 2 by tier2Cost
    # Finally, part 1 is muliplied by tier1Cost

    if remainingKWh > (tier2Cutoff + tier1Cutoff): # Calculate the tier 3 amount
        tierKWh = remainingKWh - (tier2Cutoff + tier1Cutoff)
        monthCost += tierKWh * tier3Cost # The difference is the 3333 part above
        remainingKWh -= tierKWh # This gets rid of the 3333 part, leaving the 11111222222222 part

    if remainingKWh > tier1Cutoff: # Calculate the tier 2 amount
        tierKWh = remainingKWh - tier1Cutoff
        monthCost += tierKWh * tier2Cost # The difference is the 2222222222 part
        remainingKWh -= tierKWh # This gets rid of the 2222222222 part

    monthCost += remainingKWh * tier1Cost # The difference is the 11111 part above

    return monthCost


# Main function
monthKWh = float(input())
tier1Cutoff, tier1Cost = map(float, input().split())
tier2Cutoff, tier2Cost, tier3Cost = map(float, input().split())

monthCost = CalculateMonthElectricCost(monthKWh, tier1Cutoff, tier1Cost, tier2Cutoff, tier2Cost, tier3Cost)

print(f"${monthCost:.2f}")
