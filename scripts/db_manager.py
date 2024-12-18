import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db', 'book_collection.db')

# DB_PATH = 'db/book_collection.db'

def connect():
    """Establish connection to the database."""
    return sqlite3.connect(DB_PATH)

def initialize_db():
    """Create books table if it doesn't exist."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            publication_year INTEGER,
            isbn TEXT,
            rating REAL,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title, author, genre, publication_year, isbn, rating, status):
    """Add a new book to the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, author, genre, publication_year, isbn, rating, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (title, author, genre, publication_year, isbn, rating, status))
    conn.commit()
    conn.close()

def list_books():
    """Retrieve and return all books in the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    return books

def search_books(term):
    """
    Search for books by title or author.
    :param term: A string to match against book titles or authors.
    :return: A list of books that match the search term.
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
    ''', (f'%{term}%', f'%{term}%'))
    books = cursor.fetchall()
    conn.close()
    return books

def delete_book(book_id):
    """
    Delete a book by its ID.
    :param book_id: The ID of the book to be deleted.
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()
