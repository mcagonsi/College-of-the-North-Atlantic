# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:28:38 2023

@author: Michael.Agonsi
"""

print('='*65)
print('Shipping Calculator')
print('='*65)

#assign variabes

cost1 = 5.95
cost2 = 7.95
cost3 = 9.95
cost4 = 'FREE'
calc = True

#starting the while loop
while calc == True:
    cost_of_item = float(input('Cost of items ordered:\t'))
    if cost_of_item <=0:
        print('You must enter a positive number. please try again')
        continue
    
    elif cost_of_item < 30.00 and cost_of_item > 0:
        total = cost1 + cost_of_item
        print(f'Shipping cost:\t\t\t{cost1:.2f}' + 
                  f'\nTotal cost:\t\t\t\t{total:.2f}')
    elif cost_of_item >= 30.00 and cost_of_item <= 49.99:
        total = cost1 + cost_of_item
        print(f'Shipping cost:\t\t\t{cost2:.2f}' + 
                  f'\nTotal cost:\t\t\t\t{total:.2f}')
    elif cost_of_item >=50.00 and cost_of_item <=9.95:
        total = cost1 + cost_of_item
        print(f'Shipping cost:\t\t\t{cost3:.2f}' + 
                  f'\nTotal cost:\t\t\t\t{total:.2f}')
    elif cost_of_item < 30.00:
        total = cost1 + cost_of_item
        print(f'Shipping cost:\t\t\t{cost4}' + 
                  f'\nTotal cost:\t\t\t\t{total:.2f}')
        
    #exiting the while loop    
    again = input('Continue? (y/n): ')
    print('_'*65+'\n')
    again = again.lower()
    if again == 'y':
            calc = True
    elif again == 'n':
        break
            