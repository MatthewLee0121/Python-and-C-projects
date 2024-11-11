from tkinter import Tk, Canvas, PhotoImage, Button, Entry, messagebox as msgbx
from pathlib import Path
import os
import backend

class LogInWindow:
    def __init__(self):
        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'loginAssets')

        backend.InitiateUNPWTable()

        # Create the main window
        self.logInWindow = Tk()
        self.logInWindow.geometry("650x400")
        self.logInWindow.configure(bg="#2F4B9F")
        self.logInWindow.title("Hazard Record Database - Login Page")

        # Create canvas
        self.canvas = Canvas(
            self.logInWindow,
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
        self.create_entries()
        self.create_buttons()

        self.logInWindow.resizable(False, False)
        self.logInWindow.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return Path(self.ASSETS_PATH) / Path(path)

    def login(self):
        username = self.entryUserName.get()
        password = self.entryPassWord.get()

        if backend.verify_credentials(username, password):
            self.logInWindow.destroy()
            backend.closeDB()
        else:
            msgbx.showerror("Error", "Invalid username or password")

    def create_background(self):
        self.canvas.create_rectangle(
            0.0,
            0.0,
            650.0,
            400.0,
            fill="#2F4B9F",
            outline=""
        )
        # Logo image
        self.image_logo = PhotoImage(file=self.relative_to_assets("logo.png"))
        self.canvas.create_image(568.0, 362.0, image=self.image_logo)

    def create_text(self):
        self.canvas.create_text(
            112.0,
            110.0,
            anchor="nw",
            text="Hazard Record Database",
            fill="#FFFFFF",
            font=("Kodchasan Bold", 36 * -1)
        )
        self.canvas.create_rectangle(
            94.0,
            162.0,
            556.9999941562619,
            163.99999994451028,
            fill="#FFFFFF",
            outline=""
        )
        self.canvas.create_text(
            167.0,
            180.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Kodchasan Regular", 12 * -1)
        )
        self.canvas.create_text(
            167.0,
            218.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Kodchasan Regular", 12 * -1)
        )

    def create_entries(self):
        # Username entry
        self.entryUserNameImage = PhotoImage(file=self.relative_to_assets("entryUserName.png"))
        self.canvas.create_image(333.0, 187.5, image=self.entryUserNameImage)
        self.entryUserName = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entryUserName.place(x=233.0, y=175.0, width=200.0, height=23.0)

        # Password entry
        self.entryPassWordImage = PhotoImage(file=self.relative_to_assets("entryPassWord.png"))
        self.canvas.create_image(333.0, 225.5, image=self.entryPassWordImage)
        self.entryPassWord = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entryPassWord.place(x=233.0, y=213.0, width=200.0, height=23.0)

    def create_buttons(self):
        # Login button
        self.buttonLoginImage = PhotoImage(file=self.relative_to_assets("loginButton.png"))
        self.loginButton = Button(
            image=self.buttonLoginImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.loginButton.place(x=283.0, y=251.0, width=100.0, height=25.0)

# Usage example with a callback for the home window
if __name__ == "__main__":
    LogInWindow()
