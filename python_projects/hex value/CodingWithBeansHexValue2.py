import pyautogui
import tkinter as tk
import pyperclip

#defining globals
current_hex_value = "#4CAF50" #global variable for the hex value

#need to make a function for the current pixel value
def get_pixel_hex_value():
    try:
        x, y = pyautogui.position() #using pyautogui to grab the x y coordinates of the pointer
        pixel_value = pyautogui.pixel(x, y) #grab the pixel data at the x y coordinates of the mouse
        hex_value = "#{:02x}{:02x}{:02x}".format(*pixel_value) # converts rgb turple into hex 02x making sure rgb is converted into a hex value
        return hex_value # returns the above value
    except Exception as e: #statement to catch errors and assigns to e
        print(f"Error: {e}") #prints e
        return None

# need a function to announce the colour value
def update_colour_label():
    global current_hex_value #imports the global hex value
    hex_value = get_pixel_hex_value() #calls the function to get the hex value so we have an output
    if hex_value: #if statement to manipulate hex value
        current_hex_value = hex_value #updates the global variable after we have got a new value from the hex value
        colour_label.config(text=f'The colour at the pointer is: {hex_value}') #updates the colour label part of the UI
        window.configure(bg=current_hex_value) #sets tkinter ui background to the colour value for user friendliness was a pain copying to see the google result

# need a function to easily copy the value 
def copy_to_clipboard():
    global current_hex_value #imports the global variable
    try:  
        pyperclip.copy(current_hex_value) #using pyperclip to copy the value to clip board
    except Exception as e:
        print(f"Error: {e}")
    
#--------------------------------------UI----------------------------------------------------------------------
# Create tkinter
window = tk.Tk()#creates the window
window.title("Colour at Pointer Codingwithbeans") # names the title

# window parameters
window.geometry("500x300")  #resolution
window.configure(bg="#f0f0f0") #background

# make a label for the print statement to value
colour_label = tk.Label( 
    window, #sets label in the window window
    text="""Make sure the grabber is in focus
    Move your pointer and
    Hold R to get the colour.""", #gives some instructions when programe first launches
    font=("Helvetica", 14), #font for label 
    bg="#f0f0f0", #white background as this is contrast with most colours and can put black text
)
colour_label.pack(pady=20) # pad out the positioning

# close the programme button
close_button = tk.Button(
    window,
    text="Close",
    command=window.destroy,
    font=("Helvetica", 12),
    bg="#4CAF50",  # Green colour
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
)
close_button.pack(pady=5)

# button to copy
copy_button = tk.Button(
    window,
    text="Copy to Clipboard",
    command=copy_to_clipboard,
    font=("Helvetica", 12),
    bg="#008CBA",  # Blue colour
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
)
copy_button.pack(pady=5)

# making the colour select upon pressing the R key
window.bind('r', lambda event: update_colour_label())

# leee go
window.mainloop()