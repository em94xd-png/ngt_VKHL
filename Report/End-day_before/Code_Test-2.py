import subprocess
import os
import pyautogui
import time

Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_before")

os.startfile(Endday_before_folder)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)         