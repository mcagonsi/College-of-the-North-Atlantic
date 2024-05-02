from sqlalchemy.dialects import mysql

mydb = mysql.connect(
    host="bankdb@localhost",
    user="root",
    passwd="root",
    database = 'bankdb'
)