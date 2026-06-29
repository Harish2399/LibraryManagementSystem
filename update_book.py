from tkinter import *
from tkinter import messagebox
import sqlite3

window = Tk()
window.title("Update Book")
window.geometry("500x420")
window.resizable(False, False)

Label(window,text="UPDATE BOOK",font=("Arial",18,"bold")).pack(pady=15)

Label(window,text="Book ID").pack()
book_id=Entry(window,width=30)
book_id.pack()

Label(window,text="Book Name").pack()
book_name=Entry(window,width=30)
book_name.pack()

Label(window,text="Author").pack()
author=Entry(window,width=30)
author.pack()


def search_book():

    if book_id.get()=="":

        messagebox.showerror("Error","Enter Book ID")
        return

    connection=sqlite3.connect("library.db")
    cursor=connection.cursor()

    cursor.execute(
        "SELECT * FROM books WHERE book_id=?",
        (book_id.get(),)
    )

    row=cursor.fetchone()

    connection.close()

    if row:

        book_name.delete(0,END)
        author.delete(0,END)

        book_name.insert(0,row[1])
        author.insert(0,row[2])

    else:

        messagebox.showerror("Error","Book Not Found")


def update_book():

    if book_name.get()=="" or author.get()=="":

        messagebox.showerror("Error","Fill all fields")
        return

    connection=sqlite3.connect("library.db")
    cursor=connection.cursor()

    cursor.execute(

        "UPDATE books SET book_name=?,author=? WHERE book_id=?",

        (
            book_name.get(),
            author.get(),
            book_id.get()
        )

    )

    connection.commit()

    connection.close()

    messagebox.showinfo("Success","Book Updated Successfully")

    book_id.delete(0,END)
    book_name.delete(0,END)
    author.delete(0,END)


Button(window,text="Search",width=20,command=search_book).pack(pady=10)

Button(window,text="Update",width=20,command=update_book).pack(pady=10)

window.mainloop()