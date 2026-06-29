from tkinter import *

window = Tk()

window.title("Library Dashboard")

window.geometry("700x500")

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

def open_add_book():
    window.destroy()
    import add_book

Button(
    window,
    text="Add Book",
    width=20,
    height=2,
    command=open_add_book
).pack(pady=5)

def open_view_books():

    window.destroy()

    import view_books

Button(
    window,
    text="View Books",
    width=20,
    height=2,
    command=open_view_books
).pack(pady=5)

Button(window, text="Search Book", width=20, height=2).pack(pady=5)

Button(window, text="Update Book", width=20, height=2).pack(pady=5)

Button(window, text="Delete Book", width=20, height=2).pack(pady=5)

Button(window, text="Issue Book", width=20, height=2).pack(pady=5)

Button(window, text="Return Book", width=20, height=2).pack(pady=5)

Button(
    window,
    text="Exit",
    width=20,
    height=2,
    command=window.destroy
).pack(pady=10)

window.mainloop()