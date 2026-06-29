from tkinter import *
import sqlite3

# -----------------------------
# Functions
# -----------------------------

def statistics():

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE status='Available'")
    available = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE status='Issued'")
    issued = cursor.fetchone()[0]

    connection.close()

    total_label.config(text=f"📚 Total Books : {total}")
    available_label.config(text=f"✅ Available Books : {available}")
    issued_label.config(text=f"📖 Issued Books : {issued}")


# -----------------------------
# Open Windows
# -----------------------------

def open_add_book():
    window.destroy()
    import add_book


def open_view_books():
    window.destroy()
    import view_books


def open_search_book():
    window.destroy()
    import search_book


def open_delete_book():
    window.destroy()
    import delete_book


def open_issue_book():
    window.destroy()
    import issue_book


def open_return_book():
    window.destroy()
    import return_book


def export():
    import export_books


# -----------------------------
# Main Window
# -----------------------------

window = Tk()

window.title("Library Management System")

window.geometry("850x720")

window.configure(bg="#F2F6FC")

window.resizable(False, False)

# -----------------------------
# Heading
# -----------------------------

Label(
    window,
    text="📚 LIBRARY MANAGEMENT SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#F2F6FC",
    fg="#003366"
).pack(pady=20)

Label(
    window,
    text="Welcome Admin",
    font=("Arial", 15, "bold"),
    bg="#F2F6FC",
    fg="gray25"
).pack()

Frame(
    window,
    bg="#1976D2",
    height=3
).pack(fill=X, pady=15)

# -----------------------------
# Statistics
# -----------------------------

stats = Frame(window, bg="#F2F6FC")
stats.pack()

total_label = Label(
    stats,
    font=("Arial", 13, "bold"),
    width=30,
    bg="#BBDEFB",
    fg="#0D47A1",
    pady=8
)

total_label.pack(pady=5)

available_label = Label(
    stats,
    font=("Arial", 13, "bold"),
    width=30,
    bg="#C8E6C9",
    fg="#1B5E20",
    pady=8
)

available_label.pack(pady=5)

issued_label = Label(
    stats,
    font=("Arial", 13, "bold"),
    width=30,
    bg="#FFCDD2",
    fg="#B71C1C",
    pady=8
)

issued_label.pack(pady=5)

statistics()

Frame(
    window,
    bg="#1976D2",
    height=3
).pack(fill=X, pady=20)

# -----------------------------
# Buttons
# -----------------------------

button_frame = Frame(window, bg="#F2F6FC")
button_frame.pack()

btn_style = {
    "width": 20,
    "height": 2,
    "bg": "#1976D2",
    "fg": "white",
    "activebackground": "#0D47A1",
    "activeforeground": "white",
    "font": ("Arial", 11, "bold")
}

Button(
    button_frame,
    text="Add Book",
    command=open_add_book,
    **btn_style
).grid(row=0, column=0, padx=15, pady=10)

Button(
    button_frame,
    text="View Books",
    command=open_view_books,
    **btn_style
).grid(row=0, column=1, padx=15, pady=10)

Button(
    button_frame,
    text="Search Book",
    command=open_search_book,
    **btn_style
).grid(row=1, column=0, padx=15, pady=10)

Button(
    button_frame,
    text="Delete Book",
    command=open_delete_book,
    **btn_style
).grid(row=1, column=1, padx=15, pady=10)

Button(
    button_frame,
    text="Issue Book",
    command=open_issue_book,
    **btn_style
).grid(row=2, column=0, padx=15, pady=10)

Button(
    button_frame,
    text="Return Book",
    command=open_return_book,
    **btn_style
).grid(row=2, column=1, padx=15, pady=10)

Button(
    button_frame,
    text="Export Books",
    command=export,
    **btn_style
).grid(row=3, column=0, padx=15, pady=10)

Button(
    button_frame,
    text="Exit",
    command=window.destroy,
    **btn_style
).grid(row=3, column=1, padx=15, pady=10)

# -----------------------------
# Footer
# -----------------------------

Label(
    window,
    text="Developed by Harish Ragavendra © 2026",
    font=("Arial", 10),
    bg="#F2F6FC",
    fg="gray50"
).pack(side=BOTTOM, pady=15)

window.mainloop()