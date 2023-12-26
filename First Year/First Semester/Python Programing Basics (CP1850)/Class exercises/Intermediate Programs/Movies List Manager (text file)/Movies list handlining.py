# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 09:33:08 2023

@author: Michael.Agonsi
"""

def menu ():
    print('COMMAND MENU' +
          '\nlist - List all movies' +
          '\nadd - Add a movie' +
          '\ndel - Delete a movie' +
          '\nexit - Exit the program')
def entry():
    command = input ('\nCommand:\t')
    return command

# def movie_list():
#     
#     return movies

def name_input():
    movie_name = input('Name:\t')
    return movie_name




def listing_movie(movies):
    n=1
    for movie in movies:
        print(str(n) + '.',movie)
        n+=1
       
def add_movie(movies):
    
    name = name_input()
    
    # movie = []
    # movie.append(name)
    
    movies.append(name)
    print("{} was added".format(name))
    with open ('Movies list.txt', 'a') as movie_list:
        movie_list.write(name + '\n')
    # return added

def del_movie(movies):
    num = int(input('Number:\t'))
    i = num -1
    delete = movies.pop(i)
    deleted = delete
    print("{} was deleted".format(deleted))
    new_movie_list = movies
    with open ('Movies list.txt', 'w') as  new_list:
        for movie in new_movie_list:
            new_list.write(movie)
    # return delete
def write(movies):
    with open('Movies list.txt', 'w') as movieslist:
        for item in movies:
            movieslist.write(item +'\n')

def main():
    menu()
    with open ('Movies list.txt', 'r') as movies:   
        movies = movies.readlines()
    while True:
        choice = entry()
        if choice.lower()=='add':
            add_movie(movies)
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

