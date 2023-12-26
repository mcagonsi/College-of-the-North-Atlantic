# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:36:52 2023

@author: Michael.Agonsi
"""

def display_menu():
    print('COMMAND MENU')
    print('view - View country name'+
          '\nadd - Add a country'+
          '\ndel - Delete a country'+
          '\nexit - Exit program')
def country_dict():
    country = {'CA': 'Canada',
               'MX': 'Mexico',
               'US': 'United States'}
    return country
def view(COUNTRY):
    for code in COUNTRY.keys():
        print(code, end = ' ')
    print()
    code = input('Enter country code: ').upper()
    if code in COUNTRY.keys():
        print('Country name:{} '.format(COUNTRY[code]))
        
    else:
        print('Country not in list!')
        
def add(COUNTRY):
    code = input('Enter country code: ').upper()
    if code in COUNTRY.keys():
        print('The country is already on the list!')
    else:
        name = input('Enter country name: ').capitalize()
        COUNTRY[code]=name
        print('{} was added.'.format(name))

def delete(COUNTRY):
    code = input('Enter country code: ').upper()
    if code in COUNTRY.keys():
        country = COUNTRY.pop(code)
        print('{} was deleted'.format(country))
    else:
        print('Country code is not on the list')
def main():
    display_menu()
    COUNTRY = country_dict()
    while True:
        cmd = input('Command: ').lower()
        if cmd =='view':
            view(COUNTRY)
        elif cmd == 'add':
            add(COUNTRY)
        elif cmd == 'del':
            delete(COUNTRY)
        elif cmd == 'exit':
            print()
            print('Bye!')
            print()
            break
        else:
            print('INVALID COMMAND! Please Try Again')
if __name__ == '__main__':
    main()