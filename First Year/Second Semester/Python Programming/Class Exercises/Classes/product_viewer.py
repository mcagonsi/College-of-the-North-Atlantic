from product_class_encapsulation import Product


def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.name}")
    print()


def show_individual_product(product):
    width = 18
    print(f"{'Name:':{width}} {product.name}")
    print(f"{'Price:':{width}} {product.product_price:.2f}")
    print(f"{'Discount percent:':{width}} {product.discountPercent:d}%")
    print(f"{'Discount amount:':{width}} {product.getDiscountAmount():.2f}")
    print(f"{'Discount price':{width}} {product.getDiscountPercent():.2f}")
    print()


def get_products():
    return (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
            Product('National Hardware 3/4" Wire Nails', 2.01, 0),
            Product('Economy Duct Tape, 60 yds, Silver', 5.99, 2))


def get_individual_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                print("Invalid product. Please look at your screen and try again.")
            else:
                return products[number-1]
        except ValueError:
            print("Invalid number, Please try again")
        print()


def main():
    print("The Product Viewer program\n")

    products = get_products()
    show_products(products)

    choice = 'y'
    while choice.lower() == 'y':
        product = get_individual_product(products)
        show_individual_product(product)

        choice = input("View another product? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()