import Q1_Objects as obj
import Q1_db_Func as db


def title():
    print("Product Manager")
    print()


def showCategories():
    print('CATEGORIES')
    categories = obj.Categories()
    categories.showCategories()
    print()


def menu():
    print('COMMAND MENU')
    print('view - View products by category')
    print('update - Update product price')
    print('Exit - Exit program')
    print()


def main():
    title()
    showCategories()
    menu()
    products = obj.Products()
    while True:
        print()
        option = input('Command: ').lower()
        print()
        if option == 'view':
            category = input('Category name: ')
            products.view(category)
        elif option == 'update':
            products.update()
        elif option == 'exit':
            print('Bye')
            db.conn.close()
            print()
            break
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
