from dataclasses import dataclass
import random

@dataclass
class Player:
    name:str =''
    value:str = ''
    wins:int = 0
    losses:int = 0

    def generateRoshambo(self):
        self.value = 'rock'
    def setValue(self,choice):
        if choice == 'r':
            self.value = 'rock'
        elif choice == 'p':
            self.value = 'paper'
        elif choice == 's':
            self.value = 'scissors'
        else:
            self.value = 'invalid'
    def play(self, player):
        values = ('rock', 'paper', 'scissors')
        while True:
            choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
            self.setValue(choice)
            if self.value in values:
                player.generateRoshambo()
                print(f'{self.name}: {self.value}')
                print(f'{player.name}: {player.value}')
                if self.value == player.value:
                    print('Draw!')
                elif self.value == 'rock' and player.value == 'scissors':
                    self.wins +=1
                    player.losses +=1
                    print(f'{self.name} wins!')
                elif self.value == 'paper' and player.value == 'rock':
                    self.wins +=1
                    player.losses +=1
                    print(f'{self.name} wins!')
                elif self.value == 'scissors' and player.value == 'paper':
                    self.wins +=1
                    player.losses +=1
                    print(f'{self.name} wins!')
                else:
                    self.losses+=1
                    player.wins+=1
                    print(f'{player.name} wins!')
                break
            else:
                print('Invalid choice')
    def endGame(self,player):
        print(f'{self.name}'.upper())
        print(f'Wins: {self.wins}')
        print(f'Losses: {self.losses}')
        print()
        print(f'{player.name}'.upper())
        print(f'Wins: {player.wins}')
        print(f'Losses: {player.losses}')\

        print()
        print('Thank you for playing!')


@dataclass
class Bart(Player):
    name:str = 'Bart'


@dataclass
class Lisa(Player):
    name: str = 'Lisa'

    def generateRoshambo(self):
        values = ('rock', 'paper', 'scissors')
        self.value = random.choice(values)

def main():
    print('Welcome to RPS game!')
    print('+'*30)
    print()
    player = Player(input('Enter your name: '))
    player.generateRoshambo()
    bart = Bart()
    lisa = Lisa()
    choosing = input('Who would you like to play with? Lisa or Bart (l/b): ').lower()
    if choosing == 'l':
        cont = 'y'
        while cont == 'y':
            player.play(lisa)
            cont = input('Would you like to play again? (y/n): ').lower()
        player.endGame(lisa)
    elif choosing == 'b':
        cont= 'y'
        while cont == 'y':
            player.play(bart)
            cont = input('Would you like to play again? (y/n) ').lower()
        player.endGame(bart)
    else:
        print('Invalid choice')

if __name__ == '__main__':
    main()


