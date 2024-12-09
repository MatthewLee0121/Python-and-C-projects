import tkinter as tk
from tkinter import filedialog, messagebox
import BackEnd  # Assuming the backend code is in a module named BackEnd

# Global variable to hold the selected file path
selected_file_path = None

def select_image(preview_widget):
    """Function to select an image file."""
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if selected_file_path:
        messagebox.showinfo("Image Selected", f"Selected file: {selected_file_path}")
        preview_widget.delete("1.0", tk.END)  # Clear preview widget
        preview_widget.insert(tk.END, "Image selected. Ready to generate ASCII art!")
    else:
        messagebox.showwarning("No File Selected", "Please select an image file.")

def generate_art(preview_widget, block_size, line_detection):
    """Function to generate ASCII art."""
    global selected_file_path
    if selected_file_path:
        try:
            # Generate ASCII art using backend
            ascii_art = BackEnd.get_ascii_art(selected_file_path, block_size, line_detection)

            # Display ASCII art in the preview widget
            preview_widget.delete("1.0", tk.END)  # Clear previous content
            preview_widget.insert(tk.END, ascii_art)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process file: {e}")
    else:
        messagebox.showwarning("No File Selected", "Please select an image file first.")

def save_art(preview_widget):
    """Function to save the generated ASCII art to a file."""
    # Get the content of the preview widget
    ascii_art = preview_widget.get("1.0", tk.END).strip()
    
    if ascii_art:  # Ensure there is ASCII art to save
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                # Save ASCII art to the file
                BackEnd.save_ascii_art(ascii_art, file_path)
                messagebox.showinfo("Save", "ASCII Art saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save ASCII art: {e}")
        else:
            messagebox.showwarning("Save Cancelled", "Save operation was cancelled.")
    else:
        messagebox.showwarning("No Art to Save", "There is no ASCII art to save. Please generate art first.")

def create_main():
    """Function to create the main window."""
    main_window = tk.Tk()
    main_window.title("Settings for your generation!")
    main_window.geometry("800x600")
    main_window.configure(bg="#f0f0f0")

    # Variables
    font_size_var = tk.IntVar(value=12)
    block_size_var = tk.IntVar(value=9)
    line_detection = tk.BooleanVar()

    # Top frame for settings
    settings_frame = tk.Frame(main_window)
    settings_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Button to select an image
    select_image_button = tk.Button(
        settings_frame,
        text="Select Image",
        font=("Rockabilly", 10),
        command=lambda: select_image(preview_widget),
        width=20,
        height=2
    )
    select_image_button.grid(row=0, column=0, padx=5, pady=5)

    # Button to generate ASCII art
    generate_art_button = tk.Button(
        settings_frame,
        text="Generate Artwork",
        font=("Rockabilly", 10),
        command=lambda: generate_art(
            preview_widget,
            font_size_var.get(),
            block_size_var.get(),
            line_detection.get()
        ),
        width=20,
        height=2
    )
    generate_art_button.grid(row=0, column=1, padx=5, pady=5)

    # Block size scale
    block_size_scale = tk.Scale(
        settings_frame,
        from_=1,
        to_=20,
        orient=tk.HORIZONTAL,
        variable=block_size_var,
        label="Block Size (Pixels per Character)"
    )
    block_size_scale.grid(row=1, column=0, padx=5, pady=5)

    # Font size scale
    font_size_scale = tk.Scale(
        settings_frame,
        from_=5,
        to_=30,
        orient=tk.HORIZONTAL,
        variable=font_size_var,
        label="Font Size"
    )
    font_size_scale.grid(row=1, column=1, padx=5, pady=5)

    # Line detection checkbox
    LineDetection_box = tk.Checkbutton(
        settings_frame,
        text='Line Detection (Edge Detection)',
        variable=line_detection,
        onvalue=True,
        offvalue=False,
    )
    LineDetection_box.grid(row=2, column=0, columnspan=2, pady=5)

    # Frame for preview widget
    preview_frame = tk.Frame(main_window)
    preview_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Preview widget
    preview_widget = tk.Text(
        preview_frame,
        wrap=tk.WORD,
        font=("Courier", font_size_var.get()),
        bg="#ffffff",
        fg="#000000"
    )
    preview_widget.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    # Scrollbar for preview widget
    scrollbar = tk.Scrollbar(preview_frame, command=preview_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    preview_widget.config(yscrollcommand=scrollbar.set)

    # Insert initial message in preview widget
    preview_widget.insert(tk.END, "Preview of ASCII art will appear here after generation.")

    # Save ASCII art button
    save_button = tk.Button(
        main_window,
        text="Save ASCII Art",
        font=("Rockabilly", 10),
        command=lambda: save_art(preview_widget),
        width=20,
        height=2
    )
    save_button.pack(pady=10)

    # Function to handle mouse wheel event for zoom
    def mouse_wheel(event):
        if event.state & 0x1:  # If Shift key is held (event.state & 0x1 means Shift)
            new_size = font_size_var.get() + (1 if event.delta > 0 else -1)
            if 5 <= new_size <= 30:  # Restrict font size range
                font_size_var.set(new_size)
                preview_widget.config(font=("Courier", font_size_var.get()))
        else:
            # Scroll the text widget
            preview_widget.yview_scroll(-1 * (event.delta // 120), "units")

    # Bind mouse wheel for zooming and scrolling
    main_window.bind("<MouseWheel>", mouse_wheel)

    return main_window

# Create and display the main window
main_window = create_main()
main_window.mainloop()
