import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from backend import *

#Homescreen
def CreateHomeScreen():
    # Initialize the database table
    initialiseDB()

    # GUI setup
    root = tk.Tk()
    root.title("Test DB")

    # Button to add data to the test table
    def on_add_test():
        test_id = entry_test_id.get()
        name = entry_name.get()
        age = entry_age.get()

        table_name = get_dropdown_value()
        add2Test(table_name, test_id, name, age)

        entry_test_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)

    # Function to view the selected table
    def on_view_table():
        # Get the selected table from the dropdown
        table_name = get_dropdown_value()

        # Fetch rows from the selected table and update the listbox
        rows = viewDBTable(table_name)

        # Clear the listbox before adding new data
        listbox_view_test.delete(0, tk.END)
        
        # Insert data into the listbox
        for row in rows:
            listbox_view_test.insert(tk.END, f"test_id: {row[0]} | name: {row[1]} | age: {row[2]}")


    # Entry fields and labels for user input
    label_test_id = tk.Label(root, text="Test ID:")
    label_test_id.grid(row=0, column=0)

    entry_test_id = tk.Entry(root)
    entry_test_id.grid(row=0, column=1)

    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=1, column=0)

    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1)

    label_age = tk.Label(root, text="Age:")
    label_age.grid(row=2, column=0)

    entry_age = tk.Entry(root)
    entry_age.grid(row=2, column=1)

    button_add_test = tk.Button(root, text="Add Test", command=on_add_test)
    button_add_test.grid(row=4, column=1, columnspan=2)

    button_view_table = tk.Button(root, text="View Table", command=on_view_table)
    button_view_table.grid(row=2, column=2, columnspan=2)

    #displays a list box to view tables
    listbox_view_test = tk.Listbox(root, width=80, height=10)
    listbox_view_test.grid(row=0, column=11, columnspan=2, rowspan=6)


    table_names = getTableNames()
    selected_table = tk.StringVar(root)
    selected_table.set(str(table_names[0]))

    label_tabel_name = tk.Label(root, text="Table Name: ")
    label_tabel_name.grid(row=3, column=0)

    table_dropdown = tk.OptionMenu(root, selected_table, *table_names)
    table_dropdown.grid(row=3, column=1)

    def get_dropdown_value():
        return selected_table.get()



    # Run the GUI loop
    root.mainloop()

    # Close the database when GUI is closed
    closeDB()

#Login screen 
def LoadLogIn():

    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'loginAssets')

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #initiate usernames and password
    InitiateUNPWTable()

    def login():
        username = entryUserName.get()
        password = entryPassWord.get()

        if verify_credentials(username, password):
            print("Login successful!")
            logInWindow.destroy()
            LoadHomeWindow()
            #CreateHomeScreen() #delete this later
        else:
            msgbx.showerror("Error", "Invalid username or password")

    logInWindow = Tk()

    logInWindow.geometry("650x400")
    logInWindow.configure(bg = "#2F4B9F")
    logInWindow.title("Hazard Record Database - Login Page")


    canvas = Canvas(
        logInWindow,
        bg = "#FFFFFF",
        height = 400,
        width = 650,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        650.0,
        400.0,
        fill="#2F4B9F",
        outline="")

    image_logo = PhotoImage(
        file=relative_to_assets("logo.png"))
    logo = canvas.create_image(
        568.0,
        362.0,
        image=image_logo
    )

    buttonLoginImage = PhotoImage(
        file=relative_to_assets("loginButton.png"))
    loginButton = Button(
        image=buttonLoginImage,
        borderwidth=0,
        highlightthickness=0,
        command=login,
        relief="flat"
    )
    loginButton.place(
        x=283.0,
        y=251.0,
        width=100.0,
        height=25.0
    )

    entryPassWordImage = PhotoImage(
        file=relative_to_assets("entryPassWord.png"))
    entryPassWordBg = canvas.create_image(
        333.0,
        225.5,
        image=entryPassWordImage
    )
    entryPassWord = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entryPassWord.place(
        x=233.0,
        y=213.0,
        width=200.0,
        height=23.0
    )

    canvas.create_text(
        167.0,
        218.0,
        anchor="nw",
        text="Password:",
        fill="#FFFFFF",
        font=("Kodchasan Regular", 12 * -1)
    )

    entryUserNameImage = PhotoImage(
        file=relative_to_assets("entryUserName.png"))
    entryUserNameBg = canvas.create_image(
        333.0,
        187.5,
        image=entryUserNameImage
    )
    entryUserName = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entryUserName.place(
        x=233.0,
        y=175.0,
        width=200.0,
        height=23.0
    )

    canvas.create_text(
        167.0,
        180.0,
        anchor="nw",
        text="Username:",
        fill="#FFFFFF",
        font=("Kodchasan Regular", 12 * -1)
    )

    canvas.create_text(
        112.0,
        110.0,
        anchor="nw",
        text="Hazard Record Database",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 36 * -1)
    )

    canvas.create_rectangle(
        94.0,
        162.0,
        556.9999941562619,
        163.99999994451028,
        fill="#FFFFFF",
        outline="")


    logInWindow.resizable(False, False)
    logInWindow.mainloop()
    closeDB()

