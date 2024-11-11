from tkinter import Tk, Canvas, PhotoImage, Button
from pathlib import Path
import os
import backend

class HomeWindow:
    def __init__(self,):
        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'homeAssets')
        self.initialise_db()
        
        # Create the main window
        self.homeWindow = Tk()
        self.homeWindow.geometry("650x400")
        self.homeWindow.configure(bg="#FFFFFF")
        self.homeWindow.title("Hazard Record Database - Home Page")
        
        # Create canvas
        self.canvas = Canvas(
            self.homeWindow,
            bg="#FFFFFF",
            height=400,
            width=650,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.create_background()
        self.create_text()
        self.create_images()
        self.create_buttons()
        
        self.homeWindow.resizable(False, False)
        self.homeWindow.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return Path(self.ASSETS_PATH) / Path(path)

    def initialise_db(self):
        backend.initialiseDB()

    def create_background(self):
        self.canvas.create_rectangle(
            0.0,
            0.0,
            650.0,
            400.0,
            fill="#2F4B9F",
            outline=""
        )

    def create_text(self):
        self.canvas.create_text(
            11.0,
            6.0,
            anchor="nw",
            text="Hazard Logs Database - Home",
            fill="#FFFFFF",
            font=("Kodchasan Bold", 36 * -1)
        )
        self.canvas.create_rectangle(
            10.0,
            58.0,
            636.0,
            59.0,
            fill="#FFFFFF",
            outline=""
        )

    def create_images(self):
        # Logo image
        self.image_logo = PhotoImage(file=self.relative_to_assets("logo.png"))
        self.canvas.create_image(568.0, 362.0, image=self.image_logo)

    def create_buttons(self):
        # Button images
        self.buttonChangeATableImage = PhotoImage(file=self.relative_to_assets("buttonChangeATable.png"))
        self.buttonDeleteATableImage = PhotoImage(file=self.relative_to_assets("buttonDeleteATable.png"))
        self.buttonAddATableImage = PhotoImage(file=self.relative_to_assets("buttonAddATable.png"))
        self.buttonViewATableImage = PhotoImage(file=self.relative_to_assets("buttonViewATable.png"))

        # Buttons with their commands
        buttonChangeATable = Button(
            image=self.buttonChangeATableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonChangeATable clicked"),
            relief="flat"
        )
        buttonChangeATable.place(x=378.0, y=114.0, width=146.0, height=86.0)

        buttonDeleteATable = Button(
            image=self.buttonDeleteATableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonDeleteATable clicked"),
            relief="flat"
        )
        buttonDeleteATable.place(x=378.0, y=229.0, width=146.0, height=86.0)

        buttonAddATable = Button(
            image=self.buttonAddATableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonAddATable clicked"),
            relief="flat"
        )
        buttonAddATable.place(x=103.0, y=229.0, width=146.0, height=86.0)

        buttonViewATable = Button(
            image=self.buttonViewATableImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_view_a_table_pressed,
            relief="flat"
        )
        buttonViewATable.place(x=103.0, y=114.0, width=146.0, height=86.0)

    def button_view_a_table_pressed(self):
        # Close this window and open the view window
        self.homeWindow.destroy()

# Usage example with a callback for view window loading
if __name__ == "__main__":
    home_window = HomeWindow()
