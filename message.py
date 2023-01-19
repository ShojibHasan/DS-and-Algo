import pyautogui
import time
time.sleep(4)
count =0
while count<=100:
    pyautogui.typewrite("I'm smq")
    pyautogui.press("enter")
    count+=1