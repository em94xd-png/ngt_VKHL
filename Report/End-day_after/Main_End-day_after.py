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

def report_print(report_name):

    Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_after")

    folder_report = os.path.join(Endday_before_folder, report_name).__add__(".PDF")

    print_url_add = "file:///" + folder_report.replace("\\", "/")

    subprocess.run(["cmd", "/c", "start", "msedge", print_url_add])

# Clear report store
os.startfile(Endday_after_folder)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.press("delete", interval=.01)
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

# VKHL Arrivals
pyautogui.write("Arrivals: Detailed FO", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# VKHL Arrivals: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format1_today(), interval=.01)
pyautogui.press("tab", presses=2, interval=.01)
time.sleep(1)
pyautogui.write(format1_today(), interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
time.sleep(.75)
pyautogui.write(Room_Type, interval=.01)
pyautogui.press("tab", presses=38, interval=.01)
pyautogui.press("delete", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=11, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(10)
# VKHL Arrivals: Save
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
time.sleep(1)
pyautogui.press("tab", presses=6, interval=.01)

VKHL_Arrivals = "4. VKHL Arrivals"

pyautogui.write(VKHL_Arrivals, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# VKHL Departures
pyautogui.write("departure_all", interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# VKHL Departures: Config
pyautogui.press("tab", presses=3, interval=0.01)
time.sleep(.75)
pyautogui.write(Room_Type, interval=.01)
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
pyautogui.press("tab", presses=12, interval=.01)
pyautogui.press("space", interval=.01) # Membership Type
time.sleep(.5)
pyautogui.press("tab", interval=.01)
pyautogui.press("space", interval=.01) # Membership Level
time.sleep(.5)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# VKHL Departures: Save
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

VKHL_Departures = "5. VKHL Departures"

pyautogui.write(VKHL_Departures, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# VKHL Guests INH
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
# VKHL Guests INH: Config
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
pyautogui.press("tab", presses=2, interval=.01)
pyautogui.write("Resv. - GEN", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=7, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(12.5)
# VKHL Guests INH: Save
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

VKHL_Guests_INH = "6. VKHL Guests INH"

pyautogui.write(VKHL_Guests_INH, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")

# VKHL VIP Guests INH
time.sleep(0.1)
# VKHL VIP Guests INH: Config
tab_reserve(19)
pyautogui.press("space", interval=.01) # VIP Only
time.sleep(1)
pyautogui.press("tab", presses=20, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# VKHL VIP Guests INH: Save
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

VKHL_VIP_Guests_INH = "3. VKHL VIP Guests INH"

pyautogui.write(VKHL_VIP_Guests_INH, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# History and Forecast
pyautogui.write("History and Forecast FO", interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3)
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
pyautogui.press("tab", presses=6, interval=.01)

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
pyautogui.press("tab", presses=6, interval=.01)

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

# Market Segment Statistics
pyautogui.write("stat_dmy_seg", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# Market Segment Statistics: Config
pyautogui.press("tab", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=17, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Market Segment Statistics: Save
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

Market_Segment_Statistics = "10. Market Segment Statistics"

pyautogui.write(Market_Segment_Statistics, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# AR Credit Limit
pyautogui.write("ar_balance", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# AR Credit Limit: Save
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

AR_Credit_Limit = "16. AR Credit Limit"

pyautogui.write(AR_Credit_Limit, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)

# Vacant Rooms
pyautogui.write("Vacant Rooms", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# Vacant Rooms: Config
pyautogui.press("tab", interval=.01)
time.sleep(.75)
pyautogui.write("1H4XK,1H4XT,2U2XKT,2U3XKT", interval=.01)
pyautogui.press("tab", presses=15, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Vacant Rooms: Save
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

Vacant_Rooms = "18. Vacant Rooms"

pyautogui.write(Vacant_Rooms, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# Reservation Cancellations
pyautogui.write("rescancel", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3)
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
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
time.sleep(5)

# To End of Day Reports
tab_reserve(7)
pyautogui.press("left", presses=2, interval=.01)
pyautogui.press("down", interval=.01)
time.sleep(.5)
pyautogui.press("down", presses=2, interval=.01)
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

# Open 4. VKHL Arrivals
report_print(VKHL_Arrivals)
time.sleep(.5)
pyautogui.press("end", interval=.01)