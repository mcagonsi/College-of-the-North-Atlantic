from dataclasses import dataclass

import Q1_db_Func as db
import Q1_Business as br


# ALL THE REQUIRED OBJECTS ARE CREATED HERE


@dataclass
class Category:
    categoryID: int
    categoryName: str


@dataclass
class Product:
    productID: int
    categoryID: int
    productCode: str
    productName: str
    listPrice: float


@dataclass
class Categories:
    categories = []

    def showCategories(self):

        for category in self.categories:
            print(category.categoryName, end=' | ')
        print()

    def __post_init__(self):
        Categories = db.getCategories()
        for category in Categories:
            self.categories.append(Category(category[0], category[1]))


@dataclass
class Products:
    def __int__(self):
        self.products = []

    def view(self, categoryName):
        self.products = []
        validCategories = Categories().categories
        for Category in validCategories:
            if Category.categoryName == categoryName.title():
                categoryID = Category.categoryID

        productsByCategory = db.viewCategory(categoryID)
        for item in productsByCategory:
            self.products.append(Product(item[1], item[1], item[2], item[3], item[4]))

        print('{:<20} {:<50} {:>6}'.format('Code', 'Name', 'Price'))
        print('-' * 80)
        if len(productsByCategory) > 0:
            for product in self.products:
                print('{:<20} {:<50} {:>6}'.format(product.productCode, product.productName, product.listPrice))

    def update(self):
        productCode, productPrice = br.validateUpdate()
        print(productCode, productPrice)
        db.updateProduct(productCode, productPrice)
        print('Product Updated')
