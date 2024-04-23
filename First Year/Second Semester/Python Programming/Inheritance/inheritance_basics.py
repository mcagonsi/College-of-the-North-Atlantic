from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discountPercent: int = 0

    def getDiscountAmount(self) -> float:
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self) -> float:
        return self.price - self.getDiscountAmount()

    def getDescription(self) -> str:
        return self.name

    def __str__(self):
        return self.name + " is actually Thor's Hammer."

    def __eq__(self, other):
        return self.name == other.name


# @dataclass
# class Book(Product):
#     author: str = ''
#
#     def getDescription(self) -> str:
#         return f"{Product.getDescription(self)} by {self.author}"

class Book(Product):
    def __init__(self, name='', price=0.0, discountPercent=0, author=''):
        Product.__init__(self, name, price, discountPercent)

        self.author = author

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} by {self.author}"

product1 = Product('Quartet Marker', 2.99, 20)
book1 = Book('The Shining', 12.00, 10, 'Stephen King')


@dataclass
class Movie(Product):
    year: int = 0

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)}  {self.year}"


# print(product1.getDescription())
# print(product1.getDiscountPrice())
# print(book1.getDescription())
# print(book1.getDiscountPrice())
#
# movie1 = Movie('Venom', 12.00, 5, 2013)
# print(movie1.getDescription())
# print(movie1.getDiscountPrice())
#
# print(isinstance(movie1, Movie))
# print(isinstance(movie1, Product))
# print(isinstance(movie1, Book))