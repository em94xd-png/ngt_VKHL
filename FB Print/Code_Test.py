import subprocess
import pyautogui
import time
from datetime import date, timedelta

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

def page_print(times):
    pyautogui.hotkey("ctrl", "p", interval=.01)
    time.sleep(1)
    pyautogui.press("tab", presses=6, interval=.01)          
    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(times), interval=.01)
    pyautogui.press("tab", interval=.01)
    pyautogui.press("enter", interval=.01)
    time.sleep(.01)
    pyautogui.press("tab", presses=3, interval=.01)
    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(times), interval=.01)
    pyautogui.press("tab", presses=3, interval=.01)
    # pyautogui.press("enter", interval=.01)
    time.sleep(5)
    pyautogui.hotkey("ctrl", "w", interval=.01)

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

pyautogui.click(x=72, y=304, interval=.01)
pyautogui.press("tab", interval=0.01)

# VKHL Guests INH (Full)
pyautogui.write("gibyroom", interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# VKHL Guests INH (Full): Config
pyautogui.press("tab", interval=.01)
time.sleep(.75)
pyautogui.write(Room_Type, interval=.01)
pyautogui.press("tab", presses=5, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
pyautogui.press("tab", presses=5, interval=.01)
pyautogui.press("space", interval=.01) # Accompanying Names
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("space", interval=.01) # Notes
time.sleep(1)
pyautogui.press("tab", interval=.01)
pyautogui.press("space", interval=.01)
pyautogui.press("tab", presses=8, interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(12.5)
# # VKHL Guests INH (Full): Print
# pyautogui.click(600, 84, interval=0.01)
# time.sleep(.5)