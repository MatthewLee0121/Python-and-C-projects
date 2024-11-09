import tkinter as tk
from backend import *

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
button_add_test.grid(row=4, column=0, columnspan=2)

button_view_table = tk.Button(root, text="View Table", command=on_view_table)
button_view_table.grid(row=5, column=0, columnspan=2)

#displays a list box to view tables
listbox_view_test = tk.Listbox(root, width=80, height=10)
listbox_view_test.grid(row=6, column=0, columnspan=2)


table_names = get_table_names()
selected_table = tk.StringVar(root)
selected_table.set(str(table_names[0]))

table_dropdown = tk.OptionMenu(root, selected_table, *table_names)
table_dropdown.grid(row=5, column=2, columnspan=2)

def get_dropdown_value():
   return selected_table.get()

# Run the GUI loop
root.mainloop()

# Close the database when GUI is closed
closeDB()
