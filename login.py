from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Library Login")

window.geometry("400x250")

window.resizable(False, False)

Label(
    window,
    text="Library Management System",
    font=("Arial",16,"bold")
).pack(pady=20)

Label(window,text="Username").pack()

username=Entry(window,width=25)

username.pack()

Label(window,text="Password").pack()

password=Entry(window,width=25,show="*")

password.pack()

def login():

    if username.get()=="admin" and password.get()=="1234":

        messagebox.showinfo("Success","Login Successful")

    else:

        messagebox.showerror("Error","Wrong Username or Password")

Button(
window,
text="Login",
width=20,
command=login
).pack(pady=20)

window.mainloop()