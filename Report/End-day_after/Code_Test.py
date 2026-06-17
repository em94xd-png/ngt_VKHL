import pyautogui
import time
from datetime import date
import calendar

Endday_after_folder = r"C:\Users\%USERPROFILE%\Documents\Runit\Report\End-day_after"

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

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
pyautogui.hotkey("win", "e", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
pyautogui.write(Endday_after_folder)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.press("del", interval=.01)
pyautogui.hotkey("ctrl", "w", interval=.01)

# Open Opera
pyautogui.press("win")
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

# History and Forecast
pyautogui.write("History and Forecast FO", interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# History and Forecast: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(date_first(), interval=.01)
pyautogui.press("tab", interval=.01)
time.sleep(1)
pyautogui.write(date_end(), interval=.01)
pyautogui.press("tab", presses=20, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# History and Forecast: Save
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
pyautogui.press("tab", presses=7, interval=.01)

History_and_Forecast = "7. History and Forecast"

pyautogui.write(History_and_Forecast, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")

# History and Forecast (AVC)
time.sleep(.1)
# History and Forecast (AVC): Config
tab_reserve(14)
pyautogui.press("space", interval=.01) # Pseudo Rooms
time.sleep(1)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# History and Forecast (AVC): Save
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
pyautogui.press("tab", presses=7, interval=.01)

History_and_Forecast_AVC = "7. History and Forecast (AVC)"

pyautogui.write(History_and_Forecast_AVC, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)