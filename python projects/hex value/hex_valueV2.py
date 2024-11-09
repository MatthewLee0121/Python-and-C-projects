import pyautogui
import tkinter as tk
import pyperclip

# Global variable to store the hexadecimal value of the colour at the pointer
current_hex_value = "#4CAF50"

# Function to get the hexadecimal value of the colour at the current mouse pointer position
def get_pixel_hex_values():
    try:
        x, y = pyautogui.position()
        pixel_values = [
            pyautogui.pixel(x - 1, y + 1),
            pyautogui.pixel(x, y + 1),
            pyautogui.pixel(x + 1, y + 1),
            pyautogui.pixel(x - 1, y),
            pyautogui.pixel(x, y),
            pyautogui.pixel(x + 1, y),
            pyautogui.pixel(x - 1, y + 1),
            pyautogui.pixel(x, y + 1),
            pyautogui.pixel(x + 1, y + 1),
        ]
        
        hex_values = [
            "#{:02x}{:02x}{:02x}".format(*pixel_value) for pixel_value in pixel_values
        ]

        return hex_values

    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to update the label displaying the colour at the pointer
def update_colour_label():
    global current_hex_value
    hex_values = get_pixel_hex_values()
    if hex_values:
        current_hex_value = hex_values[4]  # Access the value at index 4
        colour_label.config(text=f'The colour at the pointer is: {current_hex_value}')
        window.configure(bg=current_hex_value)

# Function to copy the colour hex value to the clipboard
def copy_to_clipboard():
    global current_hex_value
    if current_hex_value:
        pyperclip.copy(current_hex_value)

# Create a themed Tkinter window
window = tk.Tk()
window.title("Colour at Pointer Codingwithbeans")

# Set window size and background colour
window.geometry("500x300")  # Adjusted resolution
window.configure(bg="#f0f0f0")

# Create a label for displaying the colour at the pointer
colour_label = tk.Label(
    window,
    text="Move your pointer to get the colour.",
    font=("Helvetica", 14),
    bg="#f0f0f0",
)
colour_label.pack(pady=20)

# Create a styled button to close the window
close_button = tk.Button(
    window,
    text="Close",
    command=window.destroy,
    font=("Helvetica", 12),
    bg="#4CAF50",  # Green colour
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
)
close_button.pack(pady=5)

# Create a styled button to copy hex value to clipboard
copy_button = tk.Button(
    window,
    text="Copy to Clipboard",
    command=copy_to_clipboard,
    font=("Helvetica", 12),
    bg="#008CBA",  # Blue colour
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
)
copy_button.pack(pady=5)

# Bind 'r' key to refresh_colour function
window.bind('r', lambda event: update_colour_label())

# Run the function to update the colour label once
update_colour_label()

# Start the Tkinter main loop
window.mainloop()
