import pyautogui
import time
from datetime import date, timedelta
import os
from selenium import webdriver

Endday_before_folder = r"C:\Users\%USERPROFILE%\Documents\Runit\Report\End-day_before"

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

# Clear report store
pyautogui.hotkey("win", "e", interval=.01)
time.sleep(1)
# pyautogui.hotkey("ctrl", "f", interval=.01)
# tab_reserve(2)
# pyautogui.write(Endday_before_folder)
# pyautogui.press("enter", interval=.01)
# time.sleep(1)
# pyautogui.press("tab", presses=13, interval=.01)
# pyautogui.hotkey("ctrl", "a", interval=.01)
# pyautogui.press("del", interval=.01)
# pyautogui.hotkey("ctrl", "w", interval=.01)

# # Open Opera
# pyautogui.press("win")
# pyautogui.write(site_OPERA)
# time.sleep(0.5)
# pyautogui.press("enter")

# # In Opera  
# time.sleep(1)
# pyautogui.hotkey("win", "up", "down", "up" ,interval=.1)
# time.sleep(0.1)
# pyautogui.hotkey("ctrl", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",)
# pyautogui.hotkey("ctrl", "=", "=", "=",)
# time.sleep(5)