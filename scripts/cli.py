# from scripts.db_manager import initialize_db, add_book, list_books, search_books, delete_book
from db_manager import initialize_db, add_book, list_books, search_books, delete_book

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def main():
    initialize_db()
    while True:
        print()
        print("Welcome to Sen's Book Collection Manager")
        print("1. Add a Book")
        print("2. List All Books")
        print("3. Search for a Book")
        print("4. Delete a Book")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            publication_year = input("Publication Year: ")
            isbn = input("ISBN: ")
            rating = float(input("Rating (1-5): "))
            status = input("Status (Read/Unread): ")
            add_book(title, author, genre, publication_year, isbn, rating, status)
        elif choice == "2":
            list_all_books()
        elif choice == "3":
            search_for_book()
        elif choice == "4":
            delete_a_book()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again!")

def list_all_books():
    books = list_books()
    if books:
        print("\nYour Book Collection:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}, Rating: {book[6]}, Status: {book[7]}")
    else:
        print("\nNo books found in your collection.")

def search_for_book():
    term = input("Enter a search term (title or author): ")
    results = search_books(term)
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}, Year: {book[4]}, Rating: {book[6]}, Status: {book[7]}")
    else:
        print("\nNo books matched your search.")

def delete_a_book():
    book_id = input("Enter the ID of the book to delete: ")
    try:
        book_id = int(book_id)
        delete_book(book_id)
        print(f"Book with ID {book_id} has been deleted.")
    except ValueError:
        print("Invalid ID. Please enter a valid number.")


if __name__ == "__main__":
    main()
