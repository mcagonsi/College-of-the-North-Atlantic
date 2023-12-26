# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:07:58 2023

@author: Michael.Agonsi
"""


def mpg (miles, gallon):
    '''
    

    Parameters
    ----------
    miles : TYPE
        DESCRIPTION.
    gallon : TYPE
        DESCRIPTION.

    Returns
    -------
    miles_per_gallon : TYPE
        DESCRIPTION.

    '''
    if (gallon > 0):
      miles_per_gallon = miles/gallon
      return miles_per_gallon
      
       
    else:
        print("Gallons used must be greater than zero. Try again.")

#starts the loop
cont = 'y'
while (cont.lower()=='y'):
    print('The Miles Per Gallon Program')
    print('')
    #collects inputs
    distance= float(input('Enter miles driven:\t\t\t\t'))
    fuel = float(input('Enter gallons of gas used:\t\t'))
    #calls the function and assign it to a variable
    dToFuel = mpg(distance,fuel)
    print(f"Miles Per Gallon:\t{dToFuel:.1f}")
    print('')
    #upates the loop for continuation or exit
    cont = input('Continue y/n: ')
print("")
print("Bye!")
