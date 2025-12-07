from tkinter import *
from tkinter import messagebox

r = Tk()
r.geometry("400x450")
r.title("User Registration")

title_lbl = Label(r, text="User Registration", font=("Arial", 18, "bold"))
title_lbl.pack(pady=20)

user_lbl = Label(r, text="Username:", font=("Arial", 12))
user_lbl.pack()
username = Entry(r, font=("Arial", 12))
username.pack(pady=5)

email_lbl = Label(r, text="Email:", font=("Arial", 12))
email_lbl.pack()
email = Entry(r, font=("Arial", 12))
email.pack(pady=5)

pass_lbl = Label(r, text="Password:", font=("Arial", 12))
pass_lbl.pack()
password = Entry(r, show="*", font=("Arial", 12))
password.pack(pady=5)

cpass_lbl = Label(r, text="Confirm Password:", font=("Arial", 12))
cpass_lbl.pack()
cpassword = Entry(r, show="*", font=("Arial", 12))
cpassword.pack(pady=5)

def register_user():
    user = username.get()
    em = email.get()
    pwd = password.get()
    cpwd = cpassword.get()

    if user == "" or em == "" or pwd == "" or cpwd == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    if pwd != cpwd:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    messagebox.showinfo("Success", f"User '{user}' registered successfully!")

register_btn = Button(r,text="Register",command=register_user, bg="blue",fg="white",font=("Arial", 12))
register_btn.pack(pady=20)

r.mainloop()
