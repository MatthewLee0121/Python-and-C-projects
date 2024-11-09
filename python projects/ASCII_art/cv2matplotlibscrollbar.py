import cv2
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider



# Load your image using OpenCV
image = cv2.imread(r'C:\Users\mat_m\OneDrive\Pictures\samurai.jpg')


# Load your images using OpenCV
edges = cv2.Canny(image, 100, 200)  # Example of edge detection, replace with your own processing
edges2 = cv2.Canny(image, 399, 400)
edges3 = cv2.Canny(image, 1, 100)

# Display the images using Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Hide the axes
for ax in axes:
    ax.axis('off')

# Display original image
axes[0].imshow(edges2, cmap='gray')
axes[0].set_title('Original Image')

# Display edge-detected image
axes[1].imshow(edges3, cmap='gray')  # Assuming edges is a grayscale image
axes[1].set_title('Edge Detected Image')



plt.show()
