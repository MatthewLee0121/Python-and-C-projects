import sqlite3
import os
from tkinter import messagebox as msgbx

# Set up the database connection
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HLDB.db')
conn = sqlite3.connect(db_path)

# Function to initialize the test table
def initialiseDB():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS testtable (
            test_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()

# Function to view the test table
def viewDBTable():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM testtable")
    rows = cursor.fetchall()
    return rows

# Function to add a new entry to the test table
def add2Test(test_id, name, age):
    if test_id and name and age:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO testtable (test_id, name, age)
            VALUES (?, ?, ?)
        ''', (test_id, name, age))
        conn.commit()
        msgbx.showinfo("Success", "Test added successfully")
    else:
        msgbx.showerror('Error', 'Please enter input in all fields')

# Close the database connection when done
def closeDB():
    conn.close()
