from dataclasses import dataclass
import random


@dataclass
class Die:
    __value: int = 1

    def getValue(self):
        return self.__value

    def roll(self):
        self.__value = random.randint(1, 6)

die2 = Die()
die2.__value = 10
print("Die value: ", die2.__value, die2.getValue())