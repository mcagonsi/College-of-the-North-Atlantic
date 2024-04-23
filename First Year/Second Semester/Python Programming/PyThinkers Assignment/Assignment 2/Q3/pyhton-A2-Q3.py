class Animal:
    def __init__(self, name='', species=''):
        # Initialize the attributes of the Animal class
        self.name = name
        self.species = species

    def speak(self):
        # Abstract method for speaking, to be implemented by subclasses
        pass


class Dog(Animal):
    def __init__(self, name='', species='', breed=''):
        # Initialize attributes specific to Dog class and call the parent class constructor
        super().__init__(name, species)
        self.breed = breed

    def speak(self):
        # Implement the speak method for Dog class
        print("Woof!")


class Cat(Animal):
    def __init__(self, name='', species='', color=''):
        # Initialize attributes specific to Cat class and call the parent class constructor
        super().__init__(name, species)
        self.color = color

    def speak(self):
        # Implement the speak method for Cat class
        print("Meow!")


# Sample usage
dog = Dog("Max", "Dog", "Golden Retriever")
cat = Cat("Whiskers", "Cat", "Orange")

print("Dog:")
print("Name:", dog.name)
print("Species:", dog.species)
print("Breed:", dog.breed)
print("Sound:", end=" ")
dog.speak()
print()

print("Cat:")
print("Name:", cat.name)
print("Species:", cat.species)
print("Color:", cat.color)
print("Sound:", end=" ")
cat.speak()