import os

BOOK_FILE = "books.txt"

if not os.path.exists(BOOK_FILE):
    open(BOOK_FILE, "w").close()

def add_book():
    book = input("Enter book name: ")
    with open(BOOK_FILE, "a") as f:
        f.write(book + "\n")
    print("Book added successfully!")

def view_books():
    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    if len(books) == 0:
        print("No books available.")
    else:
        print("\nAvailable Books:")
        for i, book in enumerate(books, start=1):
            print(f"{i}. {book.strip()}")

def search_book():
    name = input("Enter book name to search: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    found = False

    for book in books:
        if name.lower() in book.lower():
            print("Book Found:", book.strip())
            found = True

    if not found:
        print("Book not found.")

def delete_book():
    name = input("Enter book name to delete: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    with open(BOOK_FILE, "w") as f:
        for book in books:
            if book.strip().lower() != name.lower():
                f.write(book)

    print("Book deleted if it existed.")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")