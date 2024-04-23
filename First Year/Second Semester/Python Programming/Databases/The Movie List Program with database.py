import sqlite3 as sql
from dataclasses import dataclass
DATASOURCE ='Movies.sqlite'

@dataclass
class Movie:
    ID:int
    Name:str
    Year:int
    Mins:int
    Category:str

def create_database():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    m.execute("CREATE TABLE IF NOT EXISTS Movies (ID integer primary key, Name varchar(50),Year integer , Mins integer , Category varchar(20));")
    movies.close()

def read_db():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()

    m.execute("SELECT * FROM Movies")

    moviesList = m.fetchall()

    movies.close()
    return moviesList

def insert_db(Movie):
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    # "INSERT INTO table VALUES (?, ?, ?)", (var1, var2, var3)
    # query = "INSERT INTO Movies VALUES (?,?,?,?,?)",(Movie.ID,Movie.Name,Movie.Year,Movie.Mins,Movie.Category)
    m.execute("INSERT INTO Movies VALUES (?,?,?,?,?)",(Movie.ID,Movie.Name,Movie.Year,Movie.Mins,Movie.Category))
    movies.commit()
    movies.close()

def readCategories():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    query = "SELECT Category FROM Movies;"
    m.execute(query)
    categories = m.fetchall()
    movies.close()

    return categories
def showCategories():
    categories = ('Animation','Comedy','Documentary','History','Music','Sci-Fi')

    print('CATEGORIES')
    for i, category in enumerate(categories,start=1):
        print(f'{i}. {category}')

def cat():
    categories = ('Animation','Comedy','Documentary','History','Music','Sci-Fi') #readCategories()
    i = int(input('Category ID: '))
    category = categories[i-1]

    movies = sql.connect(DATASOURCE)
    m = movies.cursor()
    m.execute("SELECT * FROM Movies WHERE Category = ?",(category,))
    M_C = m.fetchall()
    movies.close()


    print()
    print('MOVIES - {}'.format(category.upper()))
    print('{:<4} {:25} {:<4} {:<4} {:15}'.format('ID', 'Name', 'Year', 'Mins', 'Category'))
    print('-'*70)
    for movie in M_C:
        print('{:<4} {:25} {:<4} {:<4} {:15}'.format(movie[0], movie[1], movie[2], movie[3],movie[4]))

def showByYear():
    movies = sql.connect(DATASOURCE)
    m = movies.cursor()

    m.execute("SELECT * FROM Movies ORDER BY Year DESC ;")

    moviesList = m.fetchall()

    movies.close()
    print()
    print('MOVIES - {}'.format('BY YEAR'))
    print('{:<4} {:25} {:<4} {:<4} {:15}'.format('ID', 'Name', 'Year', 'Mins', 'Category'))
    print('-' * 70)
    for movie in moviesList:
        print('{:<4} {:25} {:<4} {:<4} {:15}'.format(movie[0], movie[1], movie[2], movie[3], movie[4]))
    print()

def add ():
    movies = read_db()
    i = len(movies) + 1

    categories = ('Animation','Comedy','Documentary','History','Music','Sci-Fi') #readCategories()

    movie = Movie(i,input('Name: '), int(input('Year: ')), int(input('Minutes: ')), categories[int(input('Category:')) - 1] )
    insert_db(movie)
    print(f"{movie.Name} was added to database")
    print()

def delete_db():
    movieToDelete = int(input('Enter the ID to delete: '))
    movies = sql.connect(DATASOURCE)
    mo = movies.cursor()
    m = movies.cursor()
    mo.execute("SELECT Name FROM Movies WHERE ID = ?;",(movieToDelete,))
    m.execute("DELETE FROM Movies WHERE ID = ?;",(movieToDelete,))
    movi = mo.fetchall()
    movies.commit()
    movies.close()
    print(f"{movi[0][0]} was deleted from database")
    print()

def title():
    print('The Movie List Program')
    print()
def menu():
    print('COMMAND MENU')
    print('cat - View movies by category')
    print('year - View movies by year')
    print('add - Add movie')
    print('del - Delete movie')
    print('exit - Exit program')
    print()

def main():
    create_database()
    title()
    menu()
    while True:
        showCategories()
        print()
        option = input('Command: ').lower()
        if option == 'cat':
            cat()
        elif option == 'year':
            showByYear()
        elif option == 'add':
            add()
        elif option == 'del':
            delete_db()
        elif option == 'exit':
            print('Thanks for using this program')
            print('Bye!')
            break
        else:
            print('Invalid Command!')
            print()

if __name__ == '__main__':
    main()

