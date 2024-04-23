from dataclasses import dataclass

@dataclass
class Product:
    name: str = ''
    __price: float = 0.0
    discountPercent: int = 0

    def __post_init__(self):
        self.price = self.__price

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def product_price(self, price):
        if price <= 0:
            raise ValueError("Price cannot be less that 0")
        else:
            self.__price = price

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountPercent(self):
        return self.price - self.getDiscountAmount()
