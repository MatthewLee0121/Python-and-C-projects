import tkinter as tk
from tkinter import filedialog, messagebox
from BackEnd import get_ascii_art

def get_image_path():
    selected_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    return selected_file_path

def open_file(selected_file_path, font_size, rows, columns, line_detection):
    if selected_file_path:
        try:
            # Generate ASCII art
            ascii_art = get_ascii_art(selected_file_path, rows, columns, line_detection)
            
            # Display ASCII art in a new window
            ascii_window = tk.Tk()
            ascii_window.title("ASCII Art")
            ascii_window.geometry("500x300")
            ascii_window.configure(bg="#f0f0f0")

            text_widget = tk.Text(ascii_window, wrap=tk.WORD, width=50, height=15, font=("Courier", font_size))
            text_widget.insert(tk.END, ascii_art)
            text_widget.pack(pady=20)

            # Add save button
            def save_ascii_art():
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
                if file_path:
                    with open(file_path, 'w') as file:
                        file.write(ascii_art)
                    messagebox.showinfo("Save", "ASCII Art saved successfully!")

            save_button = tk.Button(ascii_window, text="Save ASCII Art", command=save_ascii_art)
            save_button.pack(pady=10)

            ascii_window.mainloop()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate ASCII art: {e}")

def create_main():
    main_window = tk.Tk()
    main_window.title("Settings for your generation!")
    main_window.geometry("400x600")
    main_window.configure(bg="#f0f0f0")

    # Variables
    font_size_var = tk.IntVar(value=12)
    rows = tk.IntVar(value=3)
    columns = tk.IntVar(value=3)
    line_detection = tk.BooleanVar()

    # Generate artwork button
    get_art_button = tk.Button(
        main_window,
        text="Generate artwork",
        font=("Rockabilly", 10),
        command=lambda: open_file(get_image_path(), font_size_var.get(), rows.get(), columns.get(), line_detection.get()),
        width=20,
        height=2
    )
    get_art_button.pack(pady=10)

    # Select image button
    get_image_path_button = tk.Button(
        main_window,
        text="Select image",
        font=("Rockabilly", 10),
        command=get_image_path,
        width=20,
        height=2
    )
    get_image_path_button.pack(pady=10)

    # Font size scale
    font_size_scale = tk.Scale(
        main_window,
        from_=5,
        to_=30,
        orient=tk.HORIZONTAL,
        variable=font_size_var,
        label="Font Size"
    )
    font_size_scale.pack(pady=10)

    # Rows scale
    rows_scale = tk.Scale(
        main_window,
        from_=1,
        to_=10,
        orient=tk.HORIZONTAL,
        variable=rows,
        label="Y Scaling"
    )
    rows_scale.pack(pady=10)

    # Columns scale
    columns_scale = tk.Scale(
        main_window,
        from_=1,
        to_=10,
        orient=tk.HORIZONTAL,
        variable=columns,
        label="X Scaling"
    )
    columns_scale.pack(pady=10)

    # Line detection checkbox
    LineDetection_box = tk.Checkbutton(
        main_window,
        text='Line Detection (Edge Detection)',
        variable=line_detection,
        onvalue=True,
        offvalue=False,
    )
    LineDetection_box.pack(pady=10)

    # Return the main window
    return main_window

# Create and display the main window
main_window = create_main()
main_window.mainloop()
