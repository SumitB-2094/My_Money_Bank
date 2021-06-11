
#select choice
def choice():
    print('\n\n       -:: MY MONEY BANK ::-'
          '\n______________________________________')
    print(
        '1]   Register.'
        '\n2]   Login.')
    print('______________________________________')
    ans = input('\n--Select a valid choice--')
    if ans == '1':
        import register
        import main
    elif ans == '2':
        import login
    else:
        print('\nEnter valid choice')
        choice()
choice()
