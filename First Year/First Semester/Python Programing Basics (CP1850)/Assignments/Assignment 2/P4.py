# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:23:03 2023

@author: Chidera
"""


def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('The Wizard Inventory program')
    

def display_menu():
    '''
    

    Returns
    -------
    None.

    '''
    print('\nCOMMAND MENU' +
          '\nwalk - Walk down the path'+
          '\nshow - Show all items' +
          '\ndrop - Drop an item' +
          '\nexit - Exit program')
    
    
def read_inv()->list:
    '''
    

    Returns
    -------
    list
        DESCRIPTION.

    '''
    # reads the wizard inventory file
    with open ('wizard_inventory.txt','r', newline='') as w_inventory:
        wizard_inv = w_inventory.readlines()
    return wizard_inv

def show(wizard_inv:list):
    '''
    

    Parameters
    ----------
    wizard_inv : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # lists out items in the wizard inventory
    check = len(wizard_inv)
    if check == 0: #if wizard inventory is empty it gives the output below
        print('Nothing in inventory.')
    else:
        for i, inv in enumerate(wizard_inv, start =1):
            print('{}. {}'.format(i,inv))
            

def grab(wizard_inv:list,items_to_grab:list,i:int):
    '''
    

    Parameters
    ----------
    wizard_inv : list
        DESCRIPTION.
    items_to_grab : list
        DESCRIPTION.
    i : int
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # grabs the selected item, appends it to the wizard inventory list if the condition is met
    # and write the updated list into the wizard inventory file or return the error if conditions
    # are not met
    if  len(wizard_inv) < 4: #ensures that the maximum number of items that the wizard can carry is 4
        wizard_inv.append(items_to_grab[i])
        with open('wizard_inventory.txt', 'w', newline='\n') as w_inv:
            w_inv.writelines(wizard_inv)
        print('You picked up',items_to_grab[i])
        print()
    else:
        print("You can't carry any more items. Drop something first")
        print()
        
        
        
def walk(wizard_inv:list):
    '''
    

    Parameters
    ----------
    wizard_inv : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    import random
    # reads the wizard all items files and creates a list of all_files
    with open ('wizard_all_items.txt') as wizard_items:
        all_items = wizard_items.readlines()
     
    items_to_grab=[]
    
    # checks conditions for creating the list of items to grab that are not present in the wizards
    # inventory
    if len(wizard_inv) == 0 :
        items_to_grab = all_items
    else:
        for item in all_items:
            num = wizard_inv.count(item)
            if num == 0 :
                items_to_grab.append(item)
    # randomly selects an item to grab from the list of items_to_grab created 
    i = random.randint(1,len(items_to_grab)) - 1
    print('While walking down a path, you see', items_to_grab[i])
    action = input('Do you want to grab it? (y/n): ').lower()
    if action == 'y':
        grab(wizard_inv,items_to_grab,i)
    






def drop(wizard_inventory:list):
    '''
    

    Parameters
    ----------
    wizard_inventory : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # takes input for selected item to drop
    index = int(input('Number: '))
    # checks if the seletion is within the range of number of items in the wizard inventory
    if index >=1 and index <= len(wizard_inventory):
        i = index - 1
        item_dropped = wizard_inventory[i]
        wizard_inventory.remove(item_dropped)
        # after dropping item the wizard_inventory file is updated by writing the new wizard inventory list into it
        with open('wizard_inventory.txt','w', newline='\n') as wiz_inv:
            wiz_inv.writelines(wizard_inventory)
        print('you dropped {}'.format(item_dropped))
        print()
        
    else: #gives error message if the selection is invalid
        print('Selection not in inventory!')
        

def main():
    # introduces the program
    display_title()
    display_menu()
    #creates the wizard inventory list by reading the wizard inventory file
    wizard_inventory = read_inv()
    
    # starts the loop
    while True:
        print()
        # takes input command
        cmd = input('Command: ').lower()
        print()
        if cmd == 'walk':
            walk(wizard_inventory)
        elif cmd == 'show':
            show(wizard_inventory)
        elif cmd == 'drop':
            drop(wizard_inventory)
        elif cmd == 'exit':
            print('\nBye!')
            break
        else:
            # prints error for invald command input
            print('Please enter a valid command')
            display_menu()
            
            
            
if __name__=='__main__':   
    main()


    
    