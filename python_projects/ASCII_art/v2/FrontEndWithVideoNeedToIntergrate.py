import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for progress bar
import cv2
import numpy as np
from PIL import Image
import time
import os
import BackEndV  # Assuming the backend code is in a module named BackEndV

# Global variables to store selected file and frames list
selected_video_path = None
ascii_frames = []

def select_video(preview_widget):
    """Function to select an MP4 file."""
    global selected_video_path
    selected_video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    if selected_video_path:
        messagebox.showinfo("Video Selected", f"Selected file: {selected_video_path}")
        preview_widget.delete("1.0", tk.END)  # Clear preview widget
        preview_widget.insert(tk.END, "Video selected. Ready to generate ASCII art!")
    else:
        messagebox.showwarning("No File Selected", "Please select a video file.")

def generate_ascii_for_video(preview_widget, block_size, line_detection, progress_bar):
    """Function to generate ASCII art for each frame in the video."""
    global selected_video_path, ascii_frames

    if selected_video_path:
        try:
            # Open the video file
            video_capture = cv2.VideoCapture(selected_video_path)
            if not video_capture.isOpened():
                raise RuntimeError(f"Failed to open video file: {selected_video_path}")

            # Clear the frames list
            ascii_frames = []
            
            # Get the total number of frames in the video
            total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
            progress_bar['maximum'] = total_frames  # Set the maximum value of progress bar
            progress_bar['value'] = 0  # Start with the value at 0

            while video_capture.isOpened():
                ret, frame = video_capture.read()
                if not ret:
                    break  # End of video

                # Convert frame to ASCII art
                frame_ascii = process_frame_to_ascii(frame, block_size, line_detection)
                ascii_frames.append(frame_ascii)

                # Update the progress bar
                progress_bar['value'] += 1
                progress_bar.update()  # Update progress bar

            # Display the first frame in the preview widget
            preview_widget.delete("1.0", tk.END)  # Clear previous content
            preview_widget.insert(tk.END, ascii_frames[0])

            # Close the video capture
            video_capture.release()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process video: {e}")
            print("Error", f"Failed to process video: {e}")
    else:
        messagebox.showwarning("No File Selected", "Please select a video file first.")

def process_frame_to_ascii(frame, block_size, line_detection):
    """Convert a video frame to ASCII art."""
    if line_detection:
        frame = BackEndV.edge_detection(frame)  # Apply edge detection if required

    # Convert the frame to grayscale if it's not already
    if len(frame.shape) == 3:  # Check if frame has 3 channels (BGR/RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate new dimensions based on the block size
    height, width = frame.shape
    new_width = width // block_size
    new_height = height // block_size

    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Generate ASCII art from the frame
    ascii_art = ""
    for y in range(new_height):
        for x in range(new_width):
            brightness = resized_frame[y, x]
            char_index = int((brightness / 255) * (len(BackEndV.ascii_characters_by_density) - 1))
            ascii_art += BackEndV.ascii_characters_by_density[char_index]
        ascii_art += "\n"

    return ascii_art

def play_video(preview_widget):
    """Function to play the generated ASCII art as a video."""
    global ascii_frames

    if not ascii_frames:
        messagebox.showwarning("No Frames", "No frames to display. Please generate ASCII art first.")
        return

    try:
        # Play each frame with a delay to simulate video
        for frame in ascii_frames:
            preview_widget.delete("1.0", tk.END)  # Clear previous content
            preview_widget.insert(tk.END, frame)
            preview_widget.update()  # Update the widget
            time.sleep(0.1)  # 10 frames per second (adjust as needed)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to play video: {e}")

def save_art(preview_widget):
    """Function to save the generated ASCII art to a file."""
    # Get the content of the preview widget
    ascii_art = preview_widget.get("1.0", tk.END).strip()
    
    if ascii_art:  # Ensure there is ASCII art to save
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                # Save ASCII art to the file
                BackEndV.save_ascii_art(ascii_art, file_path)
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
    block_size_var = tk.IntVar(value=9)
    line_detection = tk.BooleanVar()
    current_font_size = tk.IntVar(value=12)  # Initial font size

    # Top frame for settings
    settings_frame = tk.Frame(main_window)
    settings_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    # Button to select a video
    select_video_button = tk.Button(
        settings_frame,
        text="Select Video",
        font=("Rockabilly", 10),
        command=lambda: select_video(preview_widget),
        width=20,
        height=2
    )
    select_video_button.grid(row=0, column=0, padx=5, pady=5)

    # Button to generate ASCII art for the video
    generate_art_button = tk.Button(
        settings_frame,
        text="Generate ASCII Art",
        font=("Rockabilly", 10),
        command=lambda: generate_ascii_for_video(
            preview_widget,
            block_size_var.get(),
            line_detection.get(),
            progress_bar  # Pass progress bar
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

    # Preview widget for displaying ASCII art frames
    preview_widget = tk.Text(
        preview_frame,
        wrap=tk.WORD,
        font=("Courier", current_font_size.get()),
        bg="#ffffff",
        fg="#000000"
    )
    preview_widget.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    # Scrollbar for preview widget
    scrollbar = tk.Scrollbar(preview_frame, command=preview_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    preview_widget.config(yscrollcommand=scrollbar.set)

    # Progress bar for video processing
    progress_bar = ttk.Progressbar(
        settings_frame,
        orient=tk.HORIZONTAL,
        length=200,
        mode="determinate"
    )
    progress_bar.grid(row=3, column=0, columnspan=2, pady=10)

    # Function to handle zoom (mouse wheel with Shift)
    def mouse_wheel(event):
        """Zoom the ASCII art in and out."""
        if event.state & 0x1:  # Shift key held
            new_size = current_font_size.get() + (1 if event.delta > 0 else -1)
            if 5 <= new_size <= 30:
                current_font_size.set(new_size)
                preview_widget.config(font=("Courier", current_font_size.get()))
        else:
            preview_widget.yview_scroll(-1 * (event.delta // 120), "units")

    # Bind mouse wheel to the preview widget
    preview_widget.bind("<MouseWheel>", mouse_wheel)

    # Play video button
    play_button = tk.Button(
        main_window,
        text="Play ASCII Art Video",
        font=("Rockabilly", 10),
        command=lambda: play_video(preview_widget),
        width=20,
        height=2
    )
    play_button.pack(pady=10)

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

    return main_window

# Create and display the main window
main_window = create_main()
main_window.mainloop()
