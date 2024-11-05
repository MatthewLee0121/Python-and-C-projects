import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect/create database
conn = sqlite3.connect('')
cursor = conn.cursor()

# Create some tables if they do not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT NOT NULL,
        published_date TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Members (
        member_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        phone_number TEXT,
        membership_date TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Borrowing (
        borrow_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        member_id INTEGER,
        borrow_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES Books (book_id),
        FOREIGN KEY (member_id) REFERENCES Members (member_id)
    )
''')

# Commit and close the connection
conn.commit()
conn.close()

##########################################GUI######################################

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    isbn = entry_isbn.get()
    published_date = entry_published_date.get()

    if title and author and isbn:
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Books (title, author, isbn, published_date)
            VALUES (?, ?, ?, ?)
        ''', (title, author, isbn, published_date))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Book added successfully")
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)
        entry_published_date.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields are required")

# Function to display all books
def view_books():
    # Connect to the database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Fetch all records from the Books table
    cursor.execute('SELECT * FROM Books')
    rows = cursor.fetchall()
    
    # Clear the listbox before adding new data
    listbox_books.delete(0, tk.END)
    
    # Insert data into the listbox
    for row in rows:
        listbox_books.insert(tk.END, f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | ISBN: {row[3]} | Published Date: {row[4]}")
    
    # Close the database connection
    conn.close()

# Set up the main window
root = tk.Tk()
root.title("Library Management System")

# Create and place widgets (labels, entry fields, buttons) for adding books
label_title = tk.Label(root, text="Title:")
label_title.grid(row=0, column=0)

entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1)

label_author = tk.Label(root, text="Author:")
label_author.grid(row=1, column=0)

entry_author = tk.Entry(root)
entry_author.grid(row=1, column=1)

label_isbn = tk.Label(root, text="ISBN:")
label_isbn.grid(row=2, column=0)

entry_isbn = tk.Entry(root)
entry_isbn.grid(row=2, column=1)

label_published_date = tk.Label(root, text="Published Date:")
label_published_date.grid(row=3, column=0)

entry_published_date = tk.Entry(root)
entry_published_date.grid(row=3, column=1)

button_add_book = tk.Button(root, text="Add Book", command=add_book)
button_add_book.grid(row=4, column=0, columnspan=2)

# Create a button to view books
button_view_books = tk.Button(root, text="View Books", command=view_books)
button_view_books.grid(row=5, column=0, columnspan=2)

# Create a Listbox to display the books
listbox_books = tk.Listbox(root, width=80, height=10)
listbox_books.grid(row=6, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
 