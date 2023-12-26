# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 08:55:15 2023

@author: Michael.Agonsi
"""

def display_title():
    print('The Wizard Inventory program')

def display_menu():
    print('\nCOMMAND MENU' +
          '\nshow - Show all items' +
          '\nstore - Show items in store'+
          '\ngrab - Grab an item'+
          '\nedit - Edit an item' +
          '\ndrop - Drop an item' +
          '\nexit - Exit program')
    
def inventory():
    inventory = ['Wooden staff', 'Wizard hat', 'cloth shoes']
    return inventory

def show(wizard_inv):
    
    for i, inv in enumerate(wizard_inv, start =1):
        print('{}. {}'.format(i,inv))

def store():
    magic_store = ['Potion of invisibility', 'Health elixir', 'Power elixir', 'unlimited health']
    return magic_store

def show_store(magicStore):
    for i, item in enumerate(magicStore, start =1):
        print('{}. {}'.format(i,item))

def grab(magicStore, wizard_inv):
    
    num_of_item_in_inv = len(wizard_inv)
    if num_of_item_in_inv < 4: 
        store_item_index = int(input('Item from store: ')) -1
        item_grabbed =  magicStore.pop(store_item_index)
        wizard_inv.append(item_grabbed)
        print('Name: {}'.format(item_grabbed))
        print('{} was added'.format(item_grabbed))
        print()
    else:
        print("You can't carry any more items. Drop something first")
        print()

def edit (wizard_inv):
    index= int(input('Number: '))
    i = index - 1
    wizard_inv[i] = input('Update name: ')
    print('Item number {} was updated'.format(index))
    print()

def drop(wizard_inv):
    index = int(input('Number: '))
    i = index - 1
    item_dropped = wizard_inv[i]
    wizard_inv.remove(item_dropped)
    print('{} was dropped'.format(item_dropped))
    print()

def main():
    display_title()
    display_menu()
    wizard_inv = inventory()
    magicStore = store()
    while True:
        print()
        cmd = input('Command: ').lower()
        print()
        if cmd == 'show':
            show(wizard_inv)
        elif cmd == 'grab':
            grab(magicStore, wizard_inv)
        elif cmd == 'store':
            show_store(magicStore)
        elif cmd == 'edit':
            edit(wizard_inv)
        elif cmd == 'drop':
            drop(wizard_inv)
        elif cmd == 'exit':
            print('\nBye!')
            wizard_inv = inventory()
            break
        else:
            print('Please enter a valid command')
            display_menu()
if __name__ == '__main__': 
    main()

    
    