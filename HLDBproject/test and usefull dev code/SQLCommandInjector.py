import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
import os

# Set up the SQLite connection
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'HLDB.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a basic Tkinter app
root = tk.Tk()
root.title("SQL Command Executor")

# Label for input
label = tk.Label(root, text="Enter SQL Command:")
label.pack()

# Text area for SQL command input
sql_input = scrolledtext.ScrolledText(root, width=60, height=10)
sql_input.pack()

# Text area for SQL output
output = scrolledtext.ScrolledText(root, width=60, height=10, state='disabled')
output.pack()

# Function to execute SQL commands
def execute_sql():
    command = sql_input.get("1.0", "end-1c")  # Get the text from input
    try:
        cursor.execute(command)
        conn.commit()  # Commit any changes
        
        # If it's a SELECT command, fetch and display the results
        if command.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            display_text = "\n".join([str(row) for row in rows])
        else:
            display_text = "Command executed successfully."
        
        # Display output
        output.config(state='normal')
        output.delete("1.0", "end")
        output.insert("1.0", display_text)
        output.config(state='disabled')
    
    except sqlite3.Error as e:
        # Show error message
        messagebox.showerror("SQL Error", str(e))

# Execute button
execute_button = tk.Button(root, text="Execute SQL", command=execute_sql)
execute_button.pack()

# Run the app
root.protocol("WM_DELETE_WINDOW", lambda: close_app())  # Close event handling

def close_app():
    conn.close()  # Ensure the database connection is closed when the app is closed
    root.quit()   # Terminate the Tkinter main loop

root.mainloop()
