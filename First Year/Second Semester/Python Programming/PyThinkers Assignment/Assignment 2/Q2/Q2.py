import random


class RandomIntList(list):  # creates the RandomIntList Class
    def __init__(self, length: int) -> None:  # overwrites the default initialization for the List super class
        for i in range(length):  # takes an argument 'length' to specify the number of integers
            self.append(random.randint(1, 100))

    def __str__(self):  # overwrites the default _str_ representation
        container = []
        for i in self:
            container.append(str(i))
        return ', '.join(container)

    @property
    def count(self):
        return len(self)  # returns the count value for the initialized class

    @property
    def average(self):
        return f'{sum(self) / len(self):.3f}'  # returns the average value for the integers in the list

    @property
    def total(self):
        return sum(self)  # returns the total(summation) value of all the integers in the list


def title() -> None:
    print('Random Integer List')
    print()


def main():
    title()

    while True:
        try:  # handles errors to make sure the user inputs valid data
            num = int(input('How many random integers should the list contain?: '))
            again = 'y'
            while again == 'y':  # conditions the loop
                print()
                print('Random Integers')
                print('=' * 15)
                int_list = RandomIntList(num)
                print(f"{'Integers:':10} {int_list}")
                print(f"{'Count':10} {int_list.count}")
                print(f"{'Total:':10} {int_list.total}")
                print(f"{'Average:':10} {int_list.average}")
                print()
                while True:
                    again = input('Continue? (y/n): ').lower()
                    if again == 'y':
                        break
                    elif again == 'n':
                        break
                    else:
                        print('Invalid choice input!')
                print()
            print('Bye!')
            break
        except ValueError:
            print('Invalid Input!')


if __name__ == '__main__':
    main()
