import Card_Class
import random

class Deck:
    """
    A class representing a deck of playing cards.

    Attributes:
    cards (list): A list containing Card objects representing the cards in the deck.
    """
    def __init__(self, cards = []):
        """
        Initializes a Deck object with a list of Card objects.

        Args:
        cards (list, optional): A list of Card objects representing the cards in the deck. Defaults to an empty list.
        """
        self.cards = cards

    def getDeck(self) :
        """
        Fills the deck with a standard 52-card deck.
        """
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for suit in suits:
            for rank in ranks:
                card = Card_Class.Card(str(rank), suit)
                self.cards.append(card)

    def shuffle(self):
        # shuffles the Deck
        random.shuffle(self.cards)
        print('I have shuffled a deck of 52 cards.')

    def countCards(self):
        """
        Returns the number of cards remaining in the deck.

        Returns:
        str: A string indicating the number of cards remaining in the deck.
        """
        return f"There are {len(self.cards)} cards left in the deck."

    def dealCard(self, num:int):
        """
        Deals a specified number of cards from the deck.

        Args:
        num (int): The number of cards to deal from the deck.
        """
        for i in range(num):
            card = self.cards.pop()
            print(card.getCard())

