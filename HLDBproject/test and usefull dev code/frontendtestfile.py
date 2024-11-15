from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox as msg
import backend
import os


class LogInWindow:
    def __init__(self):
        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'loginAssets')

        backend.InitiateUNPWTable()

        # Create the main ViewWindow
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
            HomeWindow()
        else:
            msg.showerror("Error", "Invalid username or password")

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
        self.homeWindow.destroy()
        ViewWindow()


class ViewWindow:
    def __init__(self):
         # Initialize the Tkinter window
        self.ViewWindow = tk.Tk()

        # Get screen width and height (now that self.ViewWindow is initialized)
        screen_width = self.ViewWindow.winfo_screenwidth()
        screen_height = self.ViewWindow.winfo_screenheight()


        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'viewAssets')
        
        # Set window size based on screen size (for responsiveness)
        window_width = int(screen_width * 0.75)  # 75% of the screen width
        window_height = int(screen_height * 0.75)  # 75% of the screen height
        self.ViewWindow.geometry(f"{window_width}x{window_height}")
        self.ViewWindow.configure(bg="#FFFFFF")
        self.ViewWindow.title("Hazard Record Database - Home Page")
        
        # Allow window to be resized
        self.ViewWindow.resizable(True, True)

        # Create canvas
        self.canvas = Canvas(
            self.ViewWindow,
            bg="#FFFFFF",
            height=window_height,
            width=window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0, relwidth=1.0, relheight=1.0)  # Use relative width and height
        
        # Create UI components
        self.create_background()
        self.create_lines()
        self.create_text()
        self.create_images()
        self.create_buttons()
        self.create_listbox()

        self.ViewWindow.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return Path(self.ASSETS_PATH) / Path(path)

    def create_background(self):
        # Create background rectangle that covers the entire window
        self.canvas.create_rectangle(
            0.0, 0.0, 
            1.0, 1.0,
            fill="#2F4B9F", outline="", 
            tags="background", 
            width=1,
        )
    
    def create_lines(self):
        # Adjust the lines' positioning with relative placement
        lines = [
            (0.1, 0.1, 0.1, 0.95),
            (0.3, 0.1, 0.3, 0.95),
            (0.95, 0.15, 0.95, 0.22),
            (0.48, 0.15, 0.48, 0.22),
            (0.12, 0.22, 0.27, 0.23),
            (0.3, 0.22, 0.98, 0.23),
            (0.02, 0.15, 0.98, 0.16)
        ]
        
        for x1, y1, x2, y2 in lines:
            self.canvas.create_rectangle(
                x1 * self.canvas.winfo_width(), y1 * self.canvas.winfo_height(),
                x2 * self.canvas.winfo_width(), y2 * self.canvas.winfo_height(),
                fill="#FFFFFF", outline=""
            )

    def create_listbox(self):
        listbox_specs = [
            ('ViewTable', 0.28, 0.25, 0.69, 0.63),  # Relative positioning
            ('TableName', 0.12, 0.25, 0.14, 0.03)  # Relative positioning
        ]
        
        for name, x1, y1, rel_width, rel_height in listbox_specs:
            listbox = tk.Listbox(
                self.ViewWindow,
                bg="#FFFFFF",
                font=("Kodchasan Regular", 12),
                selectbackground="#C3CDE0"
            )
            setattr(self, f"{name}Listbox", listbox)
            listbox.place(x=x1 * self.ViewWindow.winfo_width(), y=y1 * self.ViewWindow.winfo_height(),
                          relwidth=rel_width, relheight=rel_height)
        
        self.populateTableNameListBox()

    def populateTableNameListBox(self):
        # Example table names, replace with actual data fetching
        table_names = ["Table1", "Table2", "Table3"]

        self.TableNameListbox.delete(0, tk.END)
        for table_name in table_names:
            self.TableNameListbox.insert(tk.END, table_name)

    def showTable(self):
        # Handle showing the table data (update your listbox)
        pass

    def create_text(self):
        # Create text labels with relative positioning
        texts = [
            (0.02, 0.05, "Hazard Record Database - View", 36),
            (0.12, 0.18, "Table Selector", 20),
            (0.29, 0.18, "Table Viewport", 20),
            (0.48, 0.18, "Active Table:", 20),
        ]
        
        for x, y, text, size in texts:
            self.canvas.create_text(
                x * self.canvas.winfo_width(), y * self.canvas.winfo_height(),
                anchor="nw",
                text=text,
                fill="#FFFFFF",
                font=("Kodchasan Bold", size * -1)
            )
    
    def create_images(self):
        # Handle the images similarly
        self.image_logo = PhotoImage(file=self.relative_to_assets("logo.png"))
        self.canvas.create_image(
            0.92 * self.canvas.winfo_width(),
            0.94 * self.canvas.winfo_height(),
            image=self.image_logo
        )

    def create_buttons(self):
        # Create buttons with relative positioning
        button_specs = [
            ('buttonHome.png', 0.02, 0.92, self.Button_home_pressed),
            ('buttonViewTable.png', 0.16, 0.53, self.showTable),
            ('buttonDeleteTable.png', 0.02, 0.31, lambda: print("Delete Table")),
            ('buttonChangeTable.png', 0.02, 0.24, lambda: print("Change Table")),
            ('buttonAddTable.png', 0.02, 0.20, lambda: print("Add Table"))
        ]

        for img, x, y, command in button_specs:
            button_image = PhotoImage(file=self.relative_to_assets(img))
            button = Button(
                image=button_image,
                borderwidth=0,
                highlightthickness=0,
                command=command,
                relief="flat"
            )
            button.place(x=x * self.ViewWindow.winfo_width(), y=y * self.ViewWindow.winfo_height(),
                         anchor="nw", relwidth=0.1, relheight=0.05)

    def Button_home_pressed(self):
        self.ViewWindow.destroy()
        HomeWindow()  # Assuming you have a HomeWindow class to go to

if __name__ == "__main__": 
    #LogInWindow()
    #HomeWindow()
    ViewWindow()


#     def __init__(self):
#     self.ViewWindow = Tk()
#     self.ViewWindow.geometry("1395x784")
#     self.ViewWindow.bind("<Configure>", self.on_resize)
#     # Initialize other components as before...

# def on_resize(self, event):
#     # Adjust component sizes based on event.width and event.height
#     self.create_lines()  # Redraw lines
#https://stackoverflow.com/questions/41416788/python-resizing-widgets-when-window-is-resized-using-place-manager
