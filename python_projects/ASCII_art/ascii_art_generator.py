from PIL import Image
import tkinter as tk
from tkinter import filedialog
import cv2, os, time
import numpy as np

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

# Function to get the Mp4 video path
def get_video_path():
    """Gets a Mp4 File Path When Button Pressed \n
    -----------------------------------------------------------------------------\n
    Keyword Arguments: \n
    None \n
    -----------------------------------------------------------------------------\n
    Variables: \n
    selected_file_path -- Imports the global empty string so we can assign a value \n
    selected_output_path -- Imports the global empty string so we can assign a value \n
    -----------------------------------------------------------------------------\n
    Overview: \n
    Function opens x2 file browsers windows using filedialog 1st to be displayed is to get the video path, \n
    second will get a Jpeg Dump folder
    """
    global selected_file_path, selected_output_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Mp4 Files", "*.mp4;")])
    selected_output_path = filedialog.askdirectory()

# Function to set the file path
def get_image_path():
    """Gets the Jpeg image path \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
        None \n
        -----------------------------------------------------------------------------\n
        Variables: \n
        selected_file_path -- Imports the global empty string so we can assign a value \n
        -----------------------------------------------------------------------------\n
        Overview: \n
        Function opens a file browser using filedialog \n
    """
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

# Function to open the file and display ASCII art
def open_file(font_size_var):
    """Brief overview \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
        font_size_var -- used within the ASCII label to use the font size selected within the slider. \n
        -----------------------------------------------------------------------------\n
        Variables: \n
        selected_file_path -- Imports the global empty string so we can assign a value \n
        rows -- within this function the global TK variable rows (if y % 1 == 0:) is used to send data to the get ascii_art function \n
        columns -- within this function the global TK variable columns (if x % 1 == 0:) is used to send data to the get ascii_art function \n
        ascii_window -- used to create a window object within tkinter \n
        ascii_label -- creates a label object within tkinter \n
        ascii_art -- stores a string variable returned from get_ascii_art \n
        -----------------------------------------------------------------------------\n
        Overview: \n
        Function first imports the global variables (selected_file_path, rows, columns) \n
        It then enters a if loop for the selected_file_path and creates a new TKinter window titled ASCII Art \n
        Then it sets ascii_art = to the return of get_ascii_art with selected file_path, rows.get() and columns.get() as arguments \n
        .get() is used to use the values returned from the scale slider in the main GUI window \n
        Function then creates a new TKinter label to display the string variable (displaying the art) in the new window \n
    """
    global selected_file_path, rows, columns
    if selected_file_path:
        ascii_window = tk.Tk()
        ascii_window.title("ASCII Art")
        ascii_window.geometry("500x300")
        ascii_window.configure(bg="#f0f0f0")

        ascii_art = get_ascii_art(selected_file_path, rows.get(), columns.get(), line_detection.get())
        ascii_label = tk.Label(
            ascii_window,
            text=ascii_art,
            font=("Courier New", font_size_var),
            bg="#f0f0f0",
            justify="left"
        )
        ascii_label.pack(pady=5, padx=5)
        ascii_window.mainloop()

