import tkinter as tk
from db_operations import initialiseDB, add2Test, closeDB

# Initialize the database table
initialiseDB()

# GUI setup
root = tk.Tk()
root.title("Test DB")

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

# Button to add data to the test table
def on_add():
    test_id = entry_test_id.get()
    name = entry_name.get()
    age = entry_age.get()
    add2Test(test_id, name, age)
    entry_test_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)

button_add_test = tk.Button(root, text="Add Test", command=on_add)
button_add_test.grid(row=4, column=0, columnspan=2)

# Run the GUI loop
root.mainloop()

# Close the database when GUI is closed
closeDB()
