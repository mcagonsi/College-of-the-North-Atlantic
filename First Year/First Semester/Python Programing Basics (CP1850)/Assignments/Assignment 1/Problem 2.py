# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:44:20 2023

@author: Michael.Agonsi
"""
# program that calculates the tip for a meal cost and total amount

print('Tip Calculator')
print('')

#collectes input for the meal cost
cost_meal = float(input('Cost of meal:  '))


print('')

#calculation for the different per centage tip    
tip_15 = cost_meal * .15
tip_20 = cost_meal * .20
tip_25 = tip_amount = cost_meal * .25
    
#the output for all the calculations

#output for 15%
print('15%')
print(f"Tip amount:\t\t{tip_15:.2f}")
total = tip_15 + cost_meal
print(f'Total amount:\t{total:.2f}\n')

#output for 20%
print('20%')
print(f"Tip amount:\t\t{tip_20:.2f}")
total = tip_20 + cost_meal
print(f'Total amount:\t{total:.2f}\n')

#output for 25%
print('25%')
print(f"Tip amount:\t\t{tip_25:.2f}")
total = tip_amount + cost_meal
print(f'Total amount:\t{total:.2f}\n')
      
 