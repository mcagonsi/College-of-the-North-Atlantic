from dataclasses import dataclass,field

@dataclass
class Player:
    firstName:str =''
    lastName:str = ''
    pos:str = ''
    atbat:int = ''
    hit:int = ''

    @property
    def avg(self):
        return float(self.hit) / float(self.atbat)

    @property
    def name(self):
        return self.firstName + ' ' + self.lastName



@dataclass
class Lineup:
    team:list

    def __iter__(self):
        for player in self.team:
            yield player


    def addPlayer(self):
        firstName = input('First Name: ')
        lastName = input('Last Name: ')
        pos = input('Position: ')
        atbat = int(input('Atbat: '))
        hit = int(input('Hits: '))
        player = Player(firstName,lastName,pos,atbat,hit)
        self.team.append(player)
        print(f'{firstName} in position {pos} has been added to the lineup')

    def removePlayer(self):
        player = int(input('Player to remove: ')) - 1
        self.team.pop(player)

    def movePlayer(self):
        selected_player = int(input('Player to move: ')) - 1
        player = self.team.pop(selected_player)
        newPosition = int(input('New Position: ')) - 1
        self.team.insert(newPosition,player)

        print(f'{player.firstName} was moved !')

    def editPlayerPosition(self):
        selected_player = int(input('Select Player: ')) - 1
        player = self.team[selected_player]
        player.pos = input('New Position: ')
        print(f'{player.firstName} position has been updated!')

    def editPlayerStats(self):
        selected_player = int(input('Select Player')) - 1
        player = self.team[selected_player]
        player.atbat = int(input('AtBat: '))
        player.hit = int(input('Hits: '))
        print('Player Stats have been updated !')


def title():
    from datetime import date
    print('='*70)
    print('Baseball Team Manager'.center(100))
    print()
    print(date.today())
def menu():
    print('MENU OPTIONS')
    print('1. Display all players')
    print('2. Add a player')
    print('3. Remove a player')
    print('4. Move the player')
    print('5. Edit player position')
    print('6. Edit player stats')
    print('7. Exit')
    print()

def positions():
    return ('C','1B','2B','3B','SS','LF','RF','P')

def main():
    lineup = Lineup([])
    title()
    menu()
    for pos in positions():
        print(pos, end=', ')
    print()
    print('='*70)
    while True:
        option = int(input('Menu Option: '))
        if option == 1:
            print(f"  {'Player':25} {'POS':5} {'AB':>6} {'H':>6} {'AVG':>6}")
            print('-' * 70)
            for i, player in enumerate(lineup,start =1):
                print(f"{i}.  {player.name:25} {player.pos:5} {player.atbat:>6} {player.hit:>6} {player.avg:>6.3f}")

        elif option == 2:
            lineup.addPlayer()

        elif option == 3:
            lineup.removePlayer()

        elif option == 4:
            lineup.movePlayer()

        elif option ==5:
            lineup.editPlayerPosition()

        elif option == 6:
            lineup.editPlayerPosition()

        elif option == 7:
            print('Bye !')
            break
        else:
            print('Invalid Option')


if __name__ == '__main__':
    main()




