import sqlite3

conn = sqlite3.connect('guitar_shop.sqlite')
c = conn.cursor()


# CONTAINS ALL THE DATABASE FUNCTIONS FOR VIEW AND WRITING INTO DATABASE
def getCategories():
    query = 'select * from Category;'

    c.execute(query)
    categories = c.fetchall()

    return categories


def viewCategory(category):
    query = 'select * from Product where categoryID = ? order by productName;'
    c.execute(query, (category,))
    products = c.fetchall()

    return products


def updateProduct(code, price):
    query = 'update Product set listPrice = ? where productCode = ?;'
    c.execute(query, (price, code))
    conn.commit()


def checkProductCode(productCode):
    query = 'select productCode from Product where productCode = ?;'
    c.execute(query, (productCode,))
    return c.fetchone()[0]
