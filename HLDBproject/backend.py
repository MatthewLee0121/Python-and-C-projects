import sqlite3
import os
from tkinter import messagebox as msg
import hashlib

# Set up the database connection (global variables might fix this later to not be a global but will develop the programme more)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HLDB.db')
conn = sqlite3.connect(db_path)

# Function to initialize the test table
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

#hash the password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

#initiates the username and password table
def InitiateUNPWTable():
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)
    conn.commit()

#function to add to usernames and passwords table
def insert_user(username: str, password: str):

    cursor = conn.cursor()
    
    try:
        password_hash = hash_password(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        print("User added successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")

def verify_credentials(username: str, password: str) -> bool:
    cursor = conn.cursor()
    password_hash = hash_password(password)
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    
    if result and result[0] == password_hash:
        return True
    else:
        return False


# Function to view the test table
def viewDBTable(table_name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    return rows


# Function to add a new entry to the test table
def add2Test(table_name, test_id, name, age):
    if test_id and name and age:
        cursor = conn.cursor()

        query = f"INSERT INTO {table_name} (test_id, name, age) VALUES (?, ?, ?)"
        cursor.execute(query, (test_id, name, age))
        conn.commit()
        msg.showinfo("Success", "Test added successfully")
    else:
        msg.showerror('Error', 'Please enter input in all fields')

def getTableNames():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [table[0] for table in cursor.fetchall()]
    return tables

def getTableColumnNames(table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cursor.fetchall()]
    return columns

def swapUnderToSpace(text):
    text = text.replace("_", " ")
    return text

def swapSpaceToUnder(text):
    text = text.replace(" ", "_")
    return text

# Close the database connection when done
def closeDB():
    conn.close()
