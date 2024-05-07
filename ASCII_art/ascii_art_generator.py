from PIL import Image
import tkinter as tk
from tkinter import filedialog
import cv2
import os
import time
import Pmw


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

def get_video_path():
    """Gets a Mp4 File Path When Button Pressed."""
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Mp4 Files", "*.mp4;")])

def get_image_path():
    """Gets the Jpeg image path."""
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])

def open_file(font_size_var):
    """Opens the selected file and displays ASCII art."""
    global selected_file_path
    if selected_file_path:
        ascii_art = get_ascii_art(selected_file_path, rows.get(), columns.get())
        display_ascii_art(ascii_art, font_size_var, zoom_var)

def get_ascii_art(image_path, rows, columns):
    """Converts an image to ASCII art."""
    img = Image.open(image_path).convert("L")
    pixels = img.load()
    width, height = img.size
    ascii_art = ""
    min_brightness = 256
    max_brightness = 0

    for y in range(height):
        if y % rows == 0:
            for x in range(width):
                if x % columns == 0:
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

def display_ascii_art(ascii_art, font_size_var, zoom_var):
    """Displays ASCII art in a new window with zoom functionality."""
    ascii_window = tk.Tk()
    ascii_window.title("ASCII Art")
    ascii_window.geometry("500x300")
    ascii_window.configure(bg="#f0f0f0")

    frame = tk.Frame(ascii_window)
    frame.pack(fill=tk.BOTH, expand=tk.YES)

    canvas = Pmw.ScrolledCanvas(frame, borderframe=1, labelpos='n',
                                 hscrollmode='dynamic', vscrollmode='dynamic',
                                 usehullsize=1, hull_width=200, hull_height=200)
    canvas.pack(expand=True, fill='both')

    text = tk.Text(canvas.interior(), font=("Courier New", font_size_var), wrap='none')
    text.pack(expand=True, fill='both')
    text.insert(tk.END, ascii_art)

    def zoom_text(event):
        font_size = text.cget("font")
        size = int(font_size.split(" ")[1])
        if event.delta < 0 and size > 6:
            size -= 1
        elif event.delta > 0 and size < 30:
            size += 1
        text.config(font=("Courier New", size))

    text.bind("<MouseWheel>", zoom_text)

    ascii_window.mainloop()

def mp4_to_ascii():
    """Reads the mp4 file, converts each frame to ASCII, and stores them in memory."""
    global selected_file_path
    cap = cv2.VideoCapture(selected_file_path)
    ascii_art_list = []

    while True:
        try:
            ret, frame = cap.read()
            if not ret:
                print("End of video or error has occurred")
                break

            ascii_art = get_ascii_art_from_frame(frame, rows.get(), columns.get())
            ascii_art_list.append(ascii_art)

        except Exception as e:
            print("Error:", e)

    cap.release()
    display_ascii_video(ascii_art_list)

def get_ascii_art_from_frame(frame, rows, columns):
    """Converts a frame to ASCII art."""
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ascii_art = get_ascii_art(gray_frame, rows, columns)
    return ascii_art

def display_ascii_video(ascii_art_list, zoom_var):
    """Displays the ASCII art video."""
    ascii_video_window = tk.Tk()
    ascii_video_window.title("ASCII Art Video")
    ascii_video_window.geometry("800x600")

    frame = tk.Frame(ascii_video_window)
    frame.pack(fill=tk.BOTH, expand=tk.YES)

    canvas = Pmw.ScrolledCanvas(frame, borderframe=1, labelpos='n',
                                 hscrollmode='dynamic', vscrollmode='dynamic',
                                 usehullsize=1, hull_width=200, hull_height=200)
    canvas.pack(expand=True, fill='both')

    text = tk.Text(canvas.interior(), font=("Courier New", 8), wrap='none')
    text.pack(expand=True, fill='both')

    def update_label():
        nonlocal text, ascii_art_list
        for ascii_art in ascii_art_list:
            text.delete(1.0, tk.END)
            text.insert(tk.END, ascii_art)
            ascii_video_window.update()
            time.sleep(0.05)

    update_label()
    ascii_video_window.mainloop()

def create_main():
    """Creates the main GUI window."""
    main_window = tk.Tk()
    main_window.title("Settings for your generation!")
    main_window.geometry("400x600")
    main_window.configure(bg="#f0f0f0")


    get_art_button = tk.Button(
        main_window,
        text="Generate artwork",
        font=("Rockabilly", 10),
        command=lambda: open_file(font_size_var.get()),
        width=20,
        height=2
    )
    get_art_button.pack(pady=10)

    get_video_button = tk.Button(
        main_window,
        text="Generate ASCII video",
        font=("Rockabilly", 10),
        command=mp4_to_ascii,
        width=20,
        height=2
    )
    get_video_button.pack(pady=20)

    get_image_path_button = tk.Button(
        main_window,
        text="Select image",
        font=("Rockabilly", 10),
        command=get_image_path,
        width=20,
        height=2
    )
    get_image_path_button.pack(pady=10)

    get_video_path_button = tk.Button(
        main_window,
        text="Select Mp4",
        font=("Rockabilly", 10),
        command=get_video_path,
        width=20,
        height=2
    )
    get_video_path_button.pack(pady=20)

    font_size_var = tk.IntVar(value=1)
    global rows
    rows = tk.IntVar(value=1)
    global columns
    columns = tk.IntVar(value=1)
    global zoom_var
    zoom_var = tk.IntVar(value=1)

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

    zoom_scale = tk.Scale(
        main_window,
        from_=1,
        to=5,
        orient=tk.HORIZONTAL,
        variable=zoom_var,
        label="Zoom"
    )
    zoom_scale.pack(pady=10)

    main_window.mainloop()

create_main()

