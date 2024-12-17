import pyautogui
import time


a = 255
c = 233
d = 228

while 1:
    x, y = pyautogui.position()
    r,g,b = pyautogui.pixel(x, y)
    print(r, g, b)
    
    time.sleep(1)
