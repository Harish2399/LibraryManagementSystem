import os

BOOK_FILE = "books.txt"

if not os.path.exists(BOOK_FILE):
    open(BOOK_FILE, "w").close()

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(BOOK_FILE, "a") as f:
        f.write(f"{book_id},{book_name},{author}\n")

    print("Book Added Successfully!")

def view_books():
    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    if not books:
        print("No books available")
        return

    print("\nBOOK LIST")
    print("-" * 50)
    print("ID\tBook Name\tAuthor")
    print("-" * 50)

    for book in books:
        data = book.strip().split(",")
        print(f"{data[0]}\t{data[1]}\t{data[2]}")

def search_book():
    search_id = input("Enter Book ID: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    found = False

    for book in books:
        data = book.strip().split(",")

        if data[0] == search_id:
            print("\nBook Found")
            print("Book ID:", data[0])
            print("Book Name:", data[1])
            print("Author:", data[2])
            found = True

    if not found:
        print("Book Not Found")

def delete_book():
    delete_id = input("Enter Book ID to delete: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    with open(BOOK_FILE, "w") as f:
        for book in books:
            data = book.strip().split(",")

            if data[0] != delete_id:
                f.write(book)

    print("Book Deleted Successfully")

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        delete_book()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")