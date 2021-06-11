name=(input("Enter your name:"))
print("-------------------------------------------------------------------------------------------")

a=print("1-Add expense:")
b=print("2-Read expense report:")
c=print("3-Email expense report:")
ans=int(input("Enter your choice:"))

def database():
    global database
    global ans
    if ans==1:
        a1=str(input("Topic of Expense:"))
        b1=(input("Expense:"))
        report_file=open(name+".txt",'a')
        report_file.write(a1)
        report_file.write("-->")
        report_file.write("RS."+b1)
        report_file.write("\n")
        report_file.close()
database()

def asking_():
    global database
    d=print("4-Add expenses:")
    e=print("5-LOGOUT")
    ans1=int(input("Enter your choice:"))

    if ans1==4:
        return database()
asking_()




