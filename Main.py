import pyautogui
import time
from datetime import date, timedelta
import os
from selenium import webdriver

# Clear report store
pyautogui.press("win", interval=.01)

Endday_before_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before"

pyautogui.write(Endday_before_folder)
time.sleep(1)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.press("del", interval=.01)
pyautogui.hotkey("ctrl", "w", interval=.01)

# Open Opera
pyautogui.press("win")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

pyautogui.write(site_OPERA)
time.sleep(0.5)
pyautogui.press("enter")

# In Opera  
time.sleep(1)
pyautogui.hotkey("win", "up")
pyautogui.hotkey("win", "down")
pyautogui.hotkey("win", "up")

time.sleep(0.1)

# Zoom out
def zoom_out(times):
    for _ in range(times):
        pyautogui.hotkey("ctrl", "-")

# Zoom in
def zoom_in(times):
    for _ in range(times):
        pyautogui.hotkey("ctrl", "=")

zoom_out(10)
zoom_in(3)
time.sleep(5)

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(4.5)
pyautogui.press("tab", interval=0.01)

# Report: Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Report: Room Discrepancy: Save
pyautogui.click(600,84, interval=.01)
pyautogui.press("tab", presses=17, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)

def find_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

find_reserve(2)
time.sleep(0.1)

pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Room_Discrepancy = "Room Discrepancy"

pyautogui.write(Room_Discrepancy)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)

# Report: Guests INH Complimentary and Houseuse
pyautogui.write("gi_c_h", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Report: Guests INH Complimentary and Houseuse: Save
pyautogui.click(600,84, interval=.01)
pyautogui.press("tab", presses=17, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Guests_INH_Complimentary_and_Houseuse = "Guests INH Complimentary and Houseuse"

pyautogui.write(Guests_INH_Complimentary_and_Houseuse)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)

# Report: Guests in house Pseudo room Rate Check
pyautogui.write("giratecheck", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# Report: Guests in house Pseudo room Rate Check: Config
pyautogui.click(125,303, interval=.01)
pyautogui.click(119,523, interval=.5)
pyautogui.press("tab", presses=7, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Notes
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(15)
# Report: Guests in house Pseudo room Rate Check: Save
pyautogui.click(600,84, interval=.01)
pyautogui.press("tab", presses=18, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Guests_in_house_Pseudo_room_Rate_Check = "Guests in house Pseudo room Rate Check"

pyautogui.write(Guests_in_house_Pseudo_room_Rate_Check)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=25, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(5)
pyautogui.press("tab", interval=.01)

# Report: Expected Arrival
pyautogui.write("Arrivals: Detailed FO", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Expected Arrival: Config
pyautogui.click(123, 302, interval=0.01)
pyautogui.click(123, 520, interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "c", interval=0.01)
pyautogui.press("tab", presses=2, interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "v", interval=0.01)
pyautogui.press("tab", presses=53, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Expected Arrival: Save
pyautogui.click(600, 84, interval=0.01)
pyautogui.press("tab", presses=17, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

def yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

Expected_Arrival = f"Expected Arrival {yesterday()}"

pyautogui.write(Expected_Arrival)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
pyautogui.press("tab", presses=25, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# Report: Out of Service by Reason
pyautogui.write("ooo", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Out of Service by Reason: Config
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.write(
    "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC,BANQ,PSEU", interval=0.01
)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
pyautogui.press("tab", interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Out of Service by Reason: Save
pyautogui.click(600, 84, interval=0.01)
pyautogui.press("tab", presses=18, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=0.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Service_by_Reason = f"17. Out of Service by Reason {yesterday()}"

pyautogui.write(Out_of_Service_by_Reason)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")

# Report: Out of Order by Reason
time.sleep(0.1)

def ooo_reverse(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

ooo_reverse(6)
time.sleep(0.5)

# Report: Out of Order by Reason: config
pyautogui.press("up", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=6, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Out of Order by Reason: Save
pyautogui.click(600, 84, interval=0.01)
pyautogui.press("tab", presses=17, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
pyautogui.press("tab", presses=6, interval=0.01)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Order_by_Reason = f"17. Out of Order by Reason {yesterday()}"

pyautogui.write(Out_of_Order_by_Reason)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
pyautogui.press("tab", presses=25, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# Report: Credit Limit
pyautogui.write("gi_authlimit", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Credit Limit: Config
pyautogui.press("tab", presses=4, interval=0.01)
pyautogui.press("space", interval=0.01) # Pseudo Rooms
pyautogui.press("tab", presses=12, interval=0.01)
pyautogui.press("space", interval=0.01) # Include Internal Notes
pyautogui.press("tab", interval=0.01)
pyautogui.write("Resv. - GEN", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=8, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(15)
# Report: Credit Limit: Save
pyautogui.click(600, 84, interval=0.01)
pyautogui.press("tab", presses=18, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Credit_Limit = f"15. Credit Limit {yesterday()}"

pyautogui.write(Credit_Limit)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
pyautogui.press("tab", presses=25, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# Report: Rebate and Correction Transactions
pyautogui.write("Journal by Cashier and Transaction Code", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.click(x=748, y=520, interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Rebate and Correction Transactions: Config
pyautogui.click(x=122, y=302, interval=0.01)
pyautogui.click(x=123, y=520, interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "c", interval=0.01)
pyautogui.press("tab", interval=0.01)
pyautogui.hotkey("ctrl", "v", interval=0.01)
pyautogui.press("tab", presses=4, interval=0.01)
time.sleep(1)
pyautogui.press("delete", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.press("space", interval=0.01) # Negative Postings Only
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Rebate and Correction Transactions: Save
pyautogui.click(600, 84, interval=0.01)
pyautogui.press("tab", presses=18, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
find_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Rebate_and_Correction_Transactions = "12. Rebate and Correction Transactions"

pyautogui.write(Rebate_and_Correction_Transactions)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)

# # Print
# def print_it(file_from):
#     driver = webdriver.Edge()
#     driver.get(file_from)

#     driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

#     time.sleep(1)

#     pyautogui.press('tab', presses=6, interval=.01)
#     pyautogui.press('up', presses=2, interval=.01)
#     pyautogui.press('tab', interval=.01)
#     pyautogui.press('enter', interval=.01)
#     pyautogui.press('tab', presses=3, interval=.01)
#     pyautogui.press('up', presses=2, interval=.01)
#     pyautogui.press('tab', presses=3, interval=.01)
#     pyautogui.press('enter', interval=.01)

# config_print_Room_Discrepancy = [
#     ("tab", 6, .01),
#     ("up", 2, .01),

# ]
# file_local = os.path.join(Endday_before_folder, Room_Discrepancy)
# file_url = "file:///" + os.path.abspath(file_local).replace("\\", "/").__add__(".PDF") # Convert your local absolute file path into a file:// URL structure

# print_it(file_url)