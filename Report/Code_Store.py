import pyautogui
from datetime import date, timedelta
import calendar
import os
import subprocess
import time
import pygetwindow
import pyperclip
from urllib.parse import urlparse, parse_qs


site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_before")

Endday_after_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_after")

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

Room_Class = "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC"

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

def report_path():
    yesterday = date.today() - timedelta(days=1)
    ytd_date = yesterday.strftime("%#d")
    ytd_month_number = yesterday.strftime("%#m")
    ytd_month_short = yesterday.strftime("%b")
    ytd_month_full = yesterday.strftime("%B")
    ytd_year_full = yesterday.strftime("%Y")

    return fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def report_print(report_name):

    Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"..")

    folder_report = os.path.join(Endday_before_folder, report_name).__add__(".PDF")

    print_url_add = "file:///" + folder_report.replace("\\", "/")

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
    # pyautogui.press("enter", interval=.01)
    # pyautogui.hotkey("ctrl", "w", interval=.01)

def file_remove(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)

pyautogui.FAILSAFE = True
# pyautogui.displayMousePosition()

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", site_OPERA])

web_page = pygetwindow.getWindowsWithTitle("Opera Cloud")[0].maximize()

time.sleep(.5)

def first_open():
    while True:
        if pyautogui.pixelMatchesColor(7, 391, (244, 243, 239), tolerance=0):
            break

first_open()

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

def after_open():
    while True:
        if pyautogui.pixelMatchesColor(139, 129, ( 70,  70,  68), tolerance=0):
            break

after_open()

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)

def manage_reports():
    while True:
        if pyautogui.pixelMatchesColor(252, 245, (88, 88, 86), tolerance=0):
            break
    
manage_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Report: Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)

def search_report():
    while True:
        if pyautogui.pixelMatchesColor(267, 452, (244, 243, 239), tolerance=0):
            break

search_report()
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
# Report: Room Discrepancy: Save

def pdf_report():
    while True:
        if pyautogui.pixelMatchesColor(1866, 975, (213, 163, 160), tolerance=10):
            break

pdf_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=6, interval=.01)

Room_Discrepancy = "Room Discrepancy"

pyautogui.write(Room_Discrepancy, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
tab_reserve(13)

# Report: Guests INH Complimentary and Houseuse
pyautogui.write("gi_c_h", interval=.01)
pyautogui.press("enter", interval=.01)

def re_search_report():
    while True:
        if pyautogui.pixelMatchesColor(289, 479, (255, 255, 255), tolerance=0):
            break

re_search_report()
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
# Report: Guests INH Complimentary and Houseuse: Save
pdf_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Guests_INH_Complimentary_and_Houseuse = "Guests INH Complimentary and Houseuse"

pyautogui.write(Guests_INH_Complimentary_and_Houseuse, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
tab_reserve(13)

# Report: Guests in house Pseudo room Rate Check
pyautogui.write("giratecheck", interval=.01)
pyautogui.press("enter", interval=.01)
re_search_report()
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)

def config_report():
    while True:
        if pyautogui.pixelMatchesColor(214, 244, (255, 255, 255), tolerance=0):
            break

config_report()
time.sleep(1)
# Report: Guests in house Pseudo room Rate Check: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=7, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
time.sleep(.5)
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Notes
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("enter", interval=.01)
# Report: Guests in house Pseudo room Rate Check: Save
pdf_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Guests_in_house_Pseudo_room_Rate_Check = "Guests in house Pseudo room Rate Check"

pyautogui.write(Guests_in_house_Pseudo_room_Rate_Check, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
tab_reserve(3)
pyautogui.press("enter", interval=.01)
manage_reports()
time.sleep(1)
pyautogui.press("tab", interval=.01)