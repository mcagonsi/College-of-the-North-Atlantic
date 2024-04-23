# Importing the module
import sqlite3

# Connecting to a database file
conn = sqlite3.connect('guitar_shop.sqlite')

c = conn.cursor()
query = "SELECT * FROM Product"
c.execute(query)
rows = c.fetchall()
conn.close()

for row in rows:
    print(row)