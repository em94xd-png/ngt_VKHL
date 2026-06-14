import pyautogui
import time
from datetime import date, timedelta
import os
from selenium import webdriver

# Open Opera
pyautogui.press("win")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"
pyautogui.write(site_OPERA)
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

Endday_before_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before"

pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Room_Discrepancy = "Room Discrepancy"

pyautogui.write(Room_Discrepancy)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)

def print_it(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    pyautogui.press('tab', presses=6, interval=.01)
    pyautogui.press('up', presses=2, interval=.01)
    pyautogui.press('tab', interval=.01)
    pyautogui.press('enter', interval=.01)
    pyautogui.press('tab', presses=3, interval=.01)
    pyautogui.press('up', presses=2, interval=.01)
    pyautogui.press('tab', presses=3, interval=.01)
    pyautogui.press('enter', interval=.01)

file_local = os.path.join(Endday_before_folder, Room_Discrepancy)
file_url = "file:///" + os.path.abspath(file_local).replace("\\", "/").__add__(".PDF") # Convert your local absolute file path into a file:// URL structure

print_it(file_url)