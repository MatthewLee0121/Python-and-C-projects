from PIL import Image, ExifTags
from tkinter import filedialog, Tk

def get_image_metadata(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Extract EXIF data
            exif_data = img._getexif()
            
            if exif_data is not None:
                # Iterate through all EXIF tags
                metadata = {}
                for tag, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    metadata[tag_name] = value
                return metadata
            else:
                print("No EXIF data found.")
                return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    root = Tk()
    root.withdraw()  # Hide the main window
    
    image_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpeg;")])  # Open file dialog to choose image
    if image_path:
        metadata = get_image_metadata(image_path)
        if metadata:
            print("Image Metadata:")
            for key, value in metadata.items():
                print(f"{key}: {value}")
        else:
            print("Failed to retrieve metadata.")
    else:
        print("No image selected.")

if __name__ == "__main__":
    main()
