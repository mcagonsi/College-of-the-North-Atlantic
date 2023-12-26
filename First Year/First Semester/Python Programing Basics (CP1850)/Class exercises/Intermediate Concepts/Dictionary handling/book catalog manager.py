# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:06:19 2023

@author: Michael.Agonsi
"""

def display_menu():
    print('COMMAND MENU')
    print('show - Show book info'+
          '\nadd - Add book'+
          '\nedit - Edit book'+
          '\ndel - Delete book'+ 
          '\nlist - List title of books' +
          '\nexit - Exit program')
def book_catalog():
    catalog = {}
    return catalog
def show(CATALOG):
    title = input('Title: ').capitalize()
    if title in CATALOG.keys():
        print()
        print(f'Title: {title}')
        print(f"Author: {CATALOG[title]['author']}")
        print(f"Publication year: {CATALOG[title]['year']}")
        print()
    else:
        print('Sorry, {} does not exist in the catalog.'.format(title))
def add(CATALOG):
    title = input('Title: ').capitalize()
    author = input('Author name: ').capitalize()
    year = int(input('Publication year: '))
    CATALOG[title] = {'author': author, 'year': year}
    print('Book was added successful')
def edit(CATALOG):
    title = input('Title: ').capitalize()
    if title in CATALOG.keys():
        CATALOG[title]['author'] = input('Author name: ').capitalize()
        CATALOG[title]['year'] = int(input('Publication year: '))
    else:
        print('Book is not present in the catalog.')
def delete(CATALOG):
    title = input('Title: ').capitalize()
    if title in CATALOG.keys():
        CATALOG.pop(title)
        print('Book has been deleted.')
    else:
        print('Book not in catalog. Cannot delete book!')
def listbook(CATALOG):
    if len(CATALOG) == 0:
        print('Book Catalog is empty!')
    else:
        for i, book in enumerate(CATALOG.keys(), start =1):
            print('{}. {}'.format(i,book))

def main():
    display_menu()
    print()
    CATALOG = book_catalog()
    while True:
        print()
        
            
        command = input('Command: ').lower()
        print()
        if command == 'show':
            show(CATALOG)
        elif command == 'add':
            add(CATALOG)
        elif command == 'edit':
            edit(CATALOG)
        elif command == 'del':
            delete(CATALOG)
        elif command == 'list':
            listbook(CATALOG)
        elif command == 'exit':
            print()
            print('Bye!')
            break
        else:
            print('Invalid Command! Please Try again')

if __name__ == "__main__":
   main()
