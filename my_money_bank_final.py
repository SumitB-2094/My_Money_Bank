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
    name_entry = Entry(register_screen, textvariable=name,width=30)
    name_entry.pack()
    email_lable = Label(register_screen, text="email * ",font=('arial black',10))
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email,width=30)
    email_entry.pack()
    username_lable = Label(register_screen, text="Username * ",font=('arial black',10))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username,width=30)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ",font=('arial black',10))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*',width=30)
    password_entry.pack()
    Label(register_screen, text="").pack()

    Button(register_screen, text="Register", font=('rog fonts', 9), width=13, height=2, bg='#c4f8f8',command=register_user).pack()


# Designing window for login

def login():

    global name
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
    username_login_entry = Entry(login_screen, textvariable=username_verify,width=30)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",font=('arial black',10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,width=30, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", font=('rog fonts', 9), width=13, height=2, bg='#c4f8f8',command=login_verify).pack()


# Implementing event on register button

def register_user():
    global name_of_user2
    username_info = username.get()
    password_info = password.get()
    name_info=name.get()
    email_info=email.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(email_info)
    file.close()


    username_entry.delete(0, END)
    password_entry.delete(0, END)

    #global name_info

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button

def login_verify():
    global name
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
    login_success_screen.geometry("450x200")
    Label(login_success_screen, text="Login Success ",font=('calibri',22),bg='#fcb393').pack()
    Label(login_success_screen,text='\nProceed With Python Console for Further Process',fg='green',font=('arial black',10)).pack()
    Label(login_success_screen,text='\n').pack()
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

def delete_login_success():
    login_success_screen.destroy()
    name = (input("Enter your name:"))
    print('___________________________________\n')

    def one():
        print('          -:: ADD EXPENSE ::-')
        date = input('Date (dd/mm/yyyy) - ')
        print('___________________________________\n')
        a1 = str(input("Topic of Expense:"))
        b1 = (input("Expense:"))
        report_file = open(name + ".txt", 'a')
        report_file.write(date + ' - ')
        report_file.write(a1)
        report_file.write("-->")
        report_file.write("RS." + b1)
        report_file.write("\n")
        report_file.close()

        print('___________________________________\n')
        d = print("1-Add expenses:")
        e = print("2-LOGOUT")
        ans1 = input("\nEnter your choice:")
        print('___________________________________\n')

        if ans1 == '1':
            one()
        elif ans1 == '2':
            print('Thanks For using MY MONEY BANK')
        else:
            print('Enter Valid Choice.')

    def second():
        # read_for_graph = open(name+'.txt', 'r')
        Xreal = []
        Yreal = []
        Y = []

        filepath = name + '.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line.format(cnt, line.strip())
                # line = fp.readline()
                for i in range(len(line)):
                    exp = ''
                    if line[i] == 'S':
                        exp += line[i + 2::]
                        if exp[-1] == '\n':
                            exp = exp[0:-1:]
                            Y.append(exp)
                        else:
                            Y.append(exp)
                line = fp.readline()
                cnt += 1
                #print(Y)
        for i in range(len(Y)):
            Xreal.append(i)
            Yrealelement = float(Y[i])
            Yreal.append(Yrealelement)
            # print(Xreal)
            # print(Yreal)
        import matplotlib.pyplot as plt
        plt.plot(Xreal, Yreal, label='X/Y')
        # plt.xlim(0,740)
        # plt.ylim(0,70)
        plt.title('No. of expenses vs Expense')
        plt.xlabel('No. of Expenses')
        plt.ylabel('Expenses')
        plt.legend()  # for label .legend() is neccessary
        plt.savefig(name + '.png')
        from fpdf import FPDF
        r = FPDF()
        r.add_page()
        r.set_font("Arial", size=15)
        r.image('mmblogo.jpg', x=30, y=2, w=150)
        r.image(name + '.png', x=85, y=195, w=120)
        read_file_pdf = open(name + '.txt', 'r')
        r.cell(10, 10, txt=' ', ln=1, align="L")
        r.cell(10, 10, txt=' ', ln=1, align="L")
        r.cell(10, 10, txt=' ', ln=1, align="L")
        r.cell(10, 10, txt=' ', ln=1, align="L")
        r.cell(10, 8, txt=' ', ln=1, align="L")
        r.cell(10, 8, txt='[DATE - TOPIC --> EXPENSE]', ln=1, align="L")
        i = 0
        for line in read_file_pdf.readlines():
            i = str(i)
            sr = str(i + '] ')
            r.cell(10, 8, txt=sr + line, ln=1, align="L")
            i = int(i)
            i += 1
        top_3_exp = []
        check = Yreal
        one_max = max(check)
        top_3_exp.append(one_max)
        check.remove(one_max)
        second_max = max(check)
        top_3_exp.append(second_max)
        check.remove(second_max)
        third_max = max(check)
        top_3_exp.append(third_max)
        top_3_exp=str(top_3_exp)
        p='Maximum Three Expenses --> '+top_3_exp
        r.cell(10, 8, txt=p, ln=1, align="L")
        r.output(name + '.pdf')
        r = FPDF(orientation='P', unit='mm', format='A4')
        print('pdf successfully created!!')
        return 1

    def third():
        email_user=input('Email (___________@gmail.com)-->')
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        a = smtplib.SMTP('smtp.gmail.com', 587)
        a.ehlo()
        a.starttls()
        body = "Attached file is your Expense Report generated By MY MONEY BANK Software.\n \nThis is automatically generated mail.\nPlease, do not reply."

        msgeg = MIMEMultipart()
        msgeg['From'] = "MY MONEY BANK <'rushikeshudhan121000@gmail.com'>"  # SENDER
        # msgeg['To']='saktelrohit243@gmail.com'#RECIEVER
        msgeg['Subject'] = 'Monthly Expense Report '
        msgeg.attach(MIMEText(body, 'plain'))

        filename = name + ".pdf"
        attachment = open(name + ".pdf", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msgeg.attach(p)
        text = msgeg.as_string()
        reciever = email_user
        sender = 'rushikeshudhan121000@gmail.com'
        a.login('rushikeshudhan121000@gmail.com', '$100indiapune??')

        a.sendmail(sender, reciever, text)
        print("Successfully Sent File")
        a.quit()
        return 1

    def database():
        global database
        global ans
        a = print("1-Add expense:")
        b = print("2-Read/Create expense report (pdf) :")
        c = print("3-Email expense report:")
        ans = input("Enter your choice:")
        print('___________________________________\n')
        if ans == '1':
            one()
        elif ans == '2':
            second()
        elif ans=='3':
            third()
        else:
            print('Enter Valid Choice.')

    database()
    return 1


# Deleting popups

#def delete_login_success():
    #login_success_screen.destroy()


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
