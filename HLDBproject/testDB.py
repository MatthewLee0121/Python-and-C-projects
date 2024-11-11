import tkinter as tk
from tkinter import messagebox as msgbx
import sqlite3
import os
from backend import *

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

#initialiseDB()
#root.mainloop()
#conn.close()


def CreateHomeScreen():
    # Initialize the database table
    initialiseDB()

    # GUI setup
    root = tk.Tk()
    root.title("Test DB")

    # Button to add data to the test table
    def on_add_test():
        test_id = entry_test_id.get()
        name = entry_name.get()
        age = entry_age.get()

        table_name = get_dropdown_value()
        add2Test(table_name, test_id, name, age)

        entry_test_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)

    # Function to view the selected table
    def on_view_table():
        # Get the selected table from the dropdown
        table_name = get_dropdown_value()

        # Fetch rows from the selected table and update the listbox
        rows = viewDBTable(table_name)

        # Clear the listbox before adding new data
        listbox_view_test.delete(0, tk.END)
        
        # Insert data into the listbox
        for row in rows:
            listbox_view_test.insert(tk.END, f"test_id: {row[0]} | name: {row[1]} | age: {row[2]}")


    # Entry fields and labels for user input
    label_test_id = tk.Label(root, text="Test ID:")
    label_test_id.grid(row=0, column=0)

    entry_test_id = tk.Entry(root)
    entry_test_id.grid(row=0, column=1)

    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=1, column=0)

    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1)

    label_age = tk.Label(root, text="Age:")
    label_age.grid(row=2, column=0)

    entry_age = tk.Entry(root)
    entry_age.grid(row=2, column=1)

    button_add_test = tk.Button(root, text="Add Test", command=on_add_test)
    button_add_test.grid(row=4, column=1, columnspan=2)

    button_view_table = tk.Button(root, text="View Table", command=on_view_table)
    button_view_table.grid(row=2, column=2, columnspan=2)

    #displays a list box to view tables
    listbox_view_test = tk.Listbox(root, width=80, height=10)
    listbox_view_test.grid(row=0, column=11, columnspan=2, rowspan=6)


    table_names = get_table_names()
    selected_table = tk.StringVar(root)
    selected_table.set(str(table_names[0]))

    label_tabel_name = tk.Label(root, text="Table Name: ")
    label_tabel_name.grid(row=3, column=0)

    table_dropdown = tk.OptionMenu(root, selected_table, *table_names)
    table_dropdown.grid(row=3, column=1)

    def get_dropdown_value():
        return selected_table.get()

    root.mainloop()

CreateHomeScreen()