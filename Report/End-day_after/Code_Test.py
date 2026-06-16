import pyautogui
import time
from datetime import date
from Code_Store import *

# Clear report store
Endday_before_folder = r"C:\Users\%USERPROFILE%\Documents\Runit\Report\End-day_before"

pyautogui.hotkey("win", "e", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

tab_reserve(2)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.press("del", interval=.01)
pyautogui.hotkey("ctrl", "w", interval=.01)