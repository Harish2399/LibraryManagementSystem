import sqlite3
import csv
from tkinter import messagebox

connection = sqlite3.connect("library.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

with open("books_export.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        [
            "Book ID",
            "Book Name",
            "Author",
            "Status",
            "Student"
        ]
    )

    writer.writerows(rows)

connection.close()

messagebox.showinfo(
    "Success",
    "Books Exported Successfully"
)