# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 09:52:00 2023

@author: Michael.Agonsi
"""

#code that calculates sales tax
subtotal = float(input("Subtotal value: ")) 
tax_percent= float(input("Tax Percent: "))
tax_ammount = subtotal * tax_percent 
grand_total = subtotal + tax_ammount 
print("The sales tax is ", grand_total)