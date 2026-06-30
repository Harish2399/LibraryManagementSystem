from tkinter import *
from tkinter import ttk
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
# Main Window
# -----------------------------
window = Tk()

window.title("View Books")

window.geometry("900x450")

window.resizable(False, False)

Label(
    window,
    text="LIBRARY BOOKS",
    font=("Arial", 16, "bold")
).pack(pady=10)

# -----------------------------
# Table
# -----------------------------
table = ttk.Treeview(
    window,
    columns=("ID", "Name", "Author", "Status", "Student"),
    show="headings"
)

table.heading("ID", text="Book ID")
table.heading("Name", text="Book Name")
table.heading("Author", text="Author")
table.heading("Status", text="Status")
table.heading("Student", text="Student")

table.column("ID", width=100, anchor=CENTER)
table.column("Name", width=220, anchor=CENTER)
table.column("Author", width=170, anchor=CENTER)
table.column("Status", width=120, anchor=CENTER)
table.column("Student", width=170, anchor=CENTER)

# -----------------------------
# Scrollbar
# -----------------------------
scrollbar = Scrollbar(window, orient=VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
table.pack(fill=BOTH, expand=True)

# -----------------------------
# Load Data
# -----------------------------
connection = sqlite3.connect("library.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM books")

rows = cursor.fetchall()

for row in rows:
    table.insert("", END, values=row)

connection.close()

# -----------------------------
# Buttons
# -----------------------------
button_frame = Frame(window)
button_frame.pack(pady=10)

Button(
    button_frame,
    text="⬅ Back",
    width=15,
    command=back
).grid(row=0, column=0, padx=10)

Button(
    button_frame,
    text="Close",
    width=15,
    command=window.destroy
).grid(row=0, column=1, padx=10)

window.mainloop()