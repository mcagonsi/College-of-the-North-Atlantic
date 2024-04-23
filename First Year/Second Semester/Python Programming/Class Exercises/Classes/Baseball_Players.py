from dataclasses import dataclass


@dataclass
class Player:
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'

    @property
    def battingAvg(self) -> float:
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0


def main():
    player1 = Player('Arun', 'Rameshbabu', 'S', 10, 10)
    print(f'Player: {player1.fullName}')
    print(f'Batting average: {player1.battingAvg}')
    print('Test complete')


if __name__ == '__main__':
    main()
