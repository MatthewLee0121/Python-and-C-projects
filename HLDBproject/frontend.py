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
        self.ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'viewAssets')
        self.ViewWindow = Tk()
        self.ViewWindow.geometry("1395x784")
        self.ViewWindow.configure(bg="#FFFFFF")
        self.ViewWindow.title("Hazard Record Database - Home Page")

        # Create canvas
        self.canvas = Canvas(
            self.ViewWindow,
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
        self.createLines()
        self.create_text()
        self.create_images()
        self.create_buttons()
        self.createListBox()

        #self.ViewWindow.resizable(False, False)
        self.ViewWindow.mainloop()

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

    def createLines(self):
        # Vertical and horizontal lines
        lines = [
            (146.0, 127.0, 147.0, 772.0),
            (383.0, 127.0, 384.0, 772.0),
            (1339.0, 123.0, 1340.0, 174.0),
            (671.0, 123.0, 672.0, 174.0),
            (173.0, 178.0, 378.0, 179.0),
            (397.0, 178.0, 1369.0, 179.0),
            (23.0, 115.0, 1365.0, 116.0),
        ]
        for x1, y1, x2, y2 in lines:
            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="#FFFFFF",
                outline=""
            )
    
    def createListBox(self):

        listbox_specs = [
        ('ViewTable', 398.0, 193.0, 967.0, 495.0),
        ('TableName', 174.0, 193.0, 189.0, 215.0)
        ]

        for name, x1, y1, width, height in listbox_specs:
            listbox = tk.Listbox(
                self.ViewWindow,
                bg="#FFFFFF",
                font=("Kodchasan Regular", 12),
                selectbackground="#C3CDE0"
            )
            setattr(self, f"{name}Listbox", listbox)
            listbox.place(x=x1, y=y1, width=width, height=height)
        
        self.populateTableNameListBox()

    def populateTableNameListBox(self):
        table_names = []
        table_names = backend.getTableNames()

        self.TableNameListbox.delete(0, tk.END)

        for table_name in table_names:
            if table_name == 'users':
                pass
            elif table_name == 'sqlite_sequence':
                pass
            else:
                self.TableNameListbox.insert(tk.END, backend.swapUnderToSpace(table_name))

    def showTable(self):

        self.ViewTableListbox.delete(0,tk.END)
        selectedTableTuple = self.TableNameListbox.curselection()
        selectedTable = self.TableNameListbox.get(selectedTableTuple[0])
        self.canvas.itemconfig(self.tableNameTextBox, text=str(selectedTable))
        selectedTable = backend.swapSpaceToUnder(selectedTable)

        rows = backend.viewDBTable(selectedTable)
        columns = backend.getTableColumnNames(selectedTable)
#        dataframe = backend.createpandasdf(rows, columns)
        columns = [backend.swapUnderToSpace(col) for col in columns]
        header = " | ".join(f"{col}:" for col in columns)
        # for i in range(len(dataframe)):
        #     self.ViewTableListbox.insert(tk.END, dataframe.iloc[i])

        self.ViewTableListbox.insert(tk.END, header)
        self.ViewTableListbox.insert(tk.END, "-" * len(header))

        for row in rows:
            row_text = " | ".join(f"{columns[i]}: {row[i]}" for i in range(len(columns)))
            self.ViewTableListbox.insert(tk.END, row_text)

    def create_text(self):
        texts = [
            (24.0, 41.0, "Hazard Record Database - View", 36),
            (174.0, 149.0, "Table Selector", 20),
            (399.0, 144.0, "Table Viewport", 20),
            (677.0, 144.0, "Active Table:", 20),
        ]

        for x, y, text, size in texts:
            self.canvas.create_text(
                x, y,
                anchor="nw",
                text=text,
                fill="#FFFFFF",
                font=("Kodchasan Bold", size * -1)
            )

        self.tableNameTextBox = self.canvas.create_text(
                817.0,
                144.0,
                anchor="nw",
                text= "No Table Selected.",
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
        self.buttonHomeImage = PhotoImage(file=self.relative_to_assets("buttonHome.png"))
        self.buttonViewTableImage = PhotoImage(file=self.relative_to_assets("buttonViewTable.png"))
        self.buttonDeleteTableImage = PhotoImage(file=self.relative_to_assets("buttonDeleteTable.png"))
        self.buttonChangeTableImage = PhotoImage(file=self.relative_to_assets("buttonChangeTable.png"))
        self.buttonAddTableImage = PhotoImage(file=self.relative_to_assets("buttonAddTable.png"))

        buttonHome = Button(
            image=self.buttonHomeImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.Button_home_pressed,
            relief="flat"
        )
        buttonHome.place(x=26.0, y=718.0, width=109.0, height=32.0)

        buttonViewTable = Button(
            image=self.buttonViewTableImage,
            borderwidth=0,
            highlightthickness=0,
            command=self.showTable,
            relief="flat"
        )
        buttonViewTable.place(x=220, y=418.0, width=109.0, height=32.0)

        buttonDeleteTable = Button(
            image=self.buttonDeleteTableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonDeleteTable clicked"),
            relief="flat"
        )
        buttonDeleteTable.place(x=24.0, y=246.0, width=109.0, height=32.0)

        buttonChangeATable = Button(
            image=self.buttonChangeTableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonChangeATable clicked"),
            relief="flat"
        )
        buttonChangeATable.place(x=24.0, y=192.0, width=109.0, height=32.0) 

        buttonAddTable = Button(
            image=self.buttonAddTableImage,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("buttonAddTable clicked"),
            relief="flat"
        )
        buttonAddTable.place(x=24.0, y=140.0, width=109.0, height=32.0)

    def Button_home_pressed(self):
        self.ViewWindow.destroy()
        HomeWindow()



if __name__ == "__main__": 
    #LogInWindow()
    #HomeWindow()
    ViewWindow()
