from tkinter import *
import sqlite3

root=Tk()

#databases
# create a database.
conn=sqlite3.connect(r'MMB REPORT.db')

    # create cursor
c=conn.cursor()

c.execute("""CREATE TABLE report(TOPIC_EXPENSE text,
EXPENDITURE integer
)""")

c=conn.commit()


# create submit function for database
def submit():

    data=sqlite3.connect(r'MMB REPORT.db')
    c = conn.cursor()
# insert into table

    c.execute("INSERT INTO report VALUES(:TOPIC_EXPENSE,:EXPENDITURE)",
              {
                  'TOPIC_EXPENSE':TOPIC_EXPENSE.get(),
                  'EXPENDITURE':EXPENDITURE.get()})
    # commit changes
    conn.commit()

    # close connection


    # clear the text boxes
    TOPIC_EXPENSE.delete(0,END)
    EXPENDITURE.delete(0,END)

#create query function

def query():
    conn = sqlite3.connect(r'MMB REPORT.db')

    # create cursor
    c = conn.cursor()

    # query database
    c.execute("SELECT *,oid FROM report")
    records=c.fetchall()
    print(records)

    print_records=""
    for records in records:
        print_records+=str(records)+"\n"

    query_label=Label(root,text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)
    # commit changes
    conn.commit()

    # create textboxes

TOPIC_EXPENSE=Entry(root,width=30)
TOPIC_EXPENSE.grid(row=0,column=1,padx=20)

EXPENDITURE=Entry(root,width=30)
EXPENDITURE.grid(row=2,column=1,padx=20)

# create textbox labels

TOPIC_EXPENSE_label=Label(root,text="TOPIC_EXPENSE")
TOPIC_EXPENSE_label.grid(row=0,column=0,padx=20)


EXPENDITURE_label=Label(root,text="EXPENDITURE")
EXPENDITURE_label.grid(row=2,column=0,padx=20)

# create submit button.

submit_btn=Button(root,text="Add record to database",command=submit)
submit_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

# create a query button

query_btn=Button(root,text="show records",command=query)
query_btn.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=137)


root.mainloop()