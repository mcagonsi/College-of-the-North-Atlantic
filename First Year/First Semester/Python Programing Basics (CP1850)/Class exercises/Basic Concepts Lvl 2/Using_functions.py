# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 09:57:14 2023

@author: Michael.Agonsi
"""

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))


def addition():
    '''
    

    Returns
    -------
    ans : TYPE
        DESCRIPTION.

    '''
    ans = x+y
    return ans
def subtraction():
    '''
    

    Returns
    -------
    ans : TYPE
        DESCRIPTION.

    '''
    ans=x-y
    return ans
def division():
    ans = x/y
    return ans

print(addition(),
subtraction(),
division())
