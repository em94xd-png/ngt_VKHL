import pyautogui
import time
from datetime import date, timedelta
import os
import calendar
import subprocess
import pygetwindow

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

Room_Class = "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC"

def report_path():
    yesterday = date.today() - timedelta(days=1)
    ytd_date = yesterday.strftime("%#d")
    ytd_month_number = yesterday.strftime("%#m")
    ytd_month_short = yesterday.strftime("%b")
    ytd_month_full = yesterday.strftime("%B")
    ytd_year_full = yesterday.strftime("%Y")

    return fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}"

def tab_reserve(times):
    pyautogui.PAUSE = 0.01
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

    Endday_after_folder = report_path()

    folder_report = os.path.join(Endday_after_folder, report_name).__add__(".PDF")

    print_url_add = "file:" + folder_report.replace("\\", "/")

    subprocess.run(["cmd", "/c", "start", "msedge", print_url_add])

def file_remove(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)

pyautogui.FAILSAFE = True

# Delete files
file_remove(report_path())

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", site_OPERA])

pygetwindow.getWindowsWithTitle("Opera Cloud")[0].maximize()

time.sleep(.5)

def first_OPERA_open():
    while True:
        if pyautogui.pixelMatchesColor(7, 391, (244, 243, 239), tolerance=0):
            break

first_OPERA_open()

# In Opera
def zoom_out(_):
    pyautogui.PAUSE = .01
    for _ in range(_):
        pyautogui.hotkey("ctrl", "-")

zoom_out(10)

def zoom_in(_):
    pyautogui.PAUSE = .01
    for _ in range(_):
        pyautogui.hotkey("ctrl", "=")

zoom_in(3)

def main_OPERA_menu():
    while True:
        if pyautogui.pixelMatchesColor(139, 129, ( 70,  70,  68), tolerance=0):
            break

main_OPERA_menu()

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)

def search_reports():
    while True:
        if pyautogui.pixelMatchesColor(252, 245, (88, 88, 86), tolerance=0):
            break
    
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# VKHL Arrivals
pyautogui.write("Arrivals: Detailed FO", interval=.01)
pyautogui.press("enter", interval=.01)

def search_enter_step1():
    while True:
        if pyautogui.pixelMatchesColor(1854, 337, (204, 204, 204), tolerance=10):
            break

def search_enter_step2():
    while True:
        if pyautogui.pixelMatchesColor(1854, 337, (6, 108, 122), tolerance=0):
            break

search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=.01)
# VKHL Arrivals: Config

def config_report():
    while True:
        if pyautogui.pixelMatchesColor(214, 244, (255, 255, 255), tolerance=0):
            break

config_report()
time.sleep(1)
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
# VKHL Arrivals: Save

def wait_report():
    while True:
        if pyautogui.pixelMatchesColor(1866, 975, (213, 163, 160), tolerance=10):
            break

wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
pyautogui.press("tab", presses=5, interval=.01)

VKHL_Arrivals = "4. VKHL Arrivals"

pyautogui.write(VKHL_Arrivals, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)

