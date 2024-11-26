import pyautogui
import time
import random

def main():
    print("You have 2 seconds to focus on your main application...")
    time.sleep(2)
    
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
    time.sleep(1) 

    pyautogui.write("Hello World", interval=random.random()d)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    pyautogui.write("Hello vlad", interval=0.1)
    time.sleep(0.5)
    pyautogui.press('enter')
    
    screen_width, screen_height = pyautogui.size()
    pyautogui.click(screen_width // 2, screen_height // 2)

if __name__ == "__main__":
    main()
