from Dice_Roller_Classes import Die
from dataclasses import dataclass, field


@dataclass
class Game:
    __turn: int = 1
    __score: int = 0
    __scoreThisTurn: int = 0
    __isTurnOver: bool = False
    __isGameOver: bool = False
    __die: Die = field(default_factory=Die)

    def play(self):
        while not self.__isGameOver:
            self.take_turn()

    def take_turn(self):
        print('TURN', self.__turn)
        self.__scoreThisTurn = 0
        self.__isTurnOver = False
        while not self.__isTurnOver:
            choice = input("Roll or Hold? (r/h): ")
            if choice.lower() == 'r':
                self.roll_die()
            elif choice.lower() == 'h':
                self.hold_turn()
            else:
                print("Invalid input. Check the options and try again.")

    def roll_die(self):
        self.__die.roll()
        print("Die: ", self.__die.get_value)
        if self.__die.get_value == 1:
            self.__scoreThisTurn = 0
            self.__turn += 1
            self.__isTurnOver = True
            print("This turn is over. You get no score. \n")
        else:
            self.__scoreThisTurn += self.__die.get_value

    def hold_turn(self):
        self.__score += self.__scoreThisTurn
        self.__isTurnOver = True
        print("Score for turn: ", self.__scoreThisTurn)
        print("Total Score: ", self.__score, '\n')
        if self.__score >= 20:
            self.__isGameOver = True
            print("You finished in ", self.__turn, " turns!")
        else:
            self.__turn += 1
