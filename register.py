#register
def register():
    name=input('Name -')
    email=input('Email id -')
    usrnm=input('Create Username (8 char) -')
    reusrnm=input('Rewrite Username -')
    if usrnm==reusrnm:
        if len(usrnm)==8:
            psswrd = input('Create Password (8 char) -')
            repsswrd = input('Rewrite Password -')
            if psswrd == repsswrd:
                if len(psswrd)==8:
                    check=open('Details.txt','a')
                    print(usrnm,psswrd,file=check)
                    mail=open('emails.txt','a')
                    print(usrnm,email,file=mail)
                    print('--- Profile Successfully Created ---')
                    print('--- You can login Now ---')
                    
                    
                else:
                    print('length of password must be 8 char\ncreate again.....')
                    register()
            else:
                print('Password not matching\n register again\n_______________________________________\n\n')
                register()
                return
        else:
            print('username must be of 8 char only\ncreate again.....')
            register()
    else:
        print('Username not matching\n register again\n_______________________________________\n\n')
        register()
register()
