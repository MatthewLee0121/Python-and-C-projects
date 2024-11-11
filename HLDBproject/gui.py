from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def createViewWindow():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mat_m\OneDrive\Desktop\build\build\assets\frame0")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1395x784")
    window.configure(bg = "#FFFFFF")


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
    canvas.create_rectangle(
        0.0,
        0.0,
        1395.0,
        784.0,
        fill="#2F4B9F",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        1295.0,
        734.0,
        image=image_image_1
    )

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

    canvas.create_rectangle(
        146.99997184986591,
        127.0,
        148.0,
        772.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        383.00000236744404,
        127.0,
        384.0000305175781,
        772.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        173.0,
        178.0,
        378.0,
        179.00000000000003,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        397.0,
        178.0,
        1369.0,
        179.0000000000001,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        23.0,
        115.0,
        1365.0,
        116.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=26.0,
        y=718.0,
        width=109.26072692871094,
        height=32.340213775634766
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=269.0,
        y=418.0,
        width=109.26072692871094,
        height=32.340213775634766
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
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
        file=relative_to_assets("button_4.png"))
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
        file=relative_to_assets("button_5.png"))
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

    canvas.create_rectangle(
        1339.0,
        123.0,
        1340.0000021855694,
        174.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        671.0,
        123.0,
        672.0000021855697,
        174.0,
        fill="#FFFFFF",
        outline="")
    window.resizable(False, False)
    window.mainloop()
