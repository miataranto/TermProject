# TermProject.py
"""
Term Project: BookBuddy
Author: Mia Taranto
Instructor: Kim Hosung
Date: August 2025
Course: IT215
"""


import json
import os

DATA_FILE = "books.json"
book_list = []

def load_books():
    """Load books from the JSON file if it exists, otherwise return an empty list."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # If the file exists but is corrupted or empty
    else:
        return []  # If the file doesn't exist


def save_books():
    """Save the current book list to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(book_list, f, indent=4)

def add_book():
    """Prompt the user for book details and add the book to the list with status 'Unread'.""" 
    title = input("Enter book title: ")
    author = input("Enter author: ")
    genre = input("Enter genre: ")
    status = "Unread"
    book = {"title": title, "author": author, "genre": genre, "status": status}
    book_list.append(book)
    print(f"✅ '{title}' added to your list!")
    save_books()

def view_books():
    """Display all books in the current list with their title, author, genre, and status."""
    if not book_list:
        print("No books in your list yet.")
        return
    print("\n📖 Your Book List:")
    for i, book in enumerate(book_list, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['genre']}) - {book['status']}")

def mark_as_read():
    """Allow the user to mark a selected book as 'Read' based on its list number."""
    view_books()
    if not book_list:
        return
    try:
        index = int(input("Enter the number of the book you've read: ")) - 1
        if 0 <= index < len(book_list):
            book_list[index]["status"] = "Read"
            print(f"📘 Marked '{book_list[index]['title']}' as read.")
            save_books()
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Run the main loop for the BookBuddy CLI, handling user input and menu navigation."""
    global book_list
    book_list = load_books()

    while True:
        print("\n📚 Welcome to BookBuddy")
        print("1. Add a book")
        print("2. View all books")
        print("3. Mark a book as read")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            mark_as_read()
        elif choice == "4":
            print("Books saved. Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")