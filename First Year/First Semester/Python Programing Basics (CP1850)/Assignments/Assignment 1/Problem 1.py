# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 08:19:16 2023

@author: Michael.Agonsi
"""
#program that converts numerical grade to letter grade

#introducing program
print('Letter Grade Converter')

#assigning variables
grader ='y' or 'Y'
output = 'Letter grade:'

#loop begins

while grader == 'y' or grader =='Y':
    
    #collecting input
    num = int(input('\nEnter numerical grade:\t'))
    
    #checking input and giving output
     
    if (num >= 88 and num <= 100) :
        print(output,'A')
    elif num >= 80 and num <= 87:
        print(output,'B')
    elif num >= 67 and num <= 79:
        print(output,'C')
    elif num >= 60 and num <= 66:
        print(output,'D')
    elif num < 60:
        print(output,'F')
        
    #updating loop for continuation or exit
    grader = input('\nContinue? (y/n): ')
    if grader == 'n' or 'N':
        break 
    
#exiting loop
# else:
#     grader = False

print('')
print('Bye!')