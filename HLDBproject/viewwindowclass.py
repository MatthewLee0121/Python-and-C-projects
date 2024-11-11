from tkinter import Tk, Canvas, PhotoImage, Button
from pathlib import Path
import os

class ViewWindow:
    def __init__(self):
        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'viewAssets')
        self.window = Tk()
        self.window.geometry("1395x784")
        self.window.configure(bg="#FFFFFF")
        
        # Create canvas
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=784,
            width=1395,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        
        # Draw components
        self.create_background()
        self.create_lines()
        self.create_text()
        self.create_images()
        self.create_buttons()

        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return Path(self.ASSETS_PATH) / Path(path)

    def create_background(self):
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1395.0,
            784.0,
            fill="#2F4B9F",
            outline=""
        )

    def create_lines(self):
        # Vertical and horizontal lines
        lines = [
            (146.0, 127.0, 147.0, 772.0),
            (383.0, 127.0, 384.0, 772.0),
            (1339.0, 123.0, 1340.0, 174.0),
            (671.0, 123.0, 672.0, 174.0),
            (173.0, 178.0, 378.0, 179.0),
            (397.0, 178.0, 1369.0, 179.0),
            (23.0, 115.0, 1365.0, 116.0),
            (398.0, 193.0, 1365.0, 688.0),
            (174.0, 193.0, 363.0, 408.0)
        ]
        for x1, y1, x2, y2 in lines:
            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#FFFFFF",
                outline=""
            )

    def create_text(self):
        # Text elements
        texts = [
            (24.0, 41.0, "Hazard Record Database - View", 36),
            (174.0, 149.0, "Table Selector", 20),
            (399.0, 144.0, "Table Viewport", 20),
            (677.0, 144.0, "Active Table:", 20),
            (817.0, 144.0, "Table_name", 20)
        ]
        for x, y, text, size in texts:
            self.canvas.create_text(
                x, y,
                anchor="nw",
                text=text,
                fill="#FFFFFF",
                font=("Kodchasan Bold", size * -1)
            )

    def create_images(self):
        # Logo image
        self.image_logo = PhotoImage(
            file=self.relative_to_assets("logo.png")
        )
        self.canvas.create_image(
            1295.0,
            734.0,
            image=self.image_logo
        )

    def create_buttons(self):
        # Button images and setup
        self.button_home_image = PhotoImage(file=self.relative_to_assets("buttonHome.png"))
        self.button_2_image = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_3_image = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_4_image = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_5_image = PhotoImage(file=self.relative_to_assets("button_5.png"))

        # Button creation with commands and images
        buttonHome = Button(
            image=self.button_home_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonHome clicked"),
            relief="flat"
        )
        buttonHome.place(x=26.0, y=718.0, width=109.0, height=32.0)

        button_2 = Button(
            image=self.button_2_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(x=220, y=418.0, width=109.0, height=32.0)

        button_3 = Button(
            image=self.button_3_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(x=24.0, y=246.0, width=109.0, height=32.0)

        button_4 = Button(
            image=self.button_4_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(x=24.0, y=192.0, width=109.0, height=32.0)

        button_5 = Button(
            image=self.button_5_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(x=24.0, y=140.0, width=109.0, height=32.0)

# Usage
if __name__ == "__main__":
    view_window = ViewWindow()
