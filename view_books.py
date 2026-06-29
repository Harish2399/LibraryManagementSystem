from tkinter import *
from tkinter import ttk
import sqlite3

window = Tk()

window.title("View Books")

window.geometry("850x400")

window.resizable(False, False)

Label(
    window,
    text="LIBRARY BOOKS",
    font=("Arial",16,"bold")
).pack(pady=10)

table = ttk.Treeview(
    window,
    columns=("ID","Name","Author","Status","Student"),
    show="headings"
)

table.heading("ID", text="Book ID")
table.heading("Name", text="Book Name")
table.heading("Author", text="Author")
table.heading("Status", text="Status")
table.heading("Student", text="Student")

table.column("ID", width=100)
table.column("Name", width=220)
table.column("Author", width=170)
table.column("Status", width=120)
table.column("Student", width=170)

table.pack(fill=BOTH, expand=True)

connection = sqlite3.connect("library.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

for row in rows:
    table.insert("", END, values=row)

connection.close()

Button(
    window,
    text="Close",
    command=window.destroy
).pack(pady=10)

window.mainloop()