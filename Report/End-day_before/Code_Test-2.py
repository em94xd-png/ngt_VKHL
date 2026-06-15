import pyautogui
import time
from datetime import date, timedelta
import os
from selenium import webdriver

# Clear report store
# pyautogui.press("win", interval=.01)

Endday_before_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before"

# pyautogui.write(Endday_before_folder)
# time.sleep(1)
# pyautogui.press("enter", interval=.01)
# time.sleep(1)
# pyautogui.press("tab", presses=13, interval=.01)
# pyautogui.hotkey("ctrl", "a", interval=.01)
# pyautogui.press("del", interval=.01)
# pyautogui.hotkey("ctrl", "w", interval=.01)

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

# Open Opera
pyautogui.press("win")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

pyautogui.write(site_OPERA)
time.sleep(0.5)
pyautogui.press("enter")

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

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

# Report: Rebate and Correction Transactions
pyautogui.write("Journal by Cashier and Transaction Code", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Rebate and Correction Transactions: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", interval=0.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=4, interval=0.01)
time.sleep(1)
pyautogui.press("delete", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.press("space", interval=0.01) # Negative Postings Only
pyautogui.press("tab", presses=13, interval=0.01)