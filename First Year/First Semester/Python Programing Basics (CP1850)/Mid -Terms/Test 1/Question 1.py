# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:14:50 2023

@author: Michael.Agonsi
"""

#taking input from the user
year_input = int(input('Enter the value for year:\t'))



#condition expressions for output

if (year_input % 400== 0) : #conditions for leap year
    print("True")
    if (year_input % 100 == 0) :
        if(year_input % 4 == 0):
            print('True')
        else:
            print('False')# conditions for confirming leap year or not
    else:
        print('False')
else:  #condition if not leap year
    print('False')

