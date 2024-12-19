import cv2
import os
from tkinter import filedialog
from tkinter import Tk

def images_to_video(image_folder, output_video_file, fps=30, video_size=None):
    # Get all images in the folder (looking for .png files)
    images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]
    
    # Check if there are any images to process
    if not images:
        print("No PNG images found in the folder.")
        return
    
    # Read the first image to get the size
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    
    if video_size is None:
        # Use the size of the first image as the size for the video
        height, width, _ = first_image.shape
        video_size = (width, height)
    
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
    video_writer = cv2.VideoWriter(output_video_file, fourcc, fps, video_size)
    
    # Loop through images and add them to the video
    for image_name in images:
        image_path = os.path.join(image_folder, image_name)
        frame = cv2.imread(image_path)
        
        # Resize image if necessary to match the video size
        if frame.shape[1] != video_size[0] or frame.shape[0] != video_size[1]:
            frame = cv2.resize(frame, video_size)
        
        video_writer.write(frame)
    
    # Release the video writer object
    video_writer.release()
    print(f"Video saved as {output_video_file}")

# Initialize Tkinter (so the file dialog works)
root = Tk()
root.withdraw()  # Hide the Tkinter root window

# Ask the user for the folder containing images
image_folder = filedialog.askdirectory(title="Select Folder Containing Images")

# Ask the user where to save the output video
output_video_file = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")], title="Save Video As")

if image_folder and output_video_file:
    images_to_video(image_folder, output_video_file, fps=25)
else:
    print("Operation cancelled.")
