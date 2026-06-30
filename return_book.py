from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess
import sys

# -----------------------------
# Back to Dashboard
# -----------------------------
def back():
    window.destroy()
    subprocess.Popen([sys.executable, "dashboard.py"])


# -----------------------------
# Search Book
# -----------------------------
def search_book():

    if book_id.get() == "":
        messagebox.showerror(
            "Error",
            "Please Enter Book ID"
        )
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
        messagebox.showerror(
            "Error",
            "Book Not Found"
        )


# -----------------------------
# Return Book
# -----------------------------
def return_book():

    if book_id.get() == "":
        messagebox.showerror(
            "Error",
            "Please Enter Book ID"
        )
        return

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT status FROM books WHERE book_id=?",
        (book_id.get(),)
    )

    row = cursor.fetchone()

    if row is None:

        messagebox.showerror(
            "Error",
            "Book Not Found"
        )
        connection.close()
        return

    if row[0] == "Available":

        messagebox.showerror(
            "Error",
            "Book is already Available"
        )
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


# -----------------------------
# Main Window
# -----------------------------
window = Tk()

window.title("Return Book")

window.geometry("500x480")

window.resizable(False, False)

Label(
    window,
    text="RETURN BOOK",
    font=("Arial",18,"bold")
).pack(pady=15)

Label(
    window,
    text="Book ID"
).pack()

book_id = Entry(
    window,
    width=30
)
book_id.pack()

result = Label(
    window,
    text="",
    justify=LEFT,
    font=("Arial",11)
)

result.pack(pady=20)

# -----------------------------
# Buttons
# -----------------------------
button_frame = Frame(window)
button_frame.pack(pady=10)

Button(
    button_frame,
    text="Search",
    width=15,
    command=search_book
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Return Book",
    width=15,
    command=return_book
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="⬅ Back",
    width=15,
    command=back
).grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()