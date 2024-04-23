from dataclasses import dataclass

@dataclass
class Player:
    ID:int = 1
    fName:str = ''
    lName:str = ''
    pos:str = ''
    atBats:int = 0
    hits:int = 0

    @property
    def avg(self):
        return (self.hits / self.atBats)
