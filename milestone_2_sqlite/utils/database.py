import sqlite3

"""
concerened with storing and retrieving books from a sqlite database.

"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * from books")
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()
    return books


def add_book(name, author):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books VALUES(?,?,0)", (name, author))

    connection.commit()
    connection.close()


def mark_book_as_read(book_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE books SET read=1 WHERE name=?", (book_name,))

    connection.commit()
    connection.close()    
    

def delete_book(book_name):
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE name=?", (book_name))

    connection.commit()
    connection.close()    
