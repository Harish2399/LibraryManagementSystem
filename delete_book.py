from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("Delete Book")

window.geometry("500x450")

window.resizable(False, False)

Label(
    window,
    text="DELETE BOOK",
    font=("Arial",18,"bold")
).pack(pady=15)

Label(window,text="Book ID").pack()

book_id = Entry(window,width=30)
book_id.pack()

result = Label(
    window,
    text="",
    font=("Arial",11),
    justify=LEFT
)

result.pack(pady=20)


def search_book():

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
            text=
            f"Book Name : {row[1]}\n\n"
            f"Author : {row[2]}\n\n"
            f"Status : {row[3]}\n\n"
            f"Student : {row[4]}"
        )

    else:

        result.config(text="")

        messagebox.showerror(
            "Error",
            "Book Not Found"
        )


def delete_book():

    if book_id.get()=="":

        messagebox.showerror(
            "Error",
            "Enter Book ID"
        )

        return

    answer = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to delete this book?"
    )

    if answer:

        connection = sqlite3.connect("library.db")

        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM books WHERE book_id=?",
            (book_id.get(),)
        )

        connection.commit()

        if cursor.rowcount > 0:

            messagebox.showinfo(
                "Success",
                "Book Deleted Successfully"
            )

            result.config(text="")

            book_id.delete(0,END)

        else:

            messagebox.showerror(
                "Error",
                "Book Not Found"
            )

        connection.close()


Button(
    window,
    text="Search",
    width=20,
    command=search_book
).pack(pady=5)

Button(
    window,
    text="Delete",
    width=20,
    command=delete_book
).pack(pady=10)

window.mainloop()