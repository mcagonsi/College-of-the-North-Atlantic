from Inheritance_isinstance_objects import Product, Book, Movie


def get_products():
    return (Product("Stanley 13 Ounce Wood Hammer", 5.489, 10),
            Movie("The Holy Grail - DVD", 5.3, 10))


def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}} {product.name}")
    if isinstance(product, Book):
        print(f"{'Author':{w}} {product.author}")
    elif isinstance(product, Movie):
        print(f"{'Year':{w}} {product.year}")
    print(f"{'Discount price:':{w}} {product.getDiscountPrice():.2f}")
    print()


def main():
    test_products = get_products()
    for item in test_products:
        show_product(item)


if __name__ == "__main__":
    main()