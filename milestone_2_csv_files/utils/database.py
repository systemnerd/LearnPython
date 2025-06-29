"""
concerened with storing and retrieving books from a csv file.
Format of the csv file:

name#author#read\n
name#author#read\n
name#author#read\n

"""

books_file = "books.txt"

def create_book_table():
    with open(books_file, "w"):
        pass # just to make sure file exists

def add_book(name, author):
    with open("books.txt", "a") as file:
        file.write(f"{name},{author},0\n")


def get_all_books():
    with open(books_file, "r") as file:
        lines = [ # [[name, author, read], [name, author, read]]
            line.strip().split(",")
            for line in file.readlines()
        ]
        return [
            {'name': line[0], 'author': line[1], 'read':line[2]}
            for line in lines
        ]


def mark_book_as_read(book_name):
    books = get_all_books()

    for book in books:
        if book['name'] == book_name:
            book['read'] = '1'
    
    _save_all_books(books)
    
def _save_all_books(books):
    with open(books_file, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")

def delete_book(book_name):
    books = get_all_books()

    books = [
        book for book in books if book['name'] != book_name
    ]

    _save_all_books(books)
