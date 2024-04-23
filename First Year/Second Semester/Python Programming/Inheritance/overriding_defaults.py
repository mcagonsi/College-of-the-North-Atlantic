# from inheritance_basics import Product
#
# product1 = Product("Stanley 13 Ounce Wood Hammer", 5.489, 10)
# print(str(product1))
# print()
# # print(dir(product1))
#
# product2 = Product("Stanley 13 Ounce Wood Hammer", 6.00, 20)
#
# print(product1 == product2)

from Dice_Roller_Classes import Die, Dice

dice = Dice()
dice.addDie(Die(6))
dice.addDie(Die(3))
dice.addDie(Die(2))

for obj in dice:
    # die.roll()
    print(obj)

# from Subclasses import CustomRequestError
#
# def read_movies():
#     try:
#         movies = []
#         with open('movies.csv') as file_movies:
#             pass
#     except FileNotFoundError:
#         raise CustomRequestError('This is my error')
#     except Exception:
#         raise CustomRequestError('This is a generic error')
#
#
#
# try:
#     movies = read_movies()
# except CustomRequestError as e:
#     print("CustomRequestError:", e)

