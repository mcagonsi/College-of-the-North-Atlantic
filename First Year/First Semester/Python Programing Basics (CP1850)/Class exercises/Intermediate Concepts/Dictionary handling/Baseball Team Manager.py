# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:20:49 2023

@author: Michael.Agonsi
"""

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
def positions():
    pos = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
    return pos
def display_position():
    pos = positions()
    for i in pos:
        print(i, end =', ')
    print('='*60)
    
def add_player(PLAYERS):
    pos = positions()
    
    name = input('Name: ')
    
    while True:
        POS = input('Position: ').upper()
        if POS in pos:
            AB = int(input('At bats: '))
            H = int(input('Hits: '))
            AVG = round((H/AB),3)
            PLAYERS[name] = {'POS': POS,
                            'AB': AB,
                            'H': H,
                            'AVG': AVG}
            
            print('{} was added'.format(name))
            print()
            break
        else:
            print('Invalid position. Try again')
            continue
def display_lineup(PLAYERS):
    
    if len(PLAYERS) == 0:
        print('-'*60)
        print('No player in line up')
    else:
        print('\tPlayer\t\t\tPOS\t\t\t\tAB\t\tH\t\tAVG')
        print('-'*60)
        i = 1
        for player,details in PLAYERS.items():
                print(f"{i}. {player}\t{details['POS']}\t\t\t\t{details['AB']}\t\t{details['H']}\t\t{details['AVG']}")
                i+=1
        print() 
def remove_player(PLAYERS):
    name = input('Player Name: ')
    if name in PLAYERS.keys():
        PLAYERS.pop(name)
        print('{} was removed.'.format(name))
    else:
        print('Player is not in the lineup!')
def move_player(PLAYERS):
    PlayerToMove = input('Player: ')
    
    if PlayerToMove in PLAYERS.keys():
        PlayerReplaced = input('Player: ')
        PLAYERS.insert(PlayerReplaced, PlayerToMove)
        print('{} moved successfully'.format(PlayerToMove))
        
    else:
        print("Error! Invalid input!")
def edit_position(PLAYERS):
    player = input('Player Name: ')
    if player in PLAYERS:
        pos = positions()
        while True:
            POS = input('Position: ').upper()
            if POS in pos:
                PLAYERS[player]['POS'] = POS
                print('Player position changed successfully.')
                break
            else:
                 print('Not a valid positon! Please try again!')
                 continue
    else:
        print('Player not in lineup!')
def edit_stats(PLAYERS):
    player = input('Player Name: ')
    if player in PLAYERS:
        AB = int(input('At Bats: '))
        H = int(input('Hits: '))
        PLAYERS[player]['AB'] = AB
        PLAYERS[player]['H'] = H
        AVG = round(H/AB,3)
        PLAYERS[player]['AVG'] = AVG
        print("{}'s stats successfully changed".format(player))
    else:
        print('Player not in the line up!')
        
        
        
        
            
def main():
    PLAYERS = {'Michael Agonsi' :{'POS': 'CB',
                    'AB': 50,
                    'H': 2,
                    'AVG': 0.134}}
    display_menu()
    display_position()
    while True:
        option = int(input('Menu option: '))
        if option == 1:
            display_lineup(PLAYERS)
        elif option == 2:
            add_player(PLAYERS)
        elif option == 3:
            remove_player(PLAYERS)
        elif option == 4:
            move_player(PLAYERS)
            
        elif option == 5:
            edit_position(PLAYERS)
        elif option == 6:
            edit_stats(PLAYERS)
        elif option == 7 :
            print()
            print('Bye!')
            break
        else:
            print('Invalid option! Please try again')
if __name__ == '__main__':
    main()