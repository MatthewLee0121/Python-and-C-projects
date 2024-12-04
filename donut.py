import subprocess
import time
import pyautogui
import sys
import random

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
url = "https://pump.fun/coin/EU3ufF1LFqUvS1Qg8g3JsSYpmQE3AQSGwZQzgBZKpump"

subprocess.run([chrome_path, url])

time.sleep(5)

pyautogui.press('end')

time.sleep(1)

pyautogui.moveTo(1102, 1242) 

pyautogui.click()

pyautogui.moveTo(1203, 518) 

time.sleep(1)

text = "ZOOOOOOOOOOOOOOOL TO THE MOON"


for char in text:
    pyautogui.write(char)
    random_interval = random.uniform(0.1, 0.3)
    pyautogui.sleep(random_interval)

pyautogui.click()

pyautogui.moveTo(1267, 955) 

pyautogui.click()