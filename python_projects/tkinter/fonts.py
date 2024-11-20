import tkinter as tk
from tkinter import ttk, font

def change_font():
    selected_font = font_var.get()
    text_label.config(font=(selected_font, font_size_var.get()))
    font_preview_label.config(text=f"Font Preview: {selected_font}")

# Tkinter UI setup
main_window = tk.Tk()
main_window.title("Font Example")

# Create a variable to store the selected font
font_var = tk.StringVar()
font_var.set("Arial")

# Create a variable to store the font size
font_size_var = tk.IntVar()
font_size_var.set(12)

# Updated list of fonts
font_list = ["System", "Terminal", "Fixedsys", "Modern", "Roman", "Script", "Courier", "MS Serif", "MS Sans Serif",
             "Small Fonts", "Marlett", "Arial", "Arabic Transparent", "Arial Baltic", "Arial CE", "Arial CYR",
             "Arial Greek", "Arial TUR", "Arial Black", "Bahnschrift Light", "Bahnschrift SemiLight", "Bahnschrift",
             "Bahnschrift SemiBold", "Bahnschrift Light SemiCondensed", "Bahnschrift SemiLight SemiConde", "Bahnschrift SemiCondensed",
             "Bahnschrift SemiBold SemiConden", "Bahnschrift Light Condensed", "Bahnschrift SemiLight Condensed",
             "Bahnschrift Condensed", "Bahnschrift SemiBold Condensed", "Calibri", "Calibri Light", "Cambria", "Cambria Math",
             "Candara", "Candara Light", "Comic Sans MS", "Consolas", "Constantia", "Corbel", "Corbel Light", "Courier New",
             "Courier New Baltic", "Courier New CE", "Courier New CYR", "Courier New Greek", "Courier New TUR", "Ebrima",
             "Franklin Gothic Medium", "Gabriola", "Gadugi", "Georgia", "Impact", "Ink Free", "Javanese Text", "Leelawadee UI",
             "Leelawadee UI Semilight", "Lucida Console", "Lucida Sans Unicode", "Malgun Gothic", "Malgun Gothic Semilight",
             "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft JhengHei UI", "Microsoft JhengHei Light",
             "Microsoft JhengHei UI Light", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif",
             "Microsoft Tai Le", "Microsoft YaHei", "Microsoft YaHei UI", "Microsoft YaHei Light", "Microsoft YaHei UI Light",
             "Microsoft Yi Baiti", "MingLiU-ExtB", "PMingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Mongolian Baiti", "MS Gothic",
             "MS UI Gothic", "MS PGothic", "MV Boli", "Myanmar Text", "Nirmala UI", "Nirmala UI Semilight", "Palatino Linotype",
             "Sans Serif Collection", "Segoe Fluent Icons", "Segoe MDL2 Assets", "Segoe Print", "Segoe Script", "Segoe UI",
             "Segoe UI Black", "Segoe UI Emoji", "Segoe UI Historic", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Semilight",
             "Segoe UI Symbol", "Segoe UI Variable Small Light", "Segoe UI Variable Small Semilig", "Segoe UI Variable Small",
             "Segoe UI Variable Small Semibold", "Segoe UI Variable Text Light", "Segoe UI Variable Text Semiligh",
             "Segoe UI Variable Text", "Segoe UI Variable Text Semibold", "Segoe UI Variable Display Light",
             "Segoe UI Variable Display Semil", "Segoe UI Variable Display", "Segoe UI Variable Display Semibold", "SimSun",
             "NSimSun", "SimSun-ExtB", "Sitka Small", "Sitka Small Semibold", "Sitka Text", "Sitka Text Semibold",
             "Sitka Subheading", "Sitka Subheading Semibold", "Sitka Heading", "Sitka Heading Semibold", "Sitka Display",
             "Sitka Display Semibold", "Sitka Banner", "Sitka Banner Semibold", "Sylfaen", "Symbol", "Tahoma", "Times New Roman",
             "Times New Roman Baltic", "Times New Roman CE", "Times New Roman CYR", "Times New Roman Greek", "Times New Roman TUR",
             "Trebuchet MS", "Verdana", "Webdings", "Wingdings", "Yu Gothic", "Yu Gothic UI", "Yu Gothic UI Semibold",
             "Yu Gothic Light", "Yu Gothic UI Light", "Rockybilly"]  # Add your new fonts here

# Create a style for the font menu to set the item font
font_menu_style = ttk.Style()
font_menu_style.configure("FontMenu.TMenubutton", font=("Arial", 12))

# Option menu for font selection with a scrollbar
font_menu = ttk.Combobox(main_window, textvariable=font_var, values=font_list, style="FontMenu.TMenubutton", state="readonly")
font_menu.pack(pady=10)

# Font preview label
font_preview_label = tk.Label(main_window, text="Font Preview: Arial", font=("Arial", 12))
font_preview_label.pack(pady=10)

# Scale widget for font size
font_size_scale = tk.Scale(main_window, from_=8, to=24, orient=tk.HORIZONTAL, variable=font_size_var, label="Font Size")
font_size_scale.pack(pady=10)

# Button to apply font changes
apply_button = tk.Button(main_window, text="Apply Font", command=change_font, font=("Rockybilly", 5))
apply_button.pack(pady=10)

# Label to demonstrate the selected font
text_label = tk.Label(main_window, text="ABCDEFGHIKLMNOPQRSTUVWXYZ \n abcdefghijklmnopqrstwxyz", font=("Arial", 12))
text_label.pack(pady=10)

main_window.mainloop()
    