# VKHL Guests INH (Comp)
tab_reserve(54)
# VKHL Guests INH (Comp): Config
pyautogui.press("right", interval=0.01)
pyautogui.press("tab", presses=4, interval=0.01)
time.sleep(1)
pyautogui.write(Room_Class, interval=.01)
pyautogui.press("tab", interval=0.01)
pyautogui.press("delete", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("space", interval=0.01) # Zero Rates Only
time.sleep(.5)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.press("space", interval=0.01) # Departures
time.sleep(.5)
pyautogui.press("tab", presses=33, interval=0.01)
pyautogui.press("enter", interval=0.01)
# VKHL Guests INH (Comp): Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

VKHL_Guests_INH_Comp = "6. VKHL Guests INH (Comp)"

pyautogui.write(VKHL_Guests_INH_Comp, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# VKHL Departures
pyautogui.write("departure_all", interval=.01)
pyautogui.press("enter", interval=0.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# VKHL Departures: Config
config_report()
time.sleep(1)
pyautogui.press("tab", presses=3, interval=0.01)
time.sleep(.75)
pyautogui.write(Room_Type, interval=.01)
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
time.sleep(.5)
pyautogui.press("tab", presses=12, interval=.01)
pyautogui.press("space", interval=.01) # Membership Type
time.sleep(.75)
pyautogui.press("tab", interval=.01)
pyautogui.press("space", interval=.01) # Membership Level
time.sleep(.75)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=0.01)
# VKHL Departures: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# VKHL Guests INH
pyautogui.write("gibyroom", interval=.01)
pyautogui.press("enter", interval=0.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# VKHL Guests INH: Config
config_report()
time.sleep(1)
pyautogui.press("tab", interval=.01)
time.sleep(.75)
pyautogui.write(Room_Type, interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("space", interval=.01) # Include Internal Notes
time.sleep(.5)
pyautogui.press("tab", interval=.01)
pyautogui.write("Resv. - GEN", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("enter", interval=0.01)
# VKHL Guests INH: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

VKHL_Guests_INH = "6. VKHL Guests INH"

pyautogui.write(VKHL_Guests_INH, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)

# VKHL VIP Guests INH
tab_reserve(19)
# VKHL VIP Guests INH: Config
pyautogui.press("space", interval=.01) # VIP Only
time.sleep(1)
pyautogui.press("tab", presses=20, interval=.01)
pyautogui.press("enter", interval=0.01)
# VKHL VIP Guests INH: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# History and Forecast
pyautogui.write("History and Forecast FO", interval=.01)
pyautogui.press("enter", interval=0.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# History and Forecast: Config
config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(date_first(), interval=.01)
pyautogui.press("tab", interval=.01)
time.sleep(1)
pyautogui.write(date_end(), interval=.01)
pyautogui.press("tab", presses=20, interval=0.01)
pyautogui.press("enter", interval=0.01)
# History and Forecast: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

History_and_Forecast = "7. History and Forecast"

pyautogui.write(History_and_Forecast, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)

# History and Forecast (AVC)
# History and Forecast (AVC): Config
tab_reserve(14)
pyautogui.press("space", interval=.01) # Pseudo Rooms
time.sleep(.5)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=0.01)
# History and Forecast (AVC): Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Market Segment Statistics
pyautogui.write("stat_dmy_seg", interval=.01)
pyautogui.press("enter", interval=.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=.01)
# Market Segment Statistics: Config
config_report()
time.sleep(1)
pyautogui.press("tab", interval=.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=17, interval=.01)
pyautogui.press("enter", interval=0.01)
# Market Segment Statistics: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# AR Credit Limit
pyautogui.write("ar_balance", interval=.01)
pyautogui.press("enter", interval=.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
# AR Credit Limit: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
tab_reserve(13)

# Vacant Rooms
pyautogui.write("Vacant Rooms", interval=.01)
pyautogui.press("enter", interval=.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=.01)
# Vacant Rooms: Config
config_report()
time.sleep(1)
pyautogui.press("tab", interval=.01)
time.sleep(.75)
pyautogui.write("1H4XK,1H4XT,2U2XKT,2U3XKT", interval=.01)
pyautogui.press("tab", presses=15, interval=.01)
pyautogui.press("enter", interval=0.01)
# Vacant Rooms: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Reservation Cancellations
pyautogui.write("rescancel", interval=.01)
pyautogui.press("enter", interval=.01)
search_enter_step1()
search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=.01)
# Reservation Cancellations: Config
config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=2, interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=18, interval=.01)
pyautogui.press("enter", interval=.01)
# Reservation Cancellations: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
search_reports()
time.sleep(1)

# To End of Day Reports
tab_reserve(7)
pyautogui.press("left", presses=2, interval=.01)
pyautogui.press("down", interval=.01)
time.sleep(.5)
pyautogui.press("down", presses=2, interval=.01)
pyautogui.press("right", presses=1, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2)                             
pyautogui.press("tab", presses=2, interval=.01)

# Guest Ledger Detail
pyautogui.write("gl_led_de", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("down", interval=.01)
pyautogui.press("enter", presses=3, interval=1)
# Guest Ledger Detail: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
# Manager Flash: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
time.sleep(.1)
pyautogui.press("enter", presses=3, interval=1)
# Trial Balance: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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
# No Show: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path())
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