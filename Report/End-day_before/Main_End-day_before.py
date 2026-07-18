import pyautogui
import time
from datetime import date, timedelta
import os
import subprocess
import pygetwindow

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

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

def format1_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

def file_remove(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)

pyautogui.FAILSAFE = True

# Create folder
os.makedirs(report_path().__add__(r"\Before Closeday"), exist_ok=True)

# Delete files
path_report = report_path() + r"\Before Closeday"

file_remove(path_report)

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

# Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)

def after_search():
    while True:
        if pyautogui.pixelMatchesColor(267, 452, (244, 243, 239), tolerance=0):
            break

after_search()
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
# Room Discrepancy: Save

def wait_report():
    while True:
        if pyautogui.pixelMatchesColor(1866, 975, (213, 163, 160), tolerance=10):
            break

wait_report()
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

Room_Discrepancy = "Room Discrepancy"

pyautogui.write(Room_Discrepancy, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
tab_reserve(13)

# Guests INH Complimentary and Houseuse
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
# Guests INH Complimentary and Houseuse: Save
wait_report()
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

# Guests in house Pseudo room Rate Check
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
# Guests in house Pseudo room Rate Check: Config

def config_report():
    while True:
        if pyautogui.pixelMatchesColor(214, 244, (255, 255, 255), tolerance=0):
            break

config_report()
time.sleep(1)
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
# Guests in house Pseudo room Rate Check: Save
wait_report()
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
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=.01)

# Expected Arrival
pyautogui.write("Arrivals: Detailed FO", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Expected Arrival: Config
config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=2, interval=0.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=53, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Expected Arrival: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Expected_Arrival = f"Expected Arrival {format1_yesterday()}"

pyautogui.write(Expected_Arrival, interval=.01)
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

# Report: Out of Service by Reason
pyautogui.write("ooo", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Out of Service by Reason: Config
config_report()
time.sleep(1)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.write(
    "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC,BANQ,PSEU", interval=0.01
)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(.5)
pyautogui.press("tab", interval=0.01)
pyautogui.press("down", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Out of Service by Reason: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=0.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Service_by_Reason = f"17. Out of Service by Reason {format1_yesterday()}"

pyautogui.write(Out_of_Service_by_Reason, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")

# Report: Out of Order by Reason
time.sleep(0.1)
tab_reserve(6)
time.sleep(0.5)
# Report: Out of Order by Reason: Config
pyautogui.press("up", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=6, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Out of Order by Reason: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=0.01)
tab_reserve(2)
time.sleep(.01)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Order_by_Reason = f"17. Out of Order by Reason {format1_yesterday()}"

pyautogui.write(Out_of_Order_by_Reason, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Report: Credit Limit
pyautogui.write("gi_authlimit", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Credit Limit: Config
config_report()
time.sleep(1)
pyautogui.press("tab", presses=4, interval=0.01)
pyautogui.press("space", interval=0.01) # Pseudo Rooms
time.sleep(.5)
pyautogui.press("tab", presses=12, interval=0.01)
pyautogui.press("space", interval=0.01) # Include Internal Notes
time.sleep(.5)
pyautogui.press("tab", interval=0.01)
pyautogui.write("Resv. - GEN", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=8, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Credit Limit: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Credit_Limit = f"15. Credit Limit {format1_yesterday()}"

pyautogui.write(Credit_Limit, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
pyautogui.press("enter", interval=0.01)
search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Report: Rebate and Correction Transactions
pyautogui.write("Journal by Cashier and Transaction Code", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Rebate and Correction Transactions: Config
config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", interval=0.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("space", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Report: Rebate and Correction Transactions: Save
wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(report_path().__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Rebate_and_Correction_Transactions = "12. Rebate and Correction Transactions"

pyautogui.write(Rebate_and_Correction_Transactions, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(1)

# Print
def report_print(report_name):                                  

    Endday_before_folder = report_path().__add__(r"\Before Closeday")

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

report_print(Room_Discrepancy)
time.sleep(.5)
page_print(1, 1, 0)

report_print(Guests_INH_Complimentary_and_Houseuse)
time.sleep(.5)
page_print(1, 1, 1)

report_print(Guests_in_house_Pseudo_room_Rate_Check)
time.sleep(.5)
page_print(1, 1, 1)

# report_print(Expected_Arrival)
# time.sleep(.5)
# page_print(1, 1, 1)

report_print(Out_of_Service_by_Reason)
time.sleep(.5)
page_print(1, 1, 1)

report_print(Out_of_Order_by_Reason)
time.sleep(.5)
page_print(1, 1, 1)

report_print(Credit_Limit)
time.sleep(.5)
page_print(1, 1, 1)

report_print(Rebate_and_Correction_Transactions)
time.sleep(.5)
page_print(1, 1, 1)

# Open Room Discrepancy
report_print(Room_Discrepancy)