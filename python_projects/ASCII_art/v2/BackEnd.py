import os
from PIL import Image
import cv2
import numpy as np

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

def get_ascii_art(image_path, block_size, line_detection):
    # Open and process the image
    try:
        if line_detection:
            image = cv2.imread(image_path)
            img = edge_detection(image)
            img = Image.fromarray(img)
        else:
            img = Image.open(image_path)
            
        img = img.convert("L")  # Convert to grayscale

        # Calculate new dimensions based on the block size
        width, height = img.size
        new_width = width // block_size
        new_height = height // block_size

        # Resize the image
        img = img.resize((new_width, new_height))

        # Generate ASCII art
        ascii_art = ""
        pixels = img.load()
        for y in range(new_height):
            for x in range(new_width):
                brightness = pixels[x, y]
                char_index = int((brightness / 255) * (len(ascii_characters_by_density) - 1))
                ascii_art += ascii_characters_by_density[char_index]
            ascii_art += "\n"
        
        return ascii_art
    except Exception as e:
        raise RuntimeError(f"Failed to process image: {e}")

def save_ascii_art(ascii_art, file_path):
    try:
        with open(file_path, "w") as file:
            file.write(ascii_art)
    except Exception as e:
        raise RuntimeError(f"Failed to save ASCII art: {e}")

def edge_detection(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (3, 3), 0)
    sobel_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    gradient_magnitude *= 255.0 / gradient_magnitude.max()
    gradient_magnitude = np.uint8(gradient_magnitude)
    return gradient_magnitude