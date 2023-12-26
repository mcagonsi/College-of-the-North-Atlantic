# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:41:21 2023

@author: Michael.Agonsi
"""

#Introducing the program
print('='*65)
print('Shipping Calculator')
print('='*65)


#loop for the program
loop = 'y'
while loop.lower() == 'y':
    item_cost = float(input('Cost of items ordered:\t')) #collecting input from user
    
    #checks the conditions for the shipping cost
    if item_cost < 0:
        print("You must enter a positive number. Please try again.")
        continue
    elif item_cost < 30.00:
        shipping = 5.95
    elif item_cost >= 30.00 and item_cost <=49.99:
        shipping = 7.95
    elif item_cost >= 50.00 and item_cost <= 74.99:
        shipping = 9.95
    elif item_cost >= 75.00:
        shipping = 0
    
    #calculates the total cost
    total_cost = item_cost + shipping
    
    #gives the output for the shipping cost and the total cost
    print(f"Shipping cost:\t\t\t{shipping:.2f}" +
          f"\nTotal cost:\t\t\t\t{total_cost:.2f}")
    
    #updates the condition for the loop
    loop = input("\nContinue ? (y/n):\t")
    print('='*65)
 
#exits the program
print('Bye!')
    