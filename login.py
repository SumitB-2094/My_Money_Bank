#login
def login():
    usr_un=input('\nUsername--')
    usr_ps=input('password -')
    check_username_psswrd=open('Details.txt','r')
    for lines in check_username_psswrd.readlines():
        a=''
        b=''
        a=a+lines[0:8:1]
        b=b+lines[9:-1:]
        if a==usr_un:
            print('\nUsername Verified')
            if b==usr_ps:
                print('\nPassword Verified')
        else:
            print('\nEnter valid Username or Password')
            print('b==',b)
            login()
login()
