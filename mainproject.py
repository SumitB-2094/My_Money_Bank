# import modules

from tkinter import *
import os


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Registration")
    register_screen.geometry("450x350")

    global username
    global password
    global name
    global email
    global username_entry
    global password_entry
    global name_entry
    global email_entry
    username = StringVar()
    password = StringVar()
    name=StringVar()
    email=StringVar()



    Label(register_screen, text="Registration",bg='#f2ad4a',width='300',height='2',font=('ROG FONTS',20)).pack()
    Label(register_screen, text="").pack()
    name_lable = Label(register_screen, text="Name * ",font=('arial black',10))
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    email_lable = Label(register_screen, text="email * ",font=('arial black',10))
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    username_lable = Label(register_screen, text="Username * ",font=('arial black',10))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",font=('arial black',10))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", font=('rog fonts', 9), width=13, height=2, bg='#c4f8f8',command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("450x350")
    Label(login_screen, text="Login",bg='#f2ad4a',width='300',height='2',font=('ROG FONTS',20)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ",font=('arial black',10)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",font=('arial black',10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", font=('rog fonts', 9), width=13, height=2, bg='#c4f8f8',command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()
    email_info=email.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("250x150")
    Label(login_success_screen, text="Login Success",font=('Comic sans ms',15),bg='#4af261').pack()
    Label(text='\n').pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("250x150")
    Label(password_not_recog_screen, text="Invalid Password",bg='#f2ad4a').pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found",bg='#f2ad4a').pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("450x350")
    main_screen.title("Account Login")
    Label(text='MY MONEY BANK', bg='#f2ad4a', width='300', height='2', font=('ROG FONTS', 20)).pack()
    Label(text='\n \n').pack()

    Button(text="Login",font=('comic sans ms', 14), width=13, height=1, bg='#c4f8f8', command=login).pack()
    Label(text="\n").pack()
    Button(text="Register",font=('Comic sans ms', 14), width=13, height=1, bg='#c4f8f8', command=register).pack()

    main_screen.mainloop()
main_account_screen()