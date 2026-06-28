import subprocess
import pyautogui
import time
from datetime import date, timedelta
import os

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

def report_path():
    yesterday = date.today() - timedelta(days=1)
    ytd_date = yesterday.strftime("%#d")
    ytd_month_number = yesterday.strftime("%#m")
    ytd_month_short = yesterday.strftime("%b")
    ytd_month_full = yesterday.strftime("%B")
    ytd_year_full = yesterday.strftime("%Y")

    return fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}"

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

def report_print(report_name):                                  

    Endday_before_folder = report_path()

    folder_report = os.path.join(Endday_before_folder, report_name).__add__(".PDF")

    print_url_add = "file:" + folder_report.replace("\\", "/")

    subprocess.run(["cmd", "/c", "start", "msedge", print_url_add])

def page_print(set_copy, set_both, set_page):
    pyautogui.hotkey("ctrl", "p", interval=.01)
    time.sleep(1)
    pyautogui.press("tab", presses=(set_copy), interval=.01)

    if set_copy == 1:
        pyautogui.press("tab", presses=5, interval=.01)
    elif set_copy == 2:
        pyautogui.press("tab", interval=.01)
        pyautogui.write("2", interval=.01)
        pyautogui.press("tab", presses=4, interval=.01)

    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(set_both), interval=.01)
    pyautogui.press("tab", interval=.01)
    pyautogui.press("enter", interval=.01)
    time.sleep(.01)
    pyautogui.press("tab", presses=3, interval=.01)
    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(set_page), interval=.01)
    pyautogui.press("tab", presses=3, interval=.01)
    time.sleep(.5)
    pyautogui.press("enter", interval=.01)
    pyautogui.hotkey("ctrl", "w", interval=.01)

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

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

# # VKHL Arrivals
# pyautogui.write("Arrivals: Detailed FO", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(3)
# pyautogui.press("tab", presses=9, interval=.01)
# pyautogui.press("down", presses=2, interval=.01)
# time.sleep(1.5)
# pyautogui.press("right", interval=.01)
# pyautogui.press("tab", presses=3, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(3.5)
# # VKHL Arrivals: Config
# pyautogui.hotkey("ctrl", "a", interval=.01)
# pyautogui.write(format1_today(), interval=.01)
# pyautogui.press("tab", presses=2, interval=.01)
# time.sleep(1)
# pyautogui.write(format1_today(), interval=.01)
# pyautogui.press("tab", presses=4, interval=.01)
# time.sleep(.75)
# pyautogui.write(Room_Type, interval=.01)
# pyautogui.press("tab", presses=38, interval=.01)
# pyautogui.press("delete", interval=.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=11, interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(10)
# # VKHL Arrivals: Print
# pyautogui.click(600, 84, interval=0.01)
# time.sleep(.5)
# page_print(1, 1, 1)
# tab_reserve(3)
# pyautogui.press("enter", interval=0.01)
# time.sleep(5)
# pyautogui.press("tab", interval=0.01)

# # VKHL Departures
# pyautogui.write("departure_all", interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(3)
# pyautogui.press("tab", presses=9, interval=0.01)
# pyautogui.press("down", presses=2, interval=0.01)
# time.sleep(1.5)
# pyautogui.press("right", interval=.01)
# pyautogui.press("tab", presses=3, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(3.5)
# # VKHL Departures: Config
# pyautogui.press("tab", presses=3, interval=0.01)
# time.sleep(.75)
# pyautogui.write(Room_Type, interval=.01)
# pyautogui.press("tab", presses=10, interval=.01)
# pyautogui.press("space", interval=.01) # Pseudo Rooms
# pyautogui.press("tab", presses=12, interval=.01)
# pyautogui.press("space", interval=.01) # Membership Type
# time.sleep(.5)
# pyautogui.press("tab", interval=.01)
# pyautogui.press("space", interval=.01) # Membership Level
# time.sleep(.5)
# pyautogui.press("tab", presses=13, interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(8.5)
# # VKHL Departures: Print
# pyautogui.click(600, 84, interval=0.01)
# time.sleep(.5)
# page_print(1, 1, 1)
# tab_reserve(3)
# pyautogui.press("enter", interval=0.01)
# time.sleep(5)
# pyautogui.press("tab", interval=0.01)

# # VKHL Guests INH
# pyautogui.write("gibyroom", interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(3)
# pyautogui.press("tab", presses=9, interval=0.01)
# pyautogui.press("down", presses=2, interval=0.01)
# time.sleep(1.5)
# pyautogui.press("right", interval=.01)
# pyautogui.press("tab", presses=3, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(3.5)
# # VKHL Guests INH: Config
# pyautogui.press("tab", interval=.01)
# time.sleep(.75)
# pyautogui.write(Room_Type, interval=.01)
# pyautogui.press("tab", presses=14, interval=.01)
# pyautogui.press("space", interval=.01) # Include Internal Notes
# pyautogui.press("tab", interval=.01)
# pyautogui.write("Resv. - GEN", interval=.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=8, interval=.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(12.5)
# # VKHL Guests INH: Print
# pyautogui.click(600, 84, interval=0.01)
# time.sleep(.5)
# page_print(1, 1, 1)
# tab_reserve(3)
# pyautogui.press("enter", interval=0.01)
# time.sleep(5)
# pyautogui.press("tab", interval=0.01)

# Package Forecast
pyautogui.write("Package Forecast - Detailed", interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Package Forecast: Config
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.write(format1_today(), interval=.01)
pyautogui.press("tab", interval=0.01)
time.sleep(1)
pyautogui.write(format1_today(), interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
time.sleep(.75)
pyautogui.write("BFB01E,BFB01I,BFB02E,BFB02I,BFB03I,BFB04I", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Package Forecast: Print
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
page_print(1, 1, 1)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
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
pyautogui.press("tab", presses=15, interval=.01)
pyautogui.press("delete", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(12.5)
# VKHL Guests INH (Full): Print
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
page_print(2, 1, 1)

VKHL_Arrivals = "4. VKHL Arrivals"

report_print(VKHL_Arrivals)
time.sleep(.5)
page_print(1, 1, 1)

VKHL_Departures = "5. VKHL Departures"

report_print(VKHL_Departures)
time.sleep(.5)
page_print(1, 1, 1)

VKHL_Guests_INH = "6. VKHL Guests INH"

report_print(VKHL_Guests_INH)
time.sleep(.5)
page_print(1, 1, 1)