def LoadHomeWindow():

    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'homeAssets')

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    def ButtonViewATablePressed():
        homeWindow.destroy()
        loadViewWindow()

    #initialise the DB
    initialiseDB()
    
    homeWindow = Tk()

    homeWindow.geometry("650x400")
    homeWindow.configure(bg = "#FFFFFF")
    homeWindow.title("Hazard Record Database - Home Page")

    canvas = Canvas(
        homeWindow,
        bg = "#FFFFFF",
        height = 400,
        width = 650,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        650.0,
        400.0,
        fill="#2F4B9F",
        outline="")

    image_logo = PhotoImage(
        file=relative_to_assets("logo.png"))
    logo = canvas.create_image(
        568.0,
        362.0,
        image=image_logo
    )

    canvas.create_text(
        11.0,
        6.0,
        anchor="nw",
        text="Hazard Logs Database - Home",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 36 * -1)
    )

    canvas.create_rectangle(
        10.0,
        58.0,
        636.0,
        59.0,
        fill="#FFFFFF",
        outline="")

    buttonChangeATableImage = PhotoImage(
        file=relative_to_assets("buttonChangeATable.png"))
    buttonChangeATable = Button(
        image=buttonChangeATableImage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("buttonChangeATable clicked"),
        relief="flat"
    )
    buttonChangeATable.place(
        x=378.0,
        y=114.0,
        width=146.0,
        height=86.0
    )

    buttonDeleteATableImage = PhotoImage(
        file=relative_to_assets("buttonDeleteATable.png"))
    buttonDeleteATable = Button(
        image=buttonDeleteATableImage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("buttonDeleteATable clicked"),
        relief="flat"
    )
    buttonDeleteATable.place(
        x=378.0,
        y=229.0,
        width=146.0,
        height=86.0
    )

    buttonAddATableImage = PhotoImage(
        file=relative_to_assets("buttonAddATable.png"))
    buttonAddATable = Button(
        image=buttonAddATableImage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("buttonAddATable clicked"),
        relief="flat"
    )
    buttonAddATable.place(
        x=103.0,
        y=229.0,
        width=146.0,
        height=86.0
    )

    buttonViewATableImage = PhotoImage(
        file=relative_to_assets("buttonViewATable.png"))
    buttonViewATable = Button(
        image=buttonViewATableImage,
        borderwidth=0,
        highlightthickness=0,
        command=ButtonViewATablePressed,
        relief="flat"
    )
    buttonViewATable.place(
        x=103.0,
        y=114.0,
        width=146.0,
        height=86.0
    )
    homeWindow.resizable(False, False)
    homeWindow.mainloop()

def loadViewWindow():

    ASSETS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'viewAssets')

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window = Tk()
    window.geometry("1395x784")
    window.configure(bg = "#FFFFFF")

    #creating canvas
    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 784,
        width = 1395,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    #background rectangle
    canvas.create_rectangle(
        0.0,
        0.0,
        1395.0,
        784.0,
        fill="#2F4B9F",
        outline="")
    
    #verticle line 1
    canvas.create_rectangle(
        146.99997184986591,
        127.0,
        148.0,
        772.0,
        fill="#FFFFFF",
        outline="")

    #verticle line 2
    canvas.create_rectangle(
        383.00000236744404,
        127.0,
        384.0000305175781,
        772.0,
        fill="#FFFFFF",
        outline="")
        
    #verticle line 3
    canvas.create_rectangle(
        1339.0,
        123.0,
        1340.0000021855694,
        174.0,
        fill="#FFFFFF",
        outline="")

    #verticle line 4
    canvas.create_rectangle(
        671.0,
        123.0,
        672.0000021855697,
        174.0,
        fill="#FFFFFF",
        outline="")

    #horizontal line 1
    canvas.create_rectangle(
        173.0,
        178.0,
        378.0,
        179.00000000000003,
        fill="#FFFFFF",
        outline="")
        
    #horizontal line 2
    canvas.create_rectangle(
        397.0,
        178.0,
        1369.0,
        179.0000000000001,
        fill="#FFFFFF",
        outline="")

    #horizontal line 3
    canvas.create_rectangle(
        23.0,
        115.0,
        1365.0,
        116.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        24.0,
        41.0,
        anchor="nw",
        text="Hazard Record Database - View",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 36 * -1)
    )

    canvas.create_text(
        174.0,
        149.0,
        anchor="nw",
        text="Table Selector",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 20 * -1)
    )

    canvas.create_text(
        399.0,
        144.0,
        anchor="nw",
        text="Table Viewport",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 20 * -1)
    )

    canvas.create_text(
        677.0,
        144.0,
        anchor="nw",
        text="Active Table:",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 20 * -1)
    )

    canvas.create_text(
        817.0,
        144.0,
        anchor="nw",
        text="Table_name",
        fill="#FFFFFF",
        font=("Kodchasan Bold", 20 * -1)
    )

    image_logo = PhotoImage(
        file=relative_to_assets("logo.png"))
    logo = canvas.create_image(
        1295.0,
        734.0,
        image=image_logo
    )

    buttonHomeImage = PhotoImage(
        file=relative_to_assets("buttonHome.png"))
    buttonHome = Button(
        image=buttonHomeImage,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("buttonHome clicked"),
        relief="flat"
    )
    buttonHome.place(
        x=26.0,
        y=718.0,
        width=109.26072692871094,
        height=32.340213775634766
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("logo.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=220,
        y=418.0,
        width=109.26072692871094,
        height=32.340213775634766
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("logo.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=24.0,
        y=246.0,
        width=109.26072692871094,
        height=32.340213775634766
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("logo.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=24.0,
        y=192.79013061523438,
        width=109.26072692871094,
        height=32.340213775634766
    )
    
    button_image_5 = PhotoImage(
        file=relative_to_assets("logo.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=24.0,
        y=140.0,
        width=109.392333984375,
        height=32.340213775634766
    )

    canvas.create_rectangle(
        398.0,
        193.0,
        1365.0,
        688.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        174.0,
        193.0,
        363.0,
        408.0,
        fill="#FFFFFF",
        outline="")
    
    window.resizable(False, False)
    window.mainloop()

#comment these out when working on different screens
#LoadLogIn()
#LoadHomeWindow()
CreateHomeScreen()
#loadViewWindow()

# Close the database when GUI is closed
closeDB()