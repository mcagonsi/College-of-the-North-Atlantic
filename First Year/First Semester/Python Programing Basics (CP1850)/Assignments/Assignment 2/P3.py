# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 05:16:58 2023

@author: Chidera
"""

def display_title():
    '''
    

    Returns
    -------
    None.

    '''
    print('Welcome to Tic Tac Toe')
    print()
    
    
def display_board():
    '''
    

    Returns
    -------
    None.

    '''
    print('+---'+'+---'+'+---+' + '\n'
          '|   '+'|   '+'|   |' + '\n'
          '+---'+'+---'+'+---+' + '\n'
          '|   '+'|   '+'|   |' + '\n'
          '+---'+'+---'+'+---+'  + '\n'
          '|   '+'|   '+'|   |' + '\n'
          '+---'+'+---'+'+---+' )

def gameplay_input():
    '''
    

    Returns
    -------
    r : TYPE
        DESCRIPTION.
    c : TYPE
        DESCRIPTION.

    '''
    while True:
        try:
            # takes game inputs for game 
            row = int(input('Pick a row(1,2,3): '))
            col = int(input('Pick column (1,2,3,): '))
            print()
            
            r = row - 1
            c = col - 1
            return r,c
        except ValueError:
            print('Invalid entry please try again')
            
def board()-> list: 
    '''
    

    Returns
    -------
    list
        DESCRIPTION.

    '''
    rows = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']]
    return rows


def x_plays(BOARD:list):
    '''
    

    Parameters
    ----------
    BOARD : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    rows = BOARD
    print()
    print("X's Turn")
    while True:
        r,c = gameplay_input()
            
        if (r > 2 or r < 0) or (c < 0 or c > 2):
            print('Invalid inputs. Please try again')
            continue
        
        else:
            if rows[r][c] == ' ':
                rows[r][c] = 'x'
                break
            else:
                print('Cell taken. Please try again')
    
def o_plays(BOARD:list):
    '''
    

    Parameters
    ----------
    BOARD : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    rows = BOARD
    print()
    print("O's Turn")
    while True:
        r,c = gameplay_input()
            
        if (r > 2 or r < 0) or (c < 0 or c > 2):
            print('Invalid inputs. Please try again')
            continue
        
        else:
            if rows[r][c] == ' ':
                rows[r][c] = 'o'
                break
            else:
                print('Row taken.Please try again')
def x_wins(BOARD:list)->bool:
    '''
    

    Parameters
    ----------
    BOARD : list
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    row = BOARD
    if row[0][0] == 'x' and row[0][1] == 'x' and row[0][2] == 'x':
        return True
    elif row[1][0] == 'x' and row[1][1] == 'x' and row[1][2] == 'x':
       return True
    elif row[2][0] == 'x' and row[2][1] == 'x' and row[2][2] == 'x':
       return True
    elif row[0][0] == 'x' and row[1][0] == 'x' and row[2][0] == 'x':
       return True
    elif row[0][1] == 'x' and row[1][1] == 'x' and row[2][1] == 'x':
       return True
    elif row[0][2] == 'x' and row[1][2] == 'x' and row[2][2] == 'x':
       return True
    elif row[0][0] == 'x' and row[1][1] == 'x' and row[2][2] == 'x':
       return True
    elif row[0][2] == 'x' and row[1][1] == 'x' and row[2][0] == 'x':
       return True
    else:
        False
def o_wins(BOARD:list)-> bool:
    '''
    

    Parameters
    ----------
    BOARD : list
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    row = BOARD
    if row[0][0] == 'o' and row[0][1] == 'o' and row[0][2] == 'o':
        return True
    elif row[1][0] == 'o' and row[1][1] == 'o' and row[1][2] == 'o':
       return True
    elif row[2][0] == 'o' and row[2][1] == 'o' and row[2][2] == 'o':
       return True
    elif row[0][0] == 'o' and row[1][0] == 'o' and row[2][0] == 'o':
       return True
    elif row[0][1] == 'o' and row[1][1] == 'o' and row[2][1] == 'o':
       return True
    elif row[0][2] == 'o' and row[1][2] == 'o' and row[2][2] == 'o':
       return True
    elif row[0][0] == 'o' and row[1][1] == 'o' and row[2][2] == 'o':
       return True
    elif row[0][2] == 'o' and row[1][1] == 'o' and row[2][0] == 'o':
       return True
    else:
        False
    
    
def show_play(rows:list):
    '''
    

    Parameters
    ----------
    rows : list
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    print('+---'+'+---'+'+---+' + '\n'
          f'| {rows[0][0]} '+ f'| {rows[0][1]} '+ f'| {rows[0][2]} |' + '\n'
          '+---'+'+---'+'+---+' + '\n'
          f'| {rows[1][0]} '+ f'| {rows[1][1]} '+ f'| {rows[1][2]} |' + '\n'
          '+---'+'+---'+'+---+'  + '\n'
          f'| {rows[2][0]} '+f'| {rows[2][1]} '+f'| {rows[2][2]} |' + '\n'
          '+---'+'+---'+'+---+' )
    print()
    
    
def check_board_full(BOARD:list)-> bool:
    '''
    

    Parameters
    ----------
    BOARD : list
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    '''
    n=0
    for rows in BOARD:
        for col in rows:
           if col == ' ':
               n += 1
    if n == 0 :
        return True
        
       
    
def  main():
    # introduces the game
    display_title()
    display_board()
    
    # calls the list of list 
    BOARD = board()
           
      
    while True:
        
        # X's turn to play
        x_plays(BOARD)
        show_play(BOARD)
        x_wins(BOARD)
        if x_wins(BOARD) == True:
            print('X Wins!')
            break
        
        
        # checks if board is full to confirm a game tie
        if check_board_full(BOARD) == True:
            print('Game ends in a tie')
            break
        
        
        # O's turn to play 
        o_plays(BOARD)
        show_play(BOARD)
        o_wins(BOARD)
        if o_wins(BOARD) == True:
            
            print('O Wins!')
            break
        
    # exiting the game  
    print()
    print('Game Over!')

if __name__ == '__main__':
    main()