#convert jpegs image to ascii version of jpeg image.

#imports from pillow jpeg library
from PIL import Image
from math import floor
import pyautogui
import tkinter as tk
import pyperclip

# Define ASCII characters arranged by perceived density
ascii_characters_by_density = [
    " ", ".", ",", ":", ";", "i", "!", "|", "1", "t", "f", "L", "I", "(", ")", "[", "]", "{", "}", "r", "c",
    "*", "+", "=", "7", "?", "v", "x", "J", "3", "n", "o", "s", "z", "5", "2", "S", "F", "C", "Z", "U", "O",
    "0", "Q", "8", "9", "V", "Y", "X", "G", "q", "m", "w", "p", "d", "A", "D", "H", "#", "M", "B", "&", "W",
    "E", "%", "6", "k", "R", "P", "N", "T", "4", "K", "E", "U", "h", "y", "b", "g", "j", "@", "^", "a", "u",
    "e", "l", "I", "T", "q", "H", "D", "W", "M", "B", "Q", "G", "N", "O", "Z", "S", "C", "V", "X", "Y", "K",
    "A", "0", "9", "8", "Q", "O", "Z", "C", "V", "S", "X", "Y", "N", "K", "M", "G", "B", "W", "H", "D", "Q",
    "E", "U", "T", "l", "y", "u", "a", "^", "@", "j", "g", "b", "y", "h", "U", "K", "4", "T", "N", "P", "R",
    "k", "6", "%", "E", "W", "B", "M", "#"
]

# print(len(ascii_characters_by_density))    #155

# Load the image
image_path = r"C:\Users\mat_m\OneDrive\Pictures\Screenshot 2024-02-12 203655.jpg"
#sets img variable = to the opened jpeg image
img = Image.open(image_path)

# Convert the image to grayscale mode
img = img.convert("L")

# Get pixel data
pixels = img.load()

# Get the size of the image
width, height = img.size

# Create a list to store pixel information
# Create a list to store brightness values for later ASCII conversions
brightness_list = []

# Iterate through each pixel and store its information in the list
def get_art(brightness_list):
    global ascii_characters_by_density
    global width, height
    for y in range(height):
        print("")
        for x in range(width):

            # For grayscale images, there's only one value representing intensity/brightness

            brightness = pixels[x, y]
            brightness_list.append(brightness)
            min_brightness = min(brightness_list)
            max_brightness = max(brightness_list)
            #155 ASCI characters 
            brightness = floor((brightness / 266) * len(ascii_characters_by_density))
            ascii_char = ascii_characters_by_density[brightness]
            print(ascii_char, end="")
            #append to lists for later data manipulation
            
            #append to list of brightness
            


#combine brightness values to ASCII
 # Create a themed Tkinter window
window = tk.Tk()
window.title("Colour at Pointer Codingwithbeans")

# Set window size and background colour
window.geometry("500x300")  # Adjusted resolution
window.configure(bg="#f0f0f0")
 # Create a label for displaying the colour at the pointer
colour_label = tk.Label(
    window,
    text=get_art(),
    font=("Helvetica", 14),
    bg="#f0f0f0",
)
colour_label.pack(pady=20)
window.mainloop()

#print(brightness_list)
#print(brightness_ascii_dict)

# Print the range of brightness
print(f"Range of brightness: {min_brightness} to {max_brightness}") #--> 1 to 266
# 1 to 266 is my range of brightness my ASCII list is 155 so need to iterate throught all of the list and (% 155 + 1) to the list
#can add this to the above for loop

# for y in range(height):
#     for x in range(width):
# r, g, b = pixels[x, y]
#         pixel_hex = f"#{r:02x}{g:02x}{b:02x}"_
#         pixel_info.append([[x, y], pixel_hex]) # for convert rgb


# import pyautogui
# import tkinter as tk
# import pyperclip

# # Global variable to store the hexadecimal value of the colour at the pointer
# current_hex_value = "#4CAF50"

# # Function to get the hexadecimal value of the colour at the current mouse pointer position
# def get_pixel_hex_values():
#     try:
#         x, y = pyautogui.position()
#         pixel_values = [
#             pyautogui.pixel(x - 1, y + 1),
#             pyautogui.pixel(x, y + 1),
#             pyautogui.pixel(x + 1, y + 1),
#             pyautogui.pixel(x - 1, y),
#             pyautogui.pixel(x, y),
#             pyautogui.pixel(x + 1, y),
#             pyautogui.pixel(x - 1, y + 1),
#             pyautogui.pixel(x, y + 1),
#             pyautogui.pixel(x + 1, y + 1),
#         ]
        
#         hex_values = [
#             "#{:02x}{:02x}{:02x}".format(*pixel_value) for pixel_value in pixel_values
#         ]

#         return hex_values

#     except Exception as e:
#         print(f"Error: {e}")
#         return None

# # Function to update the label displaying the colour at the pointer
# def update_colour_label():
#     global current_hex_value
#     hex_values = get_pixel_hex_values()
#     if hex_values:
#         current_hex_value = hex_values[4]  # Access the value at index 4
#         colour_label.config(text=f'The colour at the pointer is: {current_hex_value}')
#         window.configure(bg=current_hex_value)

# # Function to copy the colour hex value to the clipboard
# def copy_to_clipboard():
#     global current_hex_value
#     if current_hex_value:
#         pyperclip.copy(current_hex_value)

# # Create a themed Tkinter window
# window = tk.Tk()
# window.title("Colour at Pointer Codingwithbeans")

# # Set window size and background colour
# window.geometry("500x300")  # Adjusted resolution
# window.configure(bg="#f0f0f0")

# # Create a label for displaying the colour at the pointer
# colour_label = tk.Label(
#     window,
#     text="Move your pointer to get the colour.",
#     font=("Helvetica", 14),
#     bg="#f0f0f0",
# )
# colour_label.pack(pady=20)

# # Create a styled button to close the window
# close_button = tk.Button(
#     window,
#     text="Close",
#     command=window.destroy,
#     font=("Helvetica", 12),
#     bg="#4CAF50",  # Green colour
#     fg="white",
#     padx=10,
#     pady=5,
#     relief="flat",
# )
# close_button.pack(pady=5)

# # Create a styled button to copy hex value to clipboard
# copy_button = tk.Button(
#     window,
#     text="Copy to Clipboard",
#     command=copy_to_clipboard,
#     font=("Helvetica", 12),
#     bg="#008CBA",  # Blue colour
#     fg="white",
#     padx=10,
#     pady=5,
#     relief="flat",
# )
# copy_button.pack(pady=5)

# # Bind 'r' key to refresh_colour function
# window.bind('r', lambda event: update_colour_label())

# # Run the function to update the colour label once
# update_colour_label()

# # Start the Tkinter main loop
# window.mainloop()
