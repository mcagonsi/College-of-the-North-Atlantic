from dataclasses import dataclass

@dataclass
class Product:
    name:str = ''
    price:float = 0.0
    discount:int = 0

    def getdiscountamount(self):
        return self.price * self.discount/100

    def getdiscountprice(self):
        return self.price - self.getdiscountamount()

    def getdescription(self):
        return self.name

@dataclass
class Book(Product):
    author:str=''

    def getbook(self):
        print(f'Title: {Product.getdescription(self)}')
        print(f'Discount Price: {Product.getdiscountprice(self)}')
        print(f'Author: {self.author}')

@dataclass
class Movie(Product):
    year:int=0

    def getmovie(self):
        print (f'Movie title: {Product.getdescription(self)}\nYear: {self.year}\nDiscount Price: {self.getdiscountprice()}')


def main():
    movie =Movie('The Holy Grail - DVD',4.80,0,1975)
    book = Book('Time Relativity',20.99,2,'Albert Einstein')
    product = Product('Stanley 13 Ounce Wood Hammer',4.94,0)
    items = [movie,book,product]


    for item in items:
        print('PRODUCT DATA')
        if isinstance(item,Book):
            item.getbook()
        elif isinstance(item,Movie):
            item.getmovie()
        elif isinstance(item,Product):
            print(f'Name: {item.getdescription()}')
            print(f'Discount Price: {item.getdiscountprice()}')
        print()


main()