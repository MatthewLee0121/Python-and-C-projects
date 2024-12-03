import pyautogui
from pynput.mouse import Listener

# Function that will be triggered on mouse click
def on_click(x, y, button, pressed):
    if pressed and button.name == 'left':  # Only on left-click
        print(f'Left Clicked at ({x}, {y})')

# Start the mouse listener
with Listener(on_click=on_click) as listener:
    listener.join()



# Left Clicked at (1102, 1242)
# Left Clicked at (1203, 518)
# Left Clicked at (1267, 955)