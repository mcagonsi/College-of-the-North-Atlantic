# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:24:24 2023

@author: Michael.Agonsi
"""

print('The Miles Per Gallon Program')
print('')
miles = float(input('Enter miles driven:\t\t\t\t'))
gallon = float(input('Enter gallons of gas used:\t\t'))
print('')
#Conditional statement to give result
if (gallon > 0):
    
#The formula for the caluclation
    miles_per_gallon = miles/gallon

#gives result

    print(f'Miles Per Gallon:\t\t\t\t{miles_per_gallon:.2f}')
else:
    print("Gallons used must be greater than zero. Try again.")

print("")
print("Bye!")


#note that in the above function to format the output like a 
#float value you can use ':.{number of decimal place}f'
