from PIL import Image  ##used to read Jpeg
import tkinter as tk   #Used for GUI
from tkinter import filedialog #makes selecting files easier
import numpy as np
import cv2


# ASCII characters arranged by rough density
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


def get_image_path():

    selected_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]) #i honestly dont know how this works thank you internet u the real MPV

    return selected_file_path


    # Function to open the file and display ASCII art
def open_file(selected_file_path):
    if selected_file_path:  # Check if a file path is selected
        # Create a themed Tkinter window for displaying ASCII art
        ascii_window = tk.Tk() #creates the window
        ascii_window.title("ASCII Art") #sets new window title
        
        # Set window size and background color
        ascii_window.geometry("500x300")
        ascii_window.configure(bg="#f0f0f0") #white cos we in testing
        
        # Get ASCII art from the selected image
        ascii_art = get_ascii_art(selected_file_path, rows.get(), columns.get(), line_detection.get())
        
        # Create a label for displaying the ASCII art
        ascii_label = tk.Label(
            ascii_window,
            text=ascii_art,
            font=("Courier New", font_size_var),  # Adjust font size and font family as needed #make this into a setting so i dont need to keep re running app to modify
            bg="#f0f0f0",
            justify="left"  # Adjust justification as needed
        )
        ascii_label.pack(pady=5, padx =5) # gives us 5 pixels

        ascii_window.mainloop()


    # Function to generate art
def get_ascii_art(image_path, rows, columns, line_detection):

    if line_detection == True:
        image = cv2.imread(image_path)
        img = edge_detection(image)
        img = Image.fromarray(img)

    else:
        img = Image.open(image_path)

    # Convert the image to grayscale mode
    img = img.convert("L")

    # Get pixel data
    pixels = img.load()

    # Get the size of the image
    width, height = img.size
    #sets empty string variable
    ascii_art = ""
    min_brightness = 256 #max brighness for jpeg is 255
    max_brightness = 0 #min brightness on jpeg is 0
    #had to make 2 forloops for dynamic brightness values 
    for y in range(height):
        if y % 1 == 0:  #can be modified to exclude data not recommended unless you need to try reduce the minimum and maximum values some with the dynamic brightness index will be a more optimised version
            for x in range(width):
                if x % 1 == 0: #can be modified to exclude data not recommended unless you need to try reduce the minimum and maximum values some with the dynamic brightness index will be a more optimised version
                    brightness = pixels[x, y]
                    min_brightness = min(brightness, min_brightness)#This for loop will get me minimum and max brightness values from the range of data within the pixels
                    max_brightness = max(brightness, max_brightness)# can then utalise this information in the next for loop to dynamically set ASCII characters
    
    for y in range(height):
        if y % rows == 0: #if i change this it will exclude the height row % 3 will take every 3rd row ETC
            ascii_art += "\n" #adds a new line to the string whenever we hit a new Y coordinate char
            for x in range(width):
                if x % columns == 0: #if i change this it will exclude the width row % 3 will take every 3rd row ETC
                    # converted image to greyscale with (img = img.convert("L")) this means we no longer have to work on RGB channels and only work on brightness values
                    brightness = pixels[x, y]
                    # Calculate the brightness index in a dynamic way so every image has different brightness values, this calculates the range and gets us representative values convert to int to get approimation we can only have 155 values as a max
                    brightness_index = int(((brightness - min_brightness) / (max_brightness - min_brightness)) * (len(ascii_characters_by_density) - 1))
                    # Append the corresponding ASCII character to the ASCII art string
                    ascii_art += ascii_characters_by_density[brightness_index]
    #returns completed string
    return ascii_art
