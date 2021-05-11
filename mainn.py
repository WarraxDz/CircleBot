import pyautogui
import math
import time
pyautogui.FAILSAFE = True
r = 380
(x, y) = pyautogui.size()
(x, y) = pyautogui.position(x/2, y/2-20)
def center():
    pyautogui.moveTo(x, y)
time.sleep(3)
print(x, y)
pyautogui.moveTo(x+r, y)
pyautogui.mouseDown();
for i in range(0, 450):
    if i % 180 == 0:
        pyautogui.moveTo(x+r*math.cos(math.radians(i)), y+r*math.sin(math.radians(i)))

pyautogui.moveRel(0, 100, duration=1)
pyautogui.mouseUp();