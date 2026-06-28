from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("Add Book")

window.geometry("450x350")

window.resizable(False, False)

Label(
    window,
    text="ADD NEW BOOK",
    font=("Arial",16,"bold")
).pack(pady=15)

Label(window,text="Book ID").pack()

book_id = Entry(window,width=30)
book_id.pack()

Label(window,text="Book Name").pack()

book_name = Entry(window,width=30)
book_name.pack()

Label(window,text="Author").pack()

author = Entry(window,width=30)
author.pack()


def save_book():

    connection = sqlite3.connect("library.db")

    cursor = connection.cursor()

    try:

        cursor.execute(

            """
            INSERT INTO books
            VALUES(?,?,?,?,?)
            """,

            (
                book_id.get(),
                book_name.get(),
                author.get(),
                "Available",
                "None"
            )

        )

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Book Added Successfully"
        )

        book_id.delete(0,END)
        book_name.delete(0,END)
        author.delete(0,END)

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Book ID Already Exists"
        )

    connection.close()


Button(
    window,
    text="Save Book",
    width=20,
    command=save_book
).pack(pady=25)

window.mainloop()