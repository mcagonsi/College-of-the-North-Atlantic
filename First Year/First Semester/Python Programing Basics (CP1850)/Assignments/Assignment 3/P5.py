# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 23:35:09 2023

@author: Chidera
"""
def read()->dict:
    '''
    

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    #this reads the text file and returns it as a dictionary
    with open('monthly_sales.txt') as sales:
        Sales = sales.readlines()
        SALES = [sale.split() for sale in Sales]
        SALES = dict(SALES)
        return SALES
    
def write(SALES:dict):
    '''
    

    Parameters
    ----------
    SALES : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # takes the dictionary, converts it to a 2D list first
    Sales = [[month,sales] for month,sales in SALES.items()]
    Sales_List = []
    for sale in Sales:
        month_sale = ""
        for item in sale: #takes each item in each list of the 2D list and converts it to a string object by joining them
            month_sale += str(item) + "        "
        Sales_List.append(month_sale) #adds each string formed to a list to form a 1D list
    with open('monthly_sales.txt','w',newline='') as sales:
        sales.writelines(str(sale_month)+'\n' for sale_month in Sales_List) #writes the list into the file in the specified format.
    
           
def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Monthly Sales Program')
    print()
def display_menu():
    '''
    

    Returns
    -------
    None.

    '''
    print('COMMAND MENU'+
          '\nview - View sales for specified month'+
          '\nedit - Edit sales for specified month'+
          '\ntotals - View sales summary for year'+
          '\nexit - Exit program')
    print()
def view(SALES:dict):
    '''
    

    Parameters
    ----------
    SALES : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    month = input('Three-letter Month: ').capitalize()
    if month in SALES.keys(): #checks for the entered month in the dictionary and prints the value out
        month_sale = float(SALES[month])
        print('Sales amount for {} is {:,.2f}'.format(month,month_sale))
        print()
    else:
        print('Invalid three-letter month.') #returns this if the month is not in the dictionary
        print()
def edit(SALES:dict):
    '''
    

    Parameters
    ----------
    SALES : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    month = input('Three-letter Month: ').capitalize()
    if month in SALES.keys(): #checks if the entered month is in the dictionary
        
        try:
            SALES[month] = float(input('Sales Amount: ')) #updates the value of the month(key)
            month_sale = SALES[month]
            print('Sales amount for {} is {:,.2f}'.format(month,month_sale))
            print()
            write(SALES) #calls the function to write the updated dictionary into the file
        except ValueError:
            print('Entry cannot be letters!')
    else:
        print('Invalid three-letter month.')
        print()
def totals(SALES:dict):
    '''
    

    Parameters
    ----------
    SALES : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    Sales = [float(sale) for sale in SALES.values()] #converts all the values in dictionary into a float and adds them to a list
    total_sales = sum(Sales) #gets the sum of all the values
    monthly_avg = float(total_sales/len(Sales)) #calculates the average of all the values
    print('Yearly total: {:,.2f}'.format(total_sales))
    print('Monthy average: {:,.2f}'.format(monthly_avg))
    print()
    
def main():
    '''
    

    Returns
    -------
    None.

    '''
    display_title() #introduces the program
    display_menu()  #shows the menu
    SALES = read() 
    while True:
        cmd = input('Command: ').lower()
        if cmd == 'view':
            view(SALES)
        elif cmd == 'edit':
            edit(SALES)
        elif cmd == 'totals':
            totals(SALES)
        elif cmd == 'exit':
            print()
            print('Bye!')
            break
        else: #throws the error if a wrong command is entered
            print('Not a vaid command! Try Again!')
        
if __name__ == '__main__':
    main()