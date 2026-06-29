from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("Return Book")
window.geometry("500x450")
window.resizable(False, False)

Label(window, text="RETURN BOOK", font=("Arial",18,"bold")).pack(pady=15)

Label(window, text="Book ID").pack()

book_id = Entry(window, width=30)
book_id.pack()

result = Label(window, text="", justify=LEFT, font=("Arial",11))
result.pack(pady=20)


def search_book():

    if book_id.get() == "":
        messagebox.showerror("Error","Enter Book ID")
        return

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE book_id=?",
        (book_id.get(),)
    )

    row = cursor.fetchone()

    connection.close()

    if row:

        result.config(
            text=f"""
Book Name : {row[1]}

Author : {row[2]}

Status : {row[3]}

Student : {row[4]}
"""
        )

    else:

        result.config(text="")
        messagebox.showerror("Error","Book Not Found")


def return_book():

    if book_id.get() == "":
        messagebox.showerror("Error","Enter Book ID")
        return

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT status FROM books WHERE book_id=?",
        (book_id.get(),)
    )

    row = cursor.fetchone()

    if row is None:

        messagebox.showerror("Error","Book Not Found")
        connection.close()
        return

    if row[0] == "Available":

        messagebox.showerror("Error","Book is already Available")
        connection.close()
        return

    cursor.execute(
        """
        UPDATE books
        SET status=?, student=?
        WHERE book_id=?
        """,
        (
            "Available",
            "None",
            book_id.get()
        )
    )

    connection.commit()
    connection.close()

    messagebox.showinfo(
        "Success",
        "Book Returned Successfully"
    )

    result.config(text="")
    book_id.delete(0, END)


Button(
    window,
    text="Search",
    width=20,
    command=search_book
).pack(pady=5)

Button(
    window,
    text="Return Book",
    width=20,
    command=return_book
).pack(pady=10)

window.mainloop()