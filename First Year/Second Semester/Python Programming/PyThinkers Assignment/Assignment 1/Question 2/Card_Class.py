from dataclasses import dataclass

@dataclass
class Card:
    #Card class with attributes __rank and __suit
    __rank:str = ''
    __suit:str = ''

    def getCard(self):
        """
        Returns a string representation of a card object
        """
        return f"{self.__rank} of {self.__suit}"