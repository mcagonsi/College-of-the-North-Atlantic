class Rectangle:
    # initializes and creates the rectangle object
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

        # calculates and returns the perimeter

    def perimeter(self):
        return 2 * (self.height + self.width)

    # calculates and returns the area
    def area(self):
        return self.height * self.width

    # shows the diagrammatic representation of the shape

    def draw_box(self):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 or i == self.height - 1 or j == 0 or j == self.width - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


def main():

    # introduces the program
    print('Rectangle Calculator')


    cont = 'y'
    # starts the loop for the program
    while cont.lower() == 'y':
        while True:
            try:
                # takes inputs and handles errors upon entry
                height = int(input(f"\n{'Height:':15} "))
                width = int(input(f"{'Width:':15} "))
                rect = Rectangle(height, width)
                print(f"{'Perimeter:':15} {rect.perimeter():.0f}")
                print(f"{'Area:':15} {rect.area():.0f} ")
                rect.draw_box()
                break
            except ValueError:  # throws the exception error response
                print('Please enter an integer!')
            except Exception:
                print('An unexpected error occurred!')

        cont = input('\nContinue ? (y/n): ').lower()
    print()
    print('Bye!')# exits the code or program


if __name__ == '__main__':
    main()
