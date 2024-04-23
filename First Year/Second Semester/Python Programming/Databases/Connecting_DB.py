import sqlite3

conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()

query = "SELECT * FROM Product where listPrice < 500 and categoryID = 1"

c.execute(query)

rows = c.fetchall()


conn.close()

print(type(rows))