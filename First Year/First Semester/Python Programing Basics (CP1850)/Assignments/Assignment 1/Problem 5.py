# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:28:38 2023

@author: Michael.Agonsi
"""
# program that displays a table of squares and cubes for the specified range of numbers

#introduction of program
print('Table of Powers')
print('')

#collecting input values for start and stop value for the for-loop. 
'''note:i added an increment of 1 to the stop value because the operation will always stop at
at the value before the actual stop value in a for-loop. hence to get desired result the
increment of 1'''

loop = True

while loop == True:
    start = int(input('Start Number:\t'))
    stop = int(input('Stop number:\t')) + 1 #increment of 1 to adjust the stop value
    
    if start > stop: #checking and displaying error message
        print('Your Start value cannot be greater than your stop value! Please try again')
        continue
   
    #giving the output or result for the declared parameters and end loop
    else:
        print('\nNumber\t\tSquared\t\tCubed')
        print(f"{'='*6}\t\t{'='*7}\t\t{'='*6}")
        
        for n in range(start,stop):
            sqd = n**2
            cubd = n**3
          
            print(f"{n}\t\t\t{sqd}\t\t{cubd}")
        break

            