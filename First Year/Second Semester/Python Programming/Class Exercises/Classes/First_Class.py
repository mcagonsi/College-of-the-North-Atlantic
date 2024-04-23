from dataclasses import dataclass

@dataclass
class Product:
    name: str = ""
    price: float = 0.0
    discount_percent: float = 0.0

    def get_discount_amount(self) -> float:
        return self.price * self.discount_percent / 100

    def get_discount_price(self) -> float:
        return self.price * self.get_discount_amount()