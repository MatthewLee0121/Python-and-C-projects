import tkinter as tk
from tkinter import ttk, simpledialog
import time
import sys

file_path_list = [r"C:\Users\matty\Coding_with_beans\python projects\turtleexperiments\star"]
selected_index = 0  # Variable to store the selected index

def typing(message, delay=0.01):
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    return " "

def get_file_path():
    global file_path_list, selected_index
    file_path = file_path_list[selected_index]
    return file_path

def add_file_path():
    global file_path_list
    new_path = simpledialog.askstring("Input", "What is the new file path?")
    file_path_list.append(new_path)
    return file_path_list

def find_word():
    find = simpledialog.askstring("Input", "What word do you want to find?")
    return find

def get_replace():
    replace = simpledialog.askstring("Input", "What word do you want to replace it with?")
    return replace

def find_and_replace():
    global counter
    file_path = get_file_path()
    find = find_word()
    replace = get_replace()

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        if find in lines[i]:
            counter += 1
            lines[i] = lines[i].replace(find, replace)

    with open(file_path, 'w') as file:
        file.writelines(lines)

    if counter == 0:
        typing(f"'{find}' not found")
    else:
        typing(f"{counter} Occurrences of '{find}' replaced with '{replace}' in the file.")
        counter = 0

def how_many_occurrences():
    find = find_word()
    file_path = get_file_path()

    with open(file_path, 'r') as file:
        content = file.read()

    occurrences = content.count(find)
    typing(f"{occurrences} Occurrences of '{find}' in the file.")

def copy_to_new_file():
    file_path = get_file_path()

    with open(file_path, 'r') as file:
        content = file.read()

    new_file_path = simpledialog.askstring("Input", "Enter new file path:")

    with open(new_file_path, 'w') as new_file:
        new_file.write(content)

def on_combobox_select(event):
    global selected_index
    selected_index = file_path_list_combo.current()

# UI
window = tk.Tk()
window.title("Find And Replace Codingwithbeans")
window.geometry("500x200")
window.configure(bg="#f0f0f0")

file_path_window = tk.Tk()
file_path_window.title("File Path")
file_path_window.geometry("400x100")
file_path_window.configure(bg="#f0f0f0")
file_path_window_style = ttk.Style()
file_path_window_style.configure("FontMenu.TMenubutton", font=("Arial", 12))

font_var = tk.StringVar()
font_list = file_path_list

file_path_list_combo = ttk.Combobox(file_path_window, textvariable=font_var, values=font_list, style="FontMenu.TMenubutton", state="readonly")
file_path_list_combo.pack(pady=10)
file_path_list_combo.bind("<<ComboboxSelected>>", on_combobox_select)

find_and_replace_window = tk.Tk()
find_and_replace_window.title("Find and Replace")
find_and_replace_window.geometry("500x800")
find_and_replace_window.configure(bg="#f0f0f0")

def set_file_path_command():
    new_file_path = simpledialog.askstring("Input", "Enter new file path:")
    if new_file_path:
        file_path_list[0] = new_file_path

set_file_path_button = tk.Button(
    window,
    text="File Path Settings",
    command=file_path_window,
    padx=5,
    pady=5,
)
set_file_path_button.pack(pady=5)

find_and_replace_button = tk.Button(
    window,
    text="Find and Replace",
    command=find_and_replace,
    padx=5,
    pady=5
)
find_and_replace_button.pack(pady=5)

occurances_button = tk.Button(
    window,
    text="How many occurrences",
    command=how_many_occurrences,
    padx=5,
    pady=5,
)
occurances_button.pack(pady=5)

copy_file_to_new_button = tk.Button(
    window,
    text="Copy the lines to a new file",
    command=copy_to_new_file,
    padx=10,
    pady=10,
)
copy_file_to_new_button.pack(pady=5)

exit_button = tk.Button(
    window,
    text="Exit",
    command=window.destroy,
    padx=10,
    pady=10,
)
exit_button.pack(pady=5)

add_new_path_button = tk.Button(
    file_path_window,
    text = "Add a File Path",
    command=add_file_path,
    padx=5,
    pady=5,
)

add_new_path_button.pack(pady=5)

window.mainloop()
