from .database_connection import DatabaseConnection

"""
concerened with storing and retrieving books from a sqlite database.

"""


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT * from books")
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def add_book(name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO books VALUES(?,?,0)", (name, author))


def mark_book_as_read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("UPDATE books SET read=1 WHERE name=?", (book_name,))


def delete_book(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM books WHERE name=?", (book_name,))
