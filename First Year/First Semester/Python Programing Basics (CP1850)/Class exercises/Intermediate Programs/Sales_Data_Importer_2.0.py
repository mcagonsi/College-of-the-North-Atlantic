# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:46:33 2023

@author: Michael.Agonsi
"""
def display_title():
    print('SALES DATA IMPORTER')
    print()
def display_menu():

    print('COMMAND MENU'+
          '\nview - View all sales'+
          '\nadd - Add sales' +
          '\nmenu - Show menu' +
          '\nexit - Exit program')

def cmd_input ():
    print()
    command = input('Please enter a command: ')
    print()
    return command
    
def year_input():
    while True:
        year = int(input('Year:\t\t\t'))
        if year > 1900 and year < 2501:
            return year
            break
        else:
            print('Invalid input. Please try again')
def month_quarter_input():
    while True:
        month = int(input('Month (1-12):\t'))
        if month >= 1 and month <=3:
            quarter = 1
            break
        elif month >= 4 and month <= 6:
            quarter = 2
            break
        elif month >= 7 and month <=9:
           quarter = 3
           break
        elif month >= 10 and month <= 12:
           quarter = 4
           break  
        else:
            print('Please enter a valid data!')
    return month,quarter

def day_input():
    while True:
        day = int(input('Day (01-31):\t\t'))
        if day > 0 and day <32:
            return day
            break
        else:
            print('Please enter a valid data')
    

      
def add_sales ():
    sale = []
    
    
    amount = float(input('Amount:\t\t\t'))
    
    year = year_input()
    month, quarter = month_quarter_input()
    day = day_input()
    
    date = (str(year)+'-'+str(month)+'-'+str(day))
    
    sale.append(date)
    sale.append(quarter)
    sale.append(amount)
    print()
    print('Sales for {} added'.format(date))
    print()
    return sale

def view_sales_list (sales_list):
    print('\t\t\tDate\t\t\t\tQuarter\t\t\t\tAmount')
    print('='*60)
    total = 0
    i = 1
    for   sale in sales_list:
        
        total += sale[2]
        print(i,'\t\t\t', sale[0], '\t\t\t',sale[1],'\t\t\t\t',sale[2])
        i += 1
    
   
    
    print('='*60)   
    print(f'TOTAL:\t\t\t\t\t\t\t\t\t\t\t  {total:.1f}')
    

def main():
    display_title()
    sales_list = []
    display_menu()
    
    while True:
        command = cmd_input().lower()
        if command == 'view':
            check = len(sales_list)
            if check == 0:
                print('No sales to view')
            else:
                view_sales_list(sales_list)
        elif command == 'add':
            sale_data = add_sales()
            sales_list.append(sale_data)
        elif command == 'menu':
            display_menu()
        elif command == 'exit':
            print('\nBye!')
            break
        else :
            print('Invalid command. Please try again')

if __name__ == '__main__':
    main()
    
   
        
   


   
    