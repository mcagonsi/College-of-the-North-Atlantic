# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:22:21 2023

@author: Michael.Agonsi
"""



def futureValueCalculator (mon_inv, yr_intr, num_yr):
        '''
        This code calculates and returns the future value

        Parameters
        ----------
        mon_inv : TYPE
            DESCRIPTION.
        yr_intr : TYPE
            DESCRIPTION.
        num_yr : TYPE
            DESCRIPTION.

        Returns
        -------
        futureValue : TYPE
            DESCRIPTION.

        '''
        mon_rate = (yr_intr/12)/100
        total_mon = num_yr*12
        futureValue = 0
        for i in range(0,total_mon):
            futureValue += mon_inv
            mon_intr = futureValue * mon_rate
            futureValue += mon_intr
        return futureValue
if __name__ == '__main__':
    loop = 'y'
    loop = loop.lower()
    while loop == "y":
        monthlyInvestment = float(input('Enter monthly investment:\t'))
        yearlyInterestRate = float(input('Enter yearly interest rate:\t'))
        numberOfYears = int(input('Enter number of years:\t'))
    futureValue=futureValueCalculator (monthlyInvestment, yearlyInterestRate, numberOfYears)
    print(f'Future Value:\t{futureValue:.2f}') 
    loop = input('Continue? (y/n): ')
   

   




