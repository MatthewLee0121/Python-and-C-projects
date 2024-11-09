import tkinter as tk
from tkinter import messagebox as msgbx
import sqlite3
import os

conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\HLDB.db') #we love chris


#function to connect to the database and perform a action
#def connectDB(function_to_call):

    #opens connection to DB
    #conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\HLDB.db') #we love chris
    #cursor = conn.cursor()
    
    #passes cursor as a parameter for the function
    #function_to_call(cursor)

    #closes connection to DB
    #conn.commit()
    #conn.close()

#INITALISING A TEST TABLE
def initialiseDB():
    
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS testtable (
                   test_id INTERGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTERGER NOT NULL
                )
            ''')#look into serial datatype
    conn.commit()
#function to view test DB
def viewDBTable(cursor):
    cursor.execute("SELECT * FROM testtable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#function to add to test table
def add2Test():

    test_id = entry_test_id.get()
    name = entry_name.get()
    age = entry_age.get()

    if test_id and name and age:
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO testtable (test_id, name, age)
                VALUES (?, ?, ?)
            ''', (test_id, name, age))
        conn.commit()
        msgbx.showinfo("Success", "test added successfully")
        entry_test_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
    else:
        msgbx.showerror('Error', 'Please enter a input in all fields')

# connectDB(initialiseDB)

# connectDB(viewDBTable)
# print(r"connectDB(viewDBTable) has been executed")
# connectDB(add2Test)
# print("added to test")
# connectDB(viewDBTable)
#basic auth good enough for most backend shit


root = tk.Tk()
root.title("test DB")

label_test_id = tk.Label(
    root,
    text="Test_id: "
    )
label_test_id.grid(
    row= 0,
    column= 0
    )

entry_test_id = tk.Entry(
    root
    )
entry_test_id.grid(
    row=0,
    column=1
    )

label_name = tk.Label(
    root,
    text="name: "
    )
label_name.grid(
    row=1,
    column=0
    )

entry_name = tk.Entry(
    root
    )
entry_name.grid(
    row=1,
    column=1
    )

label_age = tk.Label(
    root,
    text="age:"
    )

label_age.grid(
    row=2,
    column=0
    )

entry_age = tk.Entry(
    root
    )

entry_age.grid(
    row=2,
    column=1
    )

button_add_test = tk.Button(
    root,
    text="Add test",
    command=add2Test
    )

button_add_test.grid(
    row=4,
    column=0,
    columnspan=2
    )

initialiseDB()
root.mainloop()
conn.close()