# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:48:17 2023

@author: Chidera
"""
from Deck_of_cards_list import deck_of_cards as cards_deck
import getting_money as gm


def title_and_option():
    
    print('BLACKJACK!')
    print('Blackjack payout is 3:2')
    print('Enter \'x\' for bet to exit')
    print('\n\n')
    
def start_money(s_money):
    while True:
        
        if s_money < 5:
            print ('Minimum amount of starting money should be 5')
            
        elif s_money > 10000:
            print ('Maximum amount of starting money should be 10,000')
        else:
            print(f'Your Balance: {s_money}')
            break
            return s_money

def bet_amount(s_money):

    loop = True
    while loop == True:
        print()
        b_amount = input('Bet amount:\t\t')
        if b_amount == 'x':
            gm.update_s_money(str(int(s_money)))
            print()
            print('Bye!')
            break
        elif float(b_amount) < 5 :
            print('Minimum bet amount should be 5')
            continue
        elif float(b_amount) > s_money:
            print('The bet can\'t be greater than player\'s current amount of money')
            continue
                     
        elif float(b_amount) > 1000:
            print ('Maximum bet amount should be 1000')
            continue
        else:
            b_amount = float(b_amount)
            return b_amount
        
def blackjack(s_money,b_amount):
    blackjack = float((b_amount*1.5)+s_money)
    return blackjack
def win(s_money, b_amount):
    win = float(s_money + b_amount) 
    return win
def push(s_money):
    push = float(s_money)
    return push
def lose(s_money, b_amount):
    lose = float(s_money - b_amount)
    return lose

def select_card(shuffled_cards):

    card = shuffled_cards.pop(0)
    return card

def choice():
    while True:
        choice = input('\nHit or Stand? (h/s):\t').lower()
        print()
        if choice =='h' or choice =='s':
            return choice
            break
        else:
            print('You cannot "split" a hand or "double down". Please enter a valid choice!')
            continue

    
def dealer_hand(shuffled_cards):
    dealer = []
    dealer_card1 = select_card(shuffled_cards)
    dealer.append(dealer_card1)
    dealer_card2 = select_card(shuffled_cards)
    dealer.append(dealer_card2)
    return dealer

def player_hand(shuffled_cards):
    player = []
    player_card1 = select_card(shuffled_cards)
    player.append(player_card1)
    player_card2 = select_card(shuffled_cards)
    player.append(player_card2)
    return player



def players_cards(player_cards):
    print('\nYOUR CARDS:')
    for card in player_cards:
        print(card[0] + ' of ' + card[1])
    
def players_points(player_cards):
    total_point = 0
    ace =0
    for card in player_cards:
        total_point += card[2]
        if card[0] == 'Ace':
            ace += 1
    if ace > 0 and total_point <= 10 :
        total_point = total_point + (ace*10)
    elif ace > 0 and (total_point >= 17 and total_point <= 21):
        total_point = total_point + (ace - 1)
    
   
    return total_point

def dealers_cards(dealer_cards):
    print("DEALER'S CARDS:")
    for card in dealer_cards:
        print(card[0] + ' of ' + card[1])
    print()
    
def dealers_points(dealer_cards):
    total_point = 0
    ace = 0
    for card in dealer_cards:
        total_point += card[2]
        if card[0] == 'Ace':
            ace += 1
    if ace > 0 and total_point <= 10 :
        total_point = total_point + (ace*10)
    elif ace > 0 and (total_point >= 17 and total_point <= 21):
        total_point = total_point
    
    return total_point
def adding_card_to_both(shuffled_cards,player_cards, dealer_cards):
    card1 = select_card(shuffled_cards)
    player_cards.append(card1)
    card2 = select_card(shuffled_cards)
    dealer_cards.append(card2)
    
    


def main():
    title_and_option() #introduce the game
    s_money = gm.read_s_money()
    
    
    
    while True:
        if s_money <= 5:
            buy = 'y'.lower()
            while buy == 'y':
                buy = input('You are low on money! Buy more chips (y/n) ?: ').lower()
                if buy == 'y':
                    gm.buy_chips(s_money)
                    gm.update_s_money(s_money)
                    break
                elif buy == 'n':
                    break
                else:
                    print('Invalid entry please try again')
                    continue
        else:
            bet_input = bet_amount(s_money)
            print()
            if bet_input == None:
                
                break
            else:
            
                shuffled_cards = cards_deck()
                dealer_cards = dealer_hand(shuffled_cards)
                player_cards = player_hand(shuffled_cards)
                
            
                print("DEALER'S SHOW CARD:")
                print(dealer_cards[0][0] + ' of ' + dealer_cards[0][1])
                print()
                players_cards(player_cards)
                players_points(player_cards)
                print(f"Total: {players_points(player_cards)}\n")
                players_total = players_points(player_cards)
                dealers_total = dealers_points(dealer_cards)
                
                
                
                if players_total > 21:
                    s_money = lose(s_money, bet_input)
                    print()
                    print('You Bust!')
                    print(f"Money: {s_money}")
                    continue
                elif players_total == 21:
                    s_money = blackjack(s_money, bet_input)
                    print()
                    print('You got a Blackjack!')
                    print(f"Money: {s_money}")
                    continue
                else:
                    if players_total == dealers_total:
                        s_money = push(s_money)
                        print()
                        print('You Push!')
                        print(f'Money: {s_money}')
                        
                    elif players_total < 21:
                        while True:
                            player_choice = choice()
                            
                            if player_choice == 'h':
                                adding_card_to_both(shuffled_cards, player_cards, dealer_cards)
                                players_cards(player_cards)
                                players_total = players_points(player_cards)
                                print(f'Total: {players_total}')
                                print()
                                
                                if players_total > 21:
                                    s_money = lose(s_money, bet_input)
                                    print()
                                    print('You Bust!')
                                    print(f"Money: {s_money}")
                                    break
                                else:
                                    continue #checks the condition for H
                            elif player_choice == 's':
                                dealers_total = dealers_points(dealer_cards)
                                while True:
                                    if dealers_total >= 17 :
                                        dealers_cards(dealer_cards)
                                        players_total = players_points(player_cards)
                                        dealers_total = dealers_points(dealer_cards)
                                        print(f'\nYOUR POINTS: {players_total}')
                                        print(f"DEALER'S POINTS: {dealers_total}")
                                        print()
                                        if dealers_total > 21:
                                            s_money = win(s_money, bet_input)
                                            print()
                                            print('Hooray! You Win!')
                                            print(f"Money: {s_money:.2f}")
                                        elif players_total < dealers_total:
                                            s_money = lose(s_money, bet_input)
                                            print()
                                            print('You Lose!')
                                            print(f"Money: {s_money:.2f}")
                                            break
                                        elif players_total > dealers_total:
                                            s_money = win(s_money, bet_input)
                                            print()
                                            print('Hooray! You Win!')
                                            print(f"Money: {s_money:.2f}")
                                        elif players_total == dealers_total:
                                            s_money = push(s_money)
                                            print()
                                            print('You Push!')
                                            print(f"Money: {s_money:.2f}")
                                        print()
                                        
                                        break
                                    elif dealers_total < 17 :
                                        adding_to_dealer = select_card(shuffled_cards)
                                        dealer_cards.append(adding_to_dealer)
                                        dealers_total = dealers_points(dealer_cards)
                                        continue
                                   
                                    else:
                                        dealers_cards(dealer_cards)
                                        players_total = players_points(player_cards)
                                        dealers_total = dealers_points(dealer_cards)
                                        print(f'YOUR POINTS: {players_total}')
                                        print(f"DEALER'S POINTS: {dealers_total}")
                                        s_money = win(s_money, bet_input)
                                        print()
                                        print('Hooray! You Win!')
                                        print(f"Money: {s_money:.2f}")
                                        break
                                        
                                break
                           
                        continue           
                

if __name__ == '__main__':
    main()





