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


@dataclass
class Book(Product):
    author: str = ''

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} by {self.author}"


@dataclass
class Movie(Product):
    year: int = 0

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)}  {self.year}"