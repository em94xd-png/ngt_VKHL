import pyautogui
import time
from datetime import date, timedelta
import os
import calendar
import subprocess

Endday_after_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_after")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

def date_first():
    today = date.today()
    today_1 = today.replace(day=1)
    return today_1.strftime("%d%m")

def date_end():
    today = date.today()

    _, last_day = calendar.monthrange(today.year, today.month)
    month_end = today.replace(day=last_day)
    return month_end.strftime("%d%m")

# Clear report store
os.startfile(Endday_after_folder)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.press("del", interval=.01)
pyautogui.hotkey("ctrl", "w", interval=.01)

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", site_OPERA])

# In Opera  
time.sleep(1)
pyautogui.hotkey("win", "up", "down", "up" ,interval=.1)
time.sleep(0.1)
pyautogui.hotkey("ctrl", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",)
pyautogui.hotkey("ctrl", "=", "=", "=",)
time.sleep(5)

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(4.5)
pyautogui.press("tab", interval=0.01)

# Reservation Cancellations
pyautogui.write("rescancel", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# Reservation Cancellations: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=2, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=18, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Reservation Cancellations: Save
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_after_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Reservation_Cancellations = "Reservation Cancellations"

pyautogui.write(Reservation_Cancellations, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
