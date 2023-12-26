# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:39:05 2023

@author: Chidera
"""


def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    
    print('Contact Manager')
    print()

def display_menu():
    '''
    

    Returns
    -------
    None.

    '''
    
    print('COMMAND MENU' +
          '\nlist - Display all contacts' +
          '\nview - View a contact' +
          '\nadd  - Add a contact'+
          '\ndel  - Delete a contact' +
          '\nexit - Exit program')
def CONTACTS_list()-> list:
    '''
    

    Returns
    -------
    list
        DESCRIPTION.

    '''
    #list of list for contacts
    list_of_contacts = [['Guido van Rossum','guido@python.org', '+31 0474 33 88 26'],
                        ['Eric Idle', 'eric@ericidle.com', '+44 20 7946 0958' ]]
    return list_of_contacts

def list_contact(CONTACT:list):
    '''
    

    Parameters
    ----------
    CONTACT : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    contacts_list = CONTACT
    check = len(contacts_list)
    # check if list is empty
    if check == 0:
        print('Contact list is empty')
     # if list is not empty it prints contact list 
    else:
        for i, contact in enumerate(contacts_list, start=1):
            print(f"{i}. {contact[0]}")
            
            
def add_contact(CONTACT:list):
    '''
    

    Parameters
    ----------
    CONTACT : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    # takes inputs
    name = input('Name: ')
    email = input('Email: ')
    phone = input('Phone: ')
    # creates a contact details list
    contact = [name,email,phone]
   
    current_list = CONTACT
        
    # appends the contact to contact list   
    current_list.append(contact)

    
   
    
    print(name +' was added.')

def view_contact(CONTACT:list):
    '''
    

    Parameters
    ----------
    CONTACT : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    current_list = CONTACT
    while True:
        # takes input for contact selected
        contact_num = int(input('Number: '))
        i = contact_num - 1
        list_length =  len(current_list)
        # checks the conditions and prints the details of the selected contact
        if contact_num > 0 and contact_num <= list_length:
            contact_to_view = current_list[i]
            print('Name: ', contact_to_view[0])
            print('Email: ', contact_to_view[1])
            print('Phone: ', contact_to_view[2])
            break
        else:
            print('Invalid entry! Contact not on the list, please try again!')
            continue
        
def del_contact(CONTACT:list):
    '''
    

    Parameters
    ----------
    CONTACT : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
   
    current_list = CONTACT
        
    while True:
        # takes input for contact to be deleted
        contact_num = int(input('Number: '))
        i = contact_num - 1
        list_length =  len(current_list)
        #checks conditions for number being on the list and deletes the number
        if contact_num > 0 and contact_num <= list_length:
            contact_del = current_list.pop(i)
            print(contact_del[0],' was deleted.')
            break
        else:
            print('Invalid entry! Contact not on the list, please try again!')
            continue 
    
    
        


def main():
    CONTACT = CONTACTS_list()
    display_title()
    display_menu()
    # starts the loop for command input
    while True:
        print()
        # takes input for different commands
        command = input('Command: ').lower()
        print()
        # checks conditions and executes statements within each condition
        if command == 'list':
            list_contact(CONTACT)
        elif command == 'view':
            view_contact(CONTACT)
        elif command == 'add':
            add_contact(CONTACT)
        elif command == 'del':
            del_contact(CONTACT)
        elif command == 'exit':
            
            break
        else:
            print('Invalid command! Please enter a valid command.')
            display_menu()
    print()
    print('Bye!')
            
if __name__ == '__main__':
    main()