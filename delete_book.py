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


# -----------------------------
# Delete Book
# -----------------------------
def delete_book():

    if book_id.get() == "":
        messagebox.showerror(
            "Error",
            "Please Enter Book ID"
        )
        return

    answer = messagebox.askyesno(
        "Confirm Delete",
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
            book_id.delete(0, END)

        else:

            messagebox.showerror(
                "Error",
                "Book Not Found"
            )

        connection.close()


# -----------------------------
# Main Window
# -----------------------------
window = Tk()

window.title("Delete Book")

window.geometry("500x450")

window.resizable(False, False)

Label(
    window,
    text="DELETE BOOK",
    font=("Arial",18,"bold")
).pack(pady=15)

Label(
    window,
    text="Enter Book ID"
).pack()

book_id = Entry(
    window,
    width=30
)
book_id.pack()

result = Label(
    window,
    text="",
    font=("Arial",11),
    justify=LEFT
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
    text="Delete",
    width=15,
    command=delete_book
).grid(row=0, column=1, padx=10)

Button(
    button_frame,
    text="⬅ Back",
    width=15,
    command=back
).grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()