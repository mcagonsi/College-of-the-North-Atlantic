# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 08:38:55 2023

@author: Michael.Agonsi
"""

# def print_welcome():
#     print("Welcome to your first function!")
#     print()
#     print("Done with the function")
    
# print_welcome()


# def print_welcom(message):
#     print(message)
#     print()
#     print('Done with the function')
    
# some_var = 'I am so sleepy'
# print_welcom(some_var)

def cal_mpg(miles_driven, gallons_fuel):
    '''
    The is function calculates and returns miles per gallon

    Parameters
    ----------
    miles_driven : TYPE
        DESCRIPTION.
    gallons_fuel : TYPE
        DESCRIPTION.

    Returns
    -------
    mpg : TYPE
        DESCRIPTION.

    '''
    mpg = miles_driven/gallons_fuel
    return mpg

miles = 500
fuel = 14

calculated_mpg = cal_mpg(miles, fuel)
print(calculated_mpg)