# # import pandas as pd

# # # Define rows and columns
# # rows = [(1, 'matty', 28), (2, 'chris', 51), (3, 'sophie', 7)]
# # columns = ['test_id', 'name', 'age']

# # # Create a pandas DataFrame
# # pandasdf = pd.DataFrame(rows, columns=columns)
# # print(pandasdf)

# # for i in range(len(pandasdf)):
# #     print(pandasdf.iloc[i])

# from tkinter import *
# from tkinter import font

# root = Tk()
# root.title('Font Families')
# fonts=list(font.families())
# fonts.sort()

# def populate(frame):
#     '''Put in the fonts'''
#     listnumber = 1
#     for i, item in enumerate(fonts):
#         label = "listlabel" + str(listnumber)
#         label = Label(frame,text=item,font=(item, 16))
#         label.grid(row=i)
#         label.bind("<Button-1>",lambda e,item=item:copy_to_clipboard(item))
#         listnumber += 1

# def copy_to_clipboard(item):
#     root.clipboard_clear()
#     root.clipboard_append("font=('" + item.lstrip('@') + "', 12)")

# def onFrameConfigure(canvas):
#     '''Reset the scroll region to encompass the inner frame'''
#     canvas.configure(scrollregion=canvas.bbox("all"))

# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame)

# root.mainloop()

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# Example dictionary
data = {0: 10001, 1: 30004, 2: 15002, 3: 44998, 4: 22504, 5: 67498, 6: 33749, 7: 101248, 8: 50624, 9: 151630, 10: 75815, 11: 227446, 12: 113723, 13: 341170, 14: 170585, 15: 511756, 16: 255878, 17: 747952, 18: 383818, 19: 1062880, 20: 575728, 21: 1417174, 22: 835918, 23: 2125762, 24: 1253878, 25: 3188644, 26: 1880818, 27: 959092, 28: 2821228, 29: 1417174, 30: 719320, 31: 2125762, 32: 1062881, 33: 3188644, 34: 1594322, 35: 4035634, 36: 2391484, 37: 6053452, 38: 3570622, 39: 1793614, 40: 5355934, 41: 2690422, 42: 8033902, 43: 4035634, 44: 12050854, 45: 6053452, 46: 18076282, 47: 9038141, 48: 27114424, 49: 13557212, 50: 6810136, 51: 3405068, 52: 10167910, 53: 5083955, 54: 15251866, 55: 7625933, 56: 22877800, 57: 11438900, 58: 5719450, 59: 8153620, 60: 8579176, 61: 4289588, 62: 8153620, 63: 6115216, 64: 3217192, 65: 8153620, 66: 4076810, 67: 2391484, 68: 6115216, 69: 3188644, 70: 1793614, 71: 3188644, 72: 2690422, 73: 1345211, 74: 4035634, 75: 2017817, 76: 6053452, 77: 3026726, 78: 6053452, 79: 4540090, 80: 6053452, 81: 6810136, 82: 3405068, 83: 6810136, 84: 4540090, 85: 6810136, 86: 6810136, 87: 3830704, 88: 6810136, 89: 3830704, 90: 2553802, 91: 3830704, 92: 3830704, 93: 1915352, 94: 3830704, 95: 1915352, 96: 1077388, 97: 808042, 98: 1077388, 99: 1212064, 100: 606032, 101: 1212064, 102: 808042, 103: 1212064, 104: 1212064, 105: 606032, 106: 1212064, 107: 606032, 108: 303016, 109: 250504, 110: 150496, 111: 150496, 112: 167002, 113: 150496, 114: 250504, 115: 150496, 116: 250504, 117: 167002, 118: 250504, 119: 250504, 120: 250504, 121: 250504, 122: 250504, 123: 125252, 124: 250504, 125: 167002, 126: 250504, 127: 250504, 128: 250504, 129: 250504, 130: 167002, 131: 100330, 132: 250504, 133: 150496, 134: 75248, 135: 167002, 136: 111334, 137: 250504, 138: 167002, 139: 83501, 140: 250504, 141: 125252, 142: 150496, 143: 150496, 144: 150496, 145: 150496, 146: 150496, 147: 75248, 148: 150496, 149: 100330, 150: 150496, 151: 150496, 152: 150496, 153: 150496, 154: 100330, 155: 59452, 156: 150496, 157: 75248, 158: 71440, 159: 100330, 160: 71440, 161: 150496, 162: 100330, 163: 50165, 164: 150496, 165: 75248, 166: 71440, 167: 71440, 168: 47626, 169: 23813, 170: 71440, 171: 35720, 172: 21166, 173: 47626, 174: 31750, 175: 71440, 176: 47626, 177: 23813, 178: 71440, 179: 35720, 180: 17860, 181: 8930, 182: 4465, 183: 13396, 184: 6698, 185: 3349, 186: 10048, 187: 5024, 188: 2512, 189: 7288, 190: 3644, 191: 7288, 192: 4858, 193: 7288, 194: 7288, 195: 4858, 196: 2429, 197: 7288, 198: 3644, 199: 9232, 200: 4858, 201: 9232, 202: 7288, 203: 9232, 204: 9232, 205: 6154, 206: 3077, 207: 9232, 208: 4616, 209: 9232, 210: 6154, 211: 3238, 212: 9232, 213: 4858, 214: 2429, 215: 7288, 216: 3644, 217: 9232, 218: 4616, 219: 2734, 220: 6154, 221: 4102, 222: 9232, 223: 6154, 224: 3077, 225: 9232, 226: 4616, 227: 9232, 228: 4616, 229: 2308, 230: 1732, 231: 866, 232: 1732, 233: 1300, 234: 650, 235: 1300, 236: 976, 237: 488, 238: 976, 239: 488, 240: 244, 241: 184, 242: 92, 243: 184, 244: 106, 245: 70, 246: 160, 247: 106, 248: 53, 249: 160, 250: 80, 251: 160, 252: 80, 253: 40, 254: 20, 255: 16, 256: 5, 257: 16}


# Split into keys and values
keys_list = list(data.keys())  # Convert keys to a list
values_list = list(data.values())  # Convert values to a list

print("Keys:", keys_list)
print("Values:", values_list)

def create_plot(frame):
    # Create a Matplotlib figure
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(keys_list, values_list)  # Example data
    ax.set_title("Example Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Embed the Matplotlib figure into the Tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=False, padx=10, pady=10)

    # (Optional) Add Matplotlib's navigation toolbar
    toolbar = ttk.Frame(frame)
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    toolbar_widget = canvas.get_tk_widget()
    toolbar_widget.pack()

# Create main Tkinter window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a frame for the graph
graph_frame = ttk.Frame(root, width=600, height=400)
graph_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create and display the plot in the frame
create_plot(graph_frame)

root.mainloop()