def edge_detection(image):
    """Edge detection using Sobel operator \n
    -----------------------------------------------------------------------------\n
    Keyword Arguments: \n
    image -- input image \n
    -----------------------------------------------------------------------------\n
    Variables: \n
    gray_image -- grayscale image \n
    blurred_image -- blurred image \n
    sobel_x -- Sobel operator on x-axis \n
    sobel_y -- Sobel operator on y-axis \n
    gradient_magnitude -- gradient magnitude of Sobel operator \n
    -----------------------------------------------------------------------------\n
    Overview: \n
    Function converts image to grayscale, applies Gaussian blur, applies Sobel operator, computes gradient magnitude, normalizes it, and returns gradient magnitude image \n
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    sobel_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    gradient_magnitude *= 255.0 / gradient_magnitude.max()
    gradient_magnitude = np.uint8(gradient_magnitude)
    return gradient_magnitude

# Function to generate ASCII art
def get_ascii_art(image_path, rows, columns, line_detection):
    """Reads a Jpeg and converts it to ASCII art \n
    ----------------------------------------------------------------------------- \n
    Keyword Arguments: \n
    image_path -- the path to the file we are going to convert \n
    rows -- Sets how many rows we should read using x % rows to vary \n
    columns -- Sets how many columns we should read using y % columns to vary \n
    ----------------------------------------------------------------------------- \n
    Variables: \n
    img -- The image \n
    Pixels -- pixel data from img.load() \n
    Width -- The amount of pixels in each row \n
    height -- The amount of pixels in each column \n
    ascii_art -- variable to store the converted image \n
    min_brightness -- sets the minimum brightness value in our range \n
    max_brightness -- sets the maximum brightness value in our range \n
    ----------------------------------------------------------------------------- \n
    Overview: \n
    Function takes an image, stores it as img variable. \n
    Function then converts image to greyscale and loads pixel data. \n
    Function then gets the Image width and height and creates an empty string variable and 2 integers variables \n
    Set the min the to height value and the max to the lowest value as when we iterate though we will call min() and max() on them \n
    \n
    Function now begins to create the Art the For loop first says every time we encounter a new Y value the string needs to print a new line \n
    Next for loop takes the value for brightness and maps each value to a index value inbetween the Len() of how every many characters we are using \n
    Finally the loop append the ASCII character to the ascii_art variable and returns the string after the loop.
    """
    if line_detection:
        image = cv2.imread(image_path)
        img = edge_detection(image)
        img = Image.fromarray(img)
    else:
        img = Image.open(image_path)

    img = img.convert("L")
    pixels = img.load()
    width, height = img.size
    ascii_art = ""
    min_brightness = 256
    max_brightness = 0

    for y in range(height):
        for x in range(width):
            brightness = pixels[x, y]
            min_brightness = min(brightness, min_brightness)
            max_brightness = max(brightness, max_brightness)

    for y in range(height):
        if y % rows == 0:
            ascii_art += "\n"
            for x in range(width):
                if x % columns == 0:
                    brightness = pixels[x, y]
                    brightness_index = int(((brightness - min_brightness) / (max_brightness - min_brightness)) * (len(ascii_characters_by_density) - 1))
                    ascii_art += ascii_characters_by_density[brightness_index]
    return ascii_art

# Function to convert MP4 to ASCII art frames
def mp4_to_jpeg():
    """Read the mp4 convert each frame into a jpeg and then ASCII, deletes the jpeg and stores the ascii \n
    -----------------------------------------------------------------------------\n
    Keyword Arguments: \n
     None \n
    -----------------------------------------------------------------------------\n
    Variables: \n
     selected_file_path -- Imports the global empty string so we can assign a value \n
     selected_output_path -- Imports the global empty string so we can assign a value \n
     variable -- explination \n
     variable -- explination \n
     variable -- explination \n
     variable -- explination \n
     variable -- explination \n
     variable -- explination \n
     variable -- explination \n
    -----------------------------------------------------------------------------\n
    Overview: \n
     Detail function behaviour \n
    """
    global selected_file_path, selected_output_path
    cap = cv2.VideoCapture(selected_file_path)
    frame_count = 0
    ascii_art_list = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if line_detection.get():
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Ensure frame is grayscale before edge detection
            frame = edge_detection(frame)
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        img = Image.fromarray(frame)
        ascii_art = get_ascii_art_from_frame(img, rows.get(), columns.get())
        ascii_art_list.append(ascii_art)
        frame_count += 1

    cap.release()
    jpeg_to_string(ascii_art_list)

# Function to generate ASCII art from a frame
def get_ascii_art_from_frame(img, rows, columns):
    pixels = img.load()
    width, height = img.size
    ascii_art = ""
    min_brightness = 256
    max_brightness = 0

    for y in range(height):
        for x in range(width):
            brightness = pixels[x, y]
            min_brightness = min(brightness, min_brightness)
            max_brightness = max(brightness, max_brightness)

    for y in range(height):
        if y % rows == 0:
            ascii_art += "\n"
            for x in range(width):
                if x % columns == 0:
                    brightness = pixels[x, y]
                    brightness_index = int(((brightness - min_brightness) / (max_brightness - min_brightness)) * (len(ascii_characters_by_density) - 1))
                    ascii_art += ascii_characters_by_density[brightness_index]
    return ascii_art

def play_video(ascii_label, ascii_art_list):
    i = 0
    while True:
        time.sleep(0.03334)
        ascii_label.config(text=ascii_art_list[i])
        ascii_label.update()
        i = (i + 1) % len(ascii_art_list)

def jpeg_to_string(ascii_art_list):
    ascii_video_window = tk.Tk()
    ascii_video_window.title("ASCII Art")
    ascii_video_window.geometry("1000x600")
    ascii_video_window.configure(bg="#f0f0f0")

    font_size = font_size_var.get()
    ascii_label = tk.Label(
        ascii_video_window,
        text=ascii_art_list[0],
        font=("Courier New", font_size),
        bg="#f0f0f0",
        justify="left"
    )
    ascii_label.grid(row=0, column=9, pady=5, padx=5)

    play_video_button = tk.Button(
        ascii_video_window,
        text="Play Video",
        font=("Rockabilly", 10),
        command=lambda: play_video(ascii_label, ascii_art_list),
        width=20,
        height=2
    )
    play_video_button.grid(row=0, column=10, pady=20, padx=10)

    ascii_video_window.mainloop()

def create_main(open_file_command, mp4_to_jpeg_command, get_image_path_command, get_video_path_command):
    """Brief overview \n
        -----------------------------------------------------------------------------\n
        Keyword Arguments: \n
        keyword -- explination \n
        -----------------------------------------------------------------------------\n
        Variables: \n
        variable -- explination \n
        -----------------------------------------------------------------------------\n
        Overview: \n
        Detail function behaviour \n
    """
    main_window = tk.Tk()
    main_window.title("Settings for your generation!")
    main_window.geometry("400x600")
    main_window.configure(bg="#f0f0f0")

    get_art_button = tk.Button(
        main_window,
        text="Generate artwork",
        font=("Rockabilly", 10),
        command=lambda: open_file_command(font_size_var.get()),
        width=20,
        height=2
    )
    get_art_button.pack(pady=10)

    get_video_button = tk.Button(
        main_window,
        text="Generate ASCII video",
        font=("Rockabilly", 10),
        command=mp4_to_jpeg_command,
        width=20,
        height=2
    )
    get_video_button.pack(pady=20)

    get_image_path_button = tk.Button(
        main_window,
        text="Select image",
        font=("Rockabilly", 10),
        command=get_image_path_command,
        width=20,
        height=2
    )
    get_image_path_button.pack(pady=10)

    get_video_path_button = tk.Button(
        main_window,
        text="Select Mp4",
        font=("Rockabilly", 10),
        command=get_video_path_command,
        width=20,
        height=2
    )
    get_video_path_button.pack(pady=20)

    global font_size_var, rows, columns, line_detection
    font_size_var = tk.IntVar(value=1)
    rows = tk.IntVar(value=1)
    columns = tk.IntVar(value=1)
    line_detection = tk.IntVar()

    font_size_scale = tk.Scale(
        main_window,
        from_=1,
        to=20,
        orient=tk.HORIZONTAL,
        variable=font_size_var,
        label="Font Size"
    )
    font_size_scale.pack(pady=10)

    rows_scale = tk.Scale(
        main_window,
        from_=1,
        to=10,
        orient=tk.HORIZONTAL,
        variable=rows,
        label="Adjust Y Scaling"
    )
    rows_scale.pack(pady=10)

    columns_scale = tk.Scale(
        main_window,
        from_=1,
        to=10,
        orient=tk.HORIZONTAL,
        variable=columns,
        label="Adjust X Scaling"
    )
    columns_scale.pack(pady=10)

    LineDetection_box = tk.Checkbutton(
        main_window,
        text='Line Detection?(untick for mp4)',
        variable=line_detection,
        onvalue=True,
        offvalue=False,
    )
    LineDetection_box.pack(pady=10)

    return main_window

main_window = create_main(open_file, mp4_to_jpeg, get_image_path, get_video_path)
main_window.mainloop()