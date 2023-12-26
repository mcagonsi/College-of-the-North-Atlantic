# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:48:39 2023

@author: Michael.Agonsi
"""

#program tha calculates the coins needed to make change for the specified number of cents

#introduction to the program
print('Change Calculator\n')
calc = 'y'
calc = calc.lower()

#loop starts
while calc == 'y':
    #collects input
    money = int(input('Enter number of cents (0-99):\t'))
    
    #calculates the required output
    quarter = money//25
    dimes = (money%25)//10
    nickel = ((money%25)%10)//5
    penny = ((money%25)%10)%5
    
    #prints the output or result
    print(f'\nQuarters:\t{quarter}'+
          f'\nDimes:\t\t{dimes}'+
          f'\nNickels:\t{nickel}'+
          f'\nPennies:\t{penny}')
    
    #to continue the loop
    again = input('Continue? (y/n):\t')
    again = again.lower()
    if again == 'y':
        print('')
        calc == True
        
    #to end the loop
    elif again == 'n':
        print('')
        print('Bye!')
        break
  


