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

def format1_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

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

# print(pyautogui.position())
pyautogui.click(x=72, y=304, interval=.01)

# To End of Day Reports
tab_reserve(7)
pyautogui.press("left", presses=2, interval=.01)
pyautogui.press("down", presses=3, interval=.01)
pyautogui.press("right", presses=1, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=2, interval=.01)

# Guest Ledger Detail
pyautogui.write("gl_led_de", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("down", interval=.01)
pyautogui.press("enter", presses=3, interval=1)
time.sleep(5)
# Guest Ledger Detail: Save
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

Guest_Ledger_Detail = "14. Guest Ledger Detail"

pyautogui.write(Guest_Ledger_Detail, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(1)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
tab_reserve(9)

# Manager Flash
pyautogui.write("manager", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("down", interval=.01)
pyautogui.press("enter", presses=3, interval=1)
time.sleep(5)
# Manager Flash: Save
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

Manager_Flash = "8. Manager Flash"

pyautogui.write(Manager_Flash, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(1)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
tab_reserve(9)

# Trial Balance
pyautogui.write("tb", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("down", interval=.01)
pyautogui.press("enter", presses=3, interval=1)
time.sleep(5)
# Trial Balance: Save
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

Trial_Balance = "9. Trial Balance"

pyautogui.write(Trial_Balance, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(1)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
tab_reserve(9)

# No Show
pyautogui.write("noshow", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("down", interval=.01)
pyautogui.press("enter", presses=3, interval=1)
time.sleep(5)
# No Show: Save
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

No_Show = f"11. No Show on {format1_yesterday()}"

pyautogui.write(No_Show, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)                             
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)