from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()

window.title("Search Book")
window.geometry("450x400")
window.resizable(False, False)

Label(
    window,
    text="SEARCH BOOK",
    font=("Arial",16,"bold")
).pack(pady=15)

Label(window,text="Enter Book ID").pack()

book_id = Entry(window,width=30)
book_id.pack()

result = Label(
    window,
    text="",
    font=("Arial",11),
    justify=LEFT
)

result.pack(pady=20)

def search():

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

        messagebox.showerror(
            "Error",
            "Book Not Found"
        )

Button(
    window,
    text="Search",
    width=20,
    command=search
).pack(pady=15)

window.mainloop()