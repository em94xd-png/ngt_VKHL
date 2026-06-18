import os
import pyautogui
import time
import subprocess
from datetime import date, timedelta

Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_before")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def format1_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

# # Open Opera
# subprocess.run(["cmd", "/c", "start", "msedge", site_OPERA])

# # In Opera  
# time.sleep(1)
# pyautogui.hotkey("win", "up", "down", "up" ,interval=.1)
# time.sleep(0.1)
# pyautogui.hotkey("ctrl", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",)
# pyautogui.hotkey("ctrl", "=", "=", "=",)
# time.sleep(5)

# # To report search
# pyautogui.press("tab", presses=5, interval=0.01)
# pyautogui.press("right", presses=6, interval=0.01)
# pyautogui.press("down", interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(4.5)
# pyautogui.press("tab", interval=0.01)

def report_print(report_name):                                  

    Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_before")

    folder_report = os.path.join(Endday_before_folder, report_name).__add__(".PDF")

    print_url_add = "file:///" + folder_report.replace("\\", "/")

    subprocess.run(["cmd", "/c", "start", "msedge", print_url_add])

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

Room_Discrepancy = "Room Discrepancy"

report_print(Room_Discrepancy)
time.sleep(.5)
page_print(0)