from Classes_Constructor import Product

# Creating the products
product1 = Product("Stanley Hammer", 9.99, 5)
product2 = Product("Quartet Marker", 2.00, 4)

print("Product Data")
print(f"Product Name:\t\t {product1.name}")
print(f"Product Price:\t\t {product1.price:.2f}")
print(f"Discount Percent:\t {product1.discount_percent:d}%")

print(f"Discount Amount:\t {product1.getDiscountAmount():.2f}")
print(f"Discount Price:\t\t {product1.getDiscountPrice():.2f}")
