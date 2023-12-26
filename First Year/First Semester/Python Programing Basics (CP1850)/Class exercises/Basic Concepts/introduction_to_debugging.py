# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 08:47:20 2023

@author: Michael.Agonsi
"""

def calculate_future_value(monthly_investment = 100, yearly_interest =12, years =10):
    
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years *12
    
    
    future_value = 0.0
    for i in range (1, months ): #a colon was missing and a + 1 was missing with the months to specify the exact month 
        future_value += monthly_investment #monthly_investment_amount is an undefined variable
        monthly_interest = future_value * monthly_interest_rate
                        #wrong indentation for monthly_interest_rate 
        future_value += monthly_interest
        return future_value
    
    ''' this code contains syntax error and logical errors.'''