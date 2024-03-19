import tkinter as tk
import math
#creating a calculator
#update the label in the calculator
#why does the onkeypress not work?!?!?
def update_label(num):
    if num == "\b":
        remove_last()
    else:
        input_output_label.config(text=input_output_label.cget("text") + str(num))

def remove_last():
    old = input_output_label.cget("text")
    new = old[:-1]
    input_output_label.config(text=new)

def equal_button_press(string):
    try:
        total = eval(string)
        total_label.config(text=str(total))
    except Exception as e:
        total_label.config(text="Error")
        print("Error:", e)

def on_key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/()" or key == "\b":
        update_label(key)
    elif key == "=":
        equal_button_press(input_output_label.cget("text"))

main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry("800x300")
main_window.configure(bg="#f0f0f0")


input_output_label = tk.Label(
    main_window,
    text="",
    font=("Rockabilly", 10),
    width=10,
    height=2
)
input_output_label.grid(column=1, row=1)

total_label = tk.Label(
    main_window,
    text="",
    font=("Rockabilly", 10),
    width=10,
    height=2
)
total_label.grid(column=3, row=1)

button_1 = tk.Button(
    main_window,
    text="1",
    font=("Rockabilly", 10),
    command=lambda: update_label(1),
    width=10,
    height=2
)
button_1.grid(column=1, row=2)

button_2 = tk.Button(
    main_window,
    text="2",
    font=("Rockabilly", 10),
    command=lambda: update_label(2),
    width=10,
    height=2
)
button_2.grid(column=2, row=2)

button_3 = tk.Button(
    main_window,
    text="3",
    font=("Rockabilly", 10),
    command=lambda: update_label(3),
    width=10,
    height=2
)
button_3.grid(column=3, row=2)

button_4 = tk.Button(
    main_window,
    text="4",
    font=("Rockabilly", 10),
    command=lambda: update_label(4),
    width=10,
    height=2
)
button_4.grid(column=1, row=3)

button_5 = tk.Button(
    main_window,
    text="5",
    font=("Rockabilly", 10),
    command=lambda: update_label(5),
    width=10,
    height=2
)
button_5.grid(column=2, row=3)

button_6 = tk.Button(
    main_window,
    text="6",
    font=("Rockabilly", 10),
    command=lambda: update_label(6),
    width=10,
    height=2
)
button_6.grid(column=3, row=3)

button_7 = tk.Button(
    main_window,
    text="7",
    font=("Rockabilly", 10),
    command=lambda: update_label(7),
    width=10,
    height=2
)
button_7.grid(column=1, row=4)

button_8 = tk.Button(
    main_window,
    text="8",
    font=("Rockabilly", 10),
    command=lambda: update_label(8),
    width=10,
    height=2
)
button_8.grid(column=2, row=4)

button_9 = tk.Button(
    main_window,
    text="9",
    font=("Rockabilly", 10),
    command=lambda: update_label(9),
    width=10,
    height=2
)
button_9.grid(column=3, row=4)

button_0 = tk.Button(
    main_window,
    text="0",
    font=("Rockabilly", 10),
    command=lambda: update_label(0),
    width=10,
    height=2
)
button_0.grid(column=2, row=5)

button_plus = tk.Button(
    main_window,
    text="+",
    font=("Rockabilly", 10),
    command=lambda: update_label("+"),
    width=10,
    height=2
)
button_plus.grid(column=4, row= 2)

button_sub = tk.Button(
    main_window,
    text="-",
    font=("Rockabilly", 10),
    command=lambda: update_label("-"),
    width=10,
    height=2
)
button_sub.grid(column=4, row= 3)

button_multiply = tk.Button(
    main_window,
    text="*",
    font=("Rockabilly", 10),
    command=lambda: update_label("*"),
    width=10,
    height=2
)
button_multiply.grid(column=4, row= 4)

button_equal = tk.Button(
    main_window,
    bg='Green',
    text="=",
    font=("Rockabilly", 10),
    command=lambda: equal_button_press(input_output_label.cget("text")),
    width=10,
    height=2
)
button_equal.grid(column=5, row= 5)

button_divide = tk.Button(
    main_window,
    text="/",
    font=("Rockabilly", 10),
    command=lambda: update_label("/"),
    width=10,
    height=2
)
button_divide.grid(column=4, row= 5)

button_bracket_open = tk.Button(
    main_window,
    text="(",
    font=("Rockabilly", 10),
    command=lambda: update_label("("),
    width=10,
    height=2
)
button_bracket_open.grid(column=5, row= 4)

button_bracket_close = tk.Button(
    main_window,
    text=")",
    font=("Rockabilly", 10),
    command=lambda: update_label(")"),
    width=10,
    height=2
)
button_bracket_close.grid(column=5, row= 3)

button_backone = tk.Button(
    main_window,
    bg= 'Red',
    text="Del last",
    font=("Rockabilly", 10),
    command=lambda: update_label("\b"),
    width=10,
    height=2
)
button_backone.grid(column=5, row= 2)

button_sin = tk.Button(
    main_window,
    text="sin",
    font=("Rockabilly", 10),
    command=lambda: update_label("sin("),
    width=10,
    height=2
)
button_sin.grid(column=6, row= 2)

button_cos = tk.Button(
    main_window,
    text="cos",
    font=("Rockabilly", 10),
    command=lambda: update_label("cos("),
    width=10,
    height=2
)
button_cos.grid(column=6, row= 3)

main_window.bind("<KeyPress>", on_key_press)

main_window.mainloop()


