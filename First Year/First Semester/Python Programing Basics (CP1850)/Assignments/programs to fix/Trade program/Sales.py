# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:18:51 2023

@author: Michael.Agonsi
"""

import csv
def display_title():
    print('SALES')
    
def get_item_prices():
    print("Enter 'x' to pay")
    prices = []
    while True:
        barcode = input('Enter Barcode: ')
        if barcode == 'x':
            break
        else:
            barcode = int(barcode)
            with open('products_records.csv') as products:
                catalog = csv.reader(products)
                for item in catalog:
                    if barcode == int(item[0]):
                        if item[3] == 'AVL':
                            prices.append(float(item[2]))
                        else:
                            print('ITEM HAS BEEN SOLD')
                if len(prices) == 0:
                    print('ITEM NOT FOUND!')
        prices = sum(prices)
        total_cost(prices)

def total_cost(prices):
    prices = get_item_prices()
    print ('COST: {}'.format(prices))
    print ('TAXES: {}'.format(prices*0.15))
    print ('TOTAL COST: {}'.format(prices*1.15))
get_item_prices()
