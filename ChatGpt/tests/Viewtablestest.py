import tkinter as tk
from tkinter import messagebox
import sqlite3

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

# Create and place widgets for adding books (as you've done)
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
