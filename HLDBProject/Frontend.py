import backend.cpp  # The compiled C++ module with wrapped functions
from tkinter import *

def connect_to_db():
    if my_backend.connect_to_db() == 0:
        print("Database connected successfully!")
    else:
        print("Failed to connect to database.")

root = Tk()
connect_button = Button(root, text="Connect to Database", command=connect_to_db)
connect_button.pack()
root.mainloop()
