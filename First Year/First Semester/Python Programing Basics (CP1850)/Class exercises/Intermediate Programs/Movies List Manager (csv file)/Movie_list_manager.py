# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:49:14 2023

@author: Michael.Agonsi
"""
import csv

def menu ():
    print('COMMAND MENU' +
          '\nlist - List all movies' +
          '\nadd - Add a movie' +
          '\ndel - Delete a movie' +
          '\nexit - Exit the program')
def entry():
    command = input ('\nCommand:\t')
    return command

def read():
    with open('Movies.csv') as movieslist:
        movies = csv.reader(movieslist)
        movies = list(movies)
        return movies

def name_input():
    movie_name = input('Name:\t')
    return movie_name

def year_input():
    year = input('Year:\t')
    return year


def listing_movie(movies):
  
  
        n=1
        for movie in movies:
            print(str(n) + '.'+ str(movie[0]) +" "+ '('+ str(movie[1]) +')')
            n+=1
       
def add_movie(movies):
        name = name_input()
        year = year_input()
        movie = [name, year]
        movies.append(movie)
        print("{} was added".format(name))
def write(movies):
    
    
    with open ('Movies.csv', 'w', newline= '') as movie_list:
        new_movie = csv.writer(movie_list)
        new_movie.writerows(movies)
        

def del_movie(movies):
    num = int(input('Number:\t'))
    i = num -1
    delete = movies.pop(i)
    deleted = delete[0]
    print("{} was deleted".format(deleted))

def main():
    menu()
    movies = read()
    
    
    
    while True:
        choice = entry()
        if choice.lower()=='add':
            add_movie(movies)
            write(movies)
            continue
        elif choice.lower() == 'list':
            listing_movie(movies)
            continue
        elif choice.lower() == 'del':
            del_movie(movies)
            continue
        elif choice.lower() == 'exit':
            write(movies)
            break
        else:
            print('\nPlease Enter A Valid Command from the options above!')
            continue
    print('\nBye!')
    
if __name__ == '__main__':
    main()