# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 09:51:09 2023

@author: Michael.Agonsi
"""


import Read_and_write_files as rw

def display_menu():
    print('='*70)
    print('\t\t\t\t\t\tBASEBALL TEAM MANAGER')
    print('MENU OPTIONS')
    print('1 - Display Lineup'+
          '\n2 - Add Player'+
          '\n3 - Remove Player'+
          '\n4 - Move Player'+
          '\n5 - Edit player position'+
          '\n6 - Edit player stats'+
          '\n7 - Exit Program')

def POSITIONS():
    pos = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P' )
    return pos
def display_position():
    line_up =POSITIONS()
    for line in line_up:
        print(line, end=' ')
    print()
    print('='*60)
    return line_up
            
        

def display_lineup():
    header =('    Player','POS', 'AT','H','AVG')
    for col in header:
        print(col, end='    ')
    players = rw.r()
        
    for i, player in enumerate(players,start=1):
        print('\n {}    {}     {}     {}    {}     {}'.format(i,col[0],col[1],col[2],col[3],col[4]))
            
    print('-'*60)
        
     
def add_player(players):
    
    
    name = input('Name: ')
    
    while True:
        position = input('Position: ').upper()
        avl_pos = POSITIONS()
       
        n= avl_pos.count(position)
            
        if n ==1 :
            position= position
            break
        else:
            print('Invalid position. Try again')
            continue
    at_bats = int(input('At bats: '))
    hits = int(input('Hits: '))
    avg = round((hits/at_bats),3)
    player = [name,position,at_bats,hits,avg]
    players.append(player)
    print('{} was added'.format(name))
    print()

def remove_player(players):
    n = int(input('Current lineup number: '))
    i = n-1
    remove_player = players.pop(i)
    removed_player = remove_player[0]
    print('{} was removed'.format(removed_player))
    print()

def move_player(players):
    o_line = int(input('Current lineup number: '))
    old = o_line-1
    move_player = players.pop(old)
    moved_player = move_player[0]
    print('{} was selected.'.format(moved_player))
    n_line = int(input('New lineup number: '))
    new = n_line-1
    players.insert(new, move_player)
    print('{} was moved.'.format(moved_player))
    print()

def edit_player_position(players):
    num = int(input('Lineup number: '))
    n =  num - 1
    player = players[n][0]
    print('You selected {}'.format(player))
    
    while True:
        position = input('New position:' )
        if position.lower() == 'c' or position.lower() =='1b' or position.lower() == '2b' or position.lower() =='3b':
            position = position.upper()
            players[n][1] = position
            break
        elif position.lower() == 'ss' or position.lower() =='lf' or position.lower() == 'cf' or position.lower() =='rf' or position.lower()=='p':
            position = position.upper()
            players[n][1] = position
            break
        else:
            print('Invalid position. Try again')
            print('POSITIONS')
            display_position()
            continue
        print('{} was updated.'.format(player))
        print()
    
def edit_player_stats(players):
    num = int(input('Lineup number: '))
    n =  num - 1
    player = players[n][0]
    print('You selected {} AB=0 H=0'.format(player))
    at_bats = int(input('At Bats: '))
    players[n][2] = at_bats
    hits = int(input('Hits: '))
    players[n][3]=hits
    avg = round((hits/at_bats),3)
    players[n][4] = avg
    print('{} was updated.'.format(player))
    print()

def main():
        Players = 'player_lineup.csv'
        display_menu()
        display_position()
        while True:
            menu_option = int(input('Menu Option: '))
            if menu_option == 1:
                display_lineup()
                continue
            elif menu_option == 2:
                add_player(Players)
                continue
            elif menu_option == 3:
                remove_player(Players)
                continue
            elif menu_option == 4:
                move_player(Players)
                continue
            elif menu_option == 5:
                edit_player_position(Players)
            elif menu_option == 6:
                edit_player_stats(Players)
                continue
            elif menu_option == 7:
                print('\nBye!')
                break
            else:
                print('Enter a valid option from above. Please try again!')
                
if __name__ =='__main__':
    main()
