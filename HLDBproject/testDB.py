import tkinter as tk
import sqlite3
import os

#function to connect to the database and perform a action
def connectDB(function_to_call):

    #opens connection to DB
    conn = sqlite3.connect(os.path.dirname(os.path.abspath(__file__)) + '\HLDB.db') #we love chris
    cursor = conn.cursor()
    
    #passes cursor as a parameter for the function
    function_to_call(cursor)

    #closes connection to DB
    conn.commit()
    conn.close()

#INITALISING A TEST TABLE
def initialiseDB(cursor):

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS testtable (
                   test_id INTERGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTERGER NOT NULL
                )
            ''')#look into serial datatype
    
#function to view test DB
def viewDBTable(cursor):
    cursor.execute("SELECT * FROM testtable")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#function to add to test table
def add2Test(cursor):

    cursor.execute('''
            INSERT INTO testtable (test_id, name, age)
            VALUES (1, 'Matty', 28)
        ''')

connectDB(initialiseDB)

connectDB(viewDBTable)
print(r"connectDB(viewDBTable) has been executed")
connectDB(add2Test)
print("added to test")
connectDB(viewDBTable)

# Get the current directory of the running file
current_directory = os.path.dirname(os.path.abspath(__file__))
print("Current directory:", current_directory)


#basic auth good enough for most backend shit