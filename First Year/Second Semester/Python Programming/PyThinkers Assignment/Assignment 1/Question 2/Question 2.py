from Deck_Class import Deck


def cardsAmount():
    """
    Prompt the user to input the number of cards they want.

    Returns:
    int: The number of cards requested by the user.
    """
    while True:
        try:
            cards_amount = int(input("How many cards would you like?:  "))
            return cards_amount
            break
        except ValueError:
            print()
            print('Invalid input! Please enter an Integer.')
            print()


def main():
    """
    Combines each aspect of the program to run properly.
    """
    print("Card Dealer")
    print()
    deck = Deck()
    deck.getDeck()
    deck.shuffle()
    print()
    cards_amount = cardsAmount()
    print()
    print("Here are your Cards:")
    deck.dealCard(cards_amount)
    print()
    print(deck.countCards())
    print()
    print("Good luck!")


if __name__ == "__main__":
    main()
