# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:51:30 2023

@author: Chidera
"""
import csv


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

def list_contact(CONTACT:csv):
    '''
    

    Parameters
    ----------
    CONTACT : csv
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    with open (CONTACT) as contact_list:
        contacts = csv.reader(contact_list)
        contacts_list = list(contacts)
        check = len(contacts_list)
        # check if list is empty
        if check == 0:
            print('Contact list is empty')
         # if list is not empty it prints contact list 
        else:
            for i, contact in enumerate(contacts_list, start=1):
                print(f"{i}. {contact[0]}")
            
            
def add_contact(CONTACT:csv):
    '''
    

    Parameters
    ----------
    CONTACT : csv
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
    with open (CONTACT) as contact_list:
        contacts = csv.reader(contact_list)
        current_list = list(contacts)
        
    # appends the contact to the read csv file contact list that has been stored   
    current_list.append(contact)
    new_list = current_list
    
    # writes the new list to the csv file to update it
    with open('contacts.csv','w',newline = "") as new_contact_list:
        writer = csv.writer(new_contact_list)
        writer.writerows(new_list)
    
    print(name +' was added.')

def view_contact(CONTACT:csv):
    '''
    

    Parameters
    ----------
    CONTACT : csv
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # reads the csv file into a list
    with open (CONTACT) as contact_list:
        contacts = csv.reader(contact_list)
        current_list = list(contacts)
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
        
def del_contact(CONTACT:csv):
    '''
    

    Parameters
    ----------
    CONTACT : csv
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    # reads csv file to list
    with open (CONTACT) as contact_list:
        contacts = csv.reader(contact_list)
        current_list = list(contacts)
        
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
    
    new_list = current_list
    
    # writes and updates the new contact list to the csv file
    with open('contacts.csv','w',newline = "") as new_contact_list:
        writer = csv.writer(new_contact_list)
        writer.writerows(new_list)
        

def main():
    CONTACT = 'contacts.csv'
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