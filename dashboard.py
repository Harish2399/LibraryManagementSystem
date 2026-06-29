from tkinter import *

# ------------------------
# Functions
# ------------------------

def open_add_book():
    window.destroy()
    import add_book


def open_view_books():
    window.destroy()
    import view_books


def open_search_book():
    window.destroy()
    import search_book


def open_update_book():
    window.destroy()
    import update_book


def open_delete_book():
    window.destroy()
    import delete_book


# ------------------------
# Main Window
# ------------------------

window = Tk()

window.title("Library Dashboard")
window.geometry("700x600")
window.resizable(False, False)

title = Label(
    window,
    text="LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold")
)
title.pack(pady=20)

welcome = Label(
    window,
    text="Welcome Admin",
    font=("Arial", 14)
)
welcome.pack(pady=10)

# ------------------------
# Buttons
# ------------------------

Button(
    window,
    text="Add Book",
    width=25,
    height=2,
    command=open_add_book
).pack(pady=5)

Button(
    window,
    text="View Books",
    width=25,
    height=2,
    command=open_view_books
).pack(pady=5)

Button(
    window,
    text="Search Book",
    width=25,
    height=2,
    command=open_search_book
).pack(pady=5)

Button(
    window,
    text="Update Book",
    width=25,
    height=2,
    command=open_update_book
).pack(pady=5)

Button(
    window,
    text="Delete Book",
    width=25,
    height=2,
    command=open_delete_book
).pack(pady=5)

# These buttons will be connected in Lesson 8

Button(
    window,
    text="Issue Book",
    width=25,
    height=2
).pack(pady=5)

Button(
    window,
    text="Return Book",
    width=25,
    height=2
).pack(pady=5)

Button(
    window,
    text="Exit",
    width=25,
    height=2,
    command=window.destroy
).pack(pady=15)

window.mainloop()