from dataclasses import dataclass
import random

ROSHAMBO_COLL = ('rock', 'paper', 'scissors')

@dataclass
class Player:
    name: str = ''
    roshambo: str = ROSHAMBO_COLL[0]
    __wins:int = 0
    __losses:int = 0

    def generateRoshambo(self):
        self.__roshambo = ROSHAMBO_COLL[0]

    def play(self, other_player):
        if self.roshambo == other_player.roshambo:
            return None
        else:
            if (self.roshambo == 'rock' and other_player.roshambo == 'scissors') \
                or (self.roshambo == 'paper' and other_player.roshambo == 'rock') \
                    or (self.roshambo == 'scissors' and other_player.roshambo == 'paper'):
                return self
            else:
                return other_player

    @property
    def wins(self):
        return self.__wins

    @property
    def losses(self):
        return self.__losses

    def addWin(self):
        self.__wins += 1

    def addLoss(self):
        self.__losses += 1

    def __str__(self):
        return f'{self.name}: {self.roshambo}'


@dataclass
class Bart(Player):
    def __post_init__(self):
        self.name = 'Bart'


@dataclass
class Lisa(Player):
    def __post_init__(self):
        self.name = 'Lisa'

    def generateRoshambo(self):
        self.roshambo = random.choice(ROSHAMBO_COLL)

def main():
    print("Roshambo Game\n")
    name = input('Enter your name: ')
    print()

    player1 = Player(name)

    opponent = input('Would you like to play against Bart or Lisa?(b/l): ')
    print()

    opponent_chosen = 'n'
    while opponent_chosen == 'n':
        if opponent.lower() == 'b':
            player2 = Bart()
            opponent_chosen = 'y'
        elif opponent.lower() == 'l':
            player2 = Lisa()
            opponent_chosen = 'y'
        else:
            print('Invalid choice, choose between Bart of Lisa (b/l)')

    play_again = 'y'
    while play_again.lower() == 'y':
        # Get Roshambo for player 1
        selection = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        print()

        if selection == 'r':
            player1.roshambo = 'rock'
        elif selection == 'p':
            player1.roshambo = 'paper'
        elif selection == 's':
            player1.roshambo = 'scissors'
        else:
            print('Invalid choice. Select again')
            continue

        # Get Roshambo for player 2
        player2.generateRoshambo()

        # Displaying names and state
        print(player1)
        print(player2)

        # Start the game!
        winner = player1.play(player2)
        if winner is None:
            print('Draw!\n')
        else:
            print(f'{winner.name} wins!\n')
            winner.addWin()
            if winner is player1:
                player2.addLoss()
            else:
                player1.addLoss()

        # Display totals for each player
        print(f'{player1.name}: {player1.wins} total win(s), {player1.losses} total loss(es)')
        print(f'{player2.name}: {player2.wins} total win(s), {player2.losses} total loss(es)')
        print()

        play_again = input('Play again? (y/n): ')
        print()

    print("Thank you for playing Roshambo")


if __name__ == '__main__':
    main()


