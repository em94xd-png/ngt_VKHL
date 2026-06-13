import pyautogui
import time
from datetime import date, timedelta
import os
from selenium import webdriver

# Open Opera
pyautogui.press("win")
pyautogui.write(
    "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"
)
time.sleep(0.5)
pyautogui.press("enter")

# In Opera  
time.sleep(1)
pyautogui.hotkey("win", "up")
pyautogui.hotkey("win", "down")
pyautogui.hotkey("win", "up")

time.sleep(0.1)

# Zoom out
def zoom_out(times):
    for _ in range(times):
        pyautogui.hotkey("ctrl", "-")

# Zoom in
def zoom_in(times):
    for _ in range(times):
        pyautogui.hotkey("ctrl", "=")

zoom_out(10)
zoom_in(3)
time.sleep(5)

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(4.5)
pyautogui.press("tab", interval=0.01)

# Report: Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Report: Room Discrepancy: Save
pyautogui.click(600,84, interval=.01)
pyautogui.press("tab", presses=17, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)

def find_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

find_reserve(2)
time.sleep(0.1)

pyautogui.press("enter", interval=.01)
pyautogui.write(r"D:\Users\fo.vkhl\Documents\Runit")
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)
pyautogui.write("Room Discrepancy")
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)

def print_it(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    # Trigger print asynchronously so Python doesn't freeze
    driver.execute_script("setTimeout(function() { window.print(); }, 0);")

    time.sleep(1)

    pyautogui.press('tab', presses=9, interval=.01)
    # pyautogui.press("enter")
    time.sleep(3)

# Convert your local absolute file path into a file:// URL structure
local_file = r"D:\Users\fo.vkhl\Documents\Runit\Room Discrepancy.PDF"
file_url = "file:///" + os.path.abspath(local_file).replace("\\", "/")

print_it(file_url)