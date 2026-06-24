import os

BOOK_FILE = os.path.join(os.path.dirname(__file__), "books.txt")

print("Using file:", os.path.abspath(BOOK_FILE))


if not os.path.exists(BOOK_FILE):
    open(BOOK_FILE, "w").close()
def add_book():
    book_id = input("Book ID: ")
    name = input("Book Name: ")
    author = input("Author: ")

    with open(BOOK_FILE, "a") as f:
        f.write(f"{book_id},{name},{author},Available,None\n")

    print("Book Added Successfully")

def view_books():
    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    if not books:
        print("No Books Found")
        return

    print("\nID | Name | Author | Status | Student")
    print("-" * 60)

    for book in books:
        if not book.strip():
           continue

        data = book.strip().split(",")

        if len(data) < 5:
           print("Invalid record:", book)
           continue

        print(f"{data[0]} | {data[1]} | {data[2]} | {data[3]} | {data[4]}")

def issue_book():
    book_id = input("Enter Book ID: ")
    student = input("Student Name: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    with open(BOOK_FILE, "w") as f:
        for book in books:
            data = book.strip().split(",")

            if data[0] == book_id:

                if data[3] == "Issued":
                    print("Book Already Issued")
                else:
                    data[3] = "Issued"
                    data[4] = student
                    print("Book Issued Successfully")

                book = ",".join(data) + "\n"

            f.write(book)

def return_book():
    book_id = input("Enter Book ID: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    with open(BOOK_FILE, "w") as f:
        for book in books:
            data = book.strip().split(",")

            if data[0] == book_id:
                data[3] = "Available"
                data[4] = "None"

                print("Book Returned Successfully")

                book = ",".join(data) + "\n"

            f.write(book)

def delete_book():
    book_id = input("Book ID to Delete: ")

    with open(BOOK_FILE, "r") as f:
        books = f.readlines()

    with open(BOOK_FILE, "w") as f:
        for book in books:
            data = book.strip().split(",")

            if data[0] != book_id:
                f.write(book)

    print("Book Deleted")

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")