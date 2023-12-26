# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:22:00 2023

@author: Chidera
"""
def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Game Stats program')
    print()
    
def Players()->dict:
    '''
    

    Returns
    -------
    dict
        DESCRIPTION.

    '''
    players = {'joel': {'wins' : 32, 'losses':14, 'ties': 17},
               'mike': {'wins' : 8, 'losses':19, 'ties': 11},
               'elizabeth': {'wins' : 41, 'losses':3, 'ties': 22},
               'chidera': {'wins' : 51, 'losses':2, 'ties': 12},
               'arun': {'wins' : 2, 'losses':42, 'ties': 10},}
    return players

def display_players(PLAYERS:dict):
    '''
    

    Parameters
    ----------
    PLAYERS : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    names = []
    for player in PLAYERS.keys(): #loops through the keys in the dictionary
        names.append(player) # adds the keys to the names list
    names.sort() #arranges the names in alphabetical order
    for name in names:
        print(name.capitalize()) #loops through the names list and print the names
    print()
    
def check_stats(PLAYERS:dict):
    '''
    

    Parameters
    ----------
    PLAYERS : dict
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    cont = 'y'
    while cont == 'y':
        name = input('Enter a player name:  ').lower()
        if name in PLAYERS.keys(): #checks if the name is on the list
            stats = PLAYERS[name] #retrieves the stats for the player name
            #prints the stats
            print('Wins:    {}'.format(stats['wins']))
            print('Losses:  {}'.format(stats['losses']))
            print('Ties:    {}'.format(stats['ties']))
            print()
        else: #throws the response if the name is not in the player list
            print('There is no player named {}'.format(name.capitalize()))
            print()
        cont = input('Continue? (y/n):  ').lower() #takes input to continue or exit the program
        print()
    print()
    print('Bye!')
def main():
    '''
    

    Returns
    -------
    None.

    '''
    display_title() #introduces the program       
    PLAYERS = Players() #calls the function for the dictionary for player list and assigns the variable
    display_players(PLAYERS) #displays players in the list
    check_stats(PLAYERS)
    
if __name__ == '__main__':
    main()