from dataclasses import dataclass

@dataclass
class Product:
    """
    A class representing a
    """
    name: str
    price: float
    discountPercent: int

    def getDiscountAmount(self):
        """
        Returns the
        :return:
        """
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        """

        :return:
        """
        return self.price - self.getDiscountAmount()
