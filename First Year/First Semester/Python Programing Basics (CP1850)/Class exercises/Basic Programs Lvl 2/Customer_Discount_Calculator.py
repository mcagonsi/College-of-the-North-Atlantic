# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:03:13 2023

@author: Michael.Agonsi
"""

#customer discount calculator
#introdution
print('Let\'s see if you get a discount')

#getting customer input
customerType= input('Enter customer type' + 
                    '\nR-Retail \nW-Wholesale \nEnter R/W: ')
invoiceTotal= int(input('Your Invoice Total:\t'))
#conditional statements

if customerType == "r" or customerType =="R":
    
    if invoiceTotal < 250:
        discountPercent= 0
        print ('You have to pay ', invoiceTotal)
    else :
        discountPercent= 0.2
        invoiceDiscount= discountPercent*invoiceTotal
        finalPay= invoiceTotal-invoiceDiscount
        print('You get 20% off')
        print('You have to pay', finalPay)
elif customerType == "w" or customerType == "W":
    discountPercent = 0.4   
    invoiceDiscount= discountPercent*invoiceTotal
    finalPay= invoiceTotal-invoiceDiscount
    print('You get 40% off')
    print('You have to pay', finalPay)
    
  
else:
    print('You have to enter either R or W')


               