import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import ASCII_art

# Load your image using OpenCV
image = cv2.imread(r'C:\Users\mat_m\OneDrive\Pictures\samurai.jpg')

edges = ASCII_art.edge_detection(image)
# Load your images using OpenCV
edges = cv2.Canny(image, 100, 200)  # Example of edge detection, replace with your own processing

# Display the images using Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Hide the axes
for ax in axes:
    ax.axis('off')

# Display original image
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')

# Display edge-detected image
axes[1].imshow(edges, cmap='gray')  # Assuming edges is a grayscale image
axes[1].set_title('Edge Detected Image')

plt.show()

import cv2
import matplotlib.pyplot as plt

# Load your images using OpenCV

edges = cv2.Canny(image, 100, 400)  # Example of edge detection, replace with your own processing

# Display the images using Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Hide the axes
for ax in axes:
    ax.axis('off')

# Display original image
axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Image')

# Display edge-detected image
axes[1].imshow(edges, cmap='gray')  # Assuming edges is a grayscale image
axes[1].set_title('Edge Detected Image')

plt.show()
