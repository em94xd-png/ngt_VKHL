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

# Report: Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Report: Room Discrepancy: Save
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

tab_reserve(2)
time.sleep(0.1)

pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
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
pyautogui.press("tab", presses=29, interval=.01)

# Report: Guests INH Complimentary and Houseuse
pyautogui.write("gi_c_h", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(8.5)
# Report: Guests INH Complimentary and Houseuse: Save
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
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
pyautogui.press("tab", presses=29, interval=.01)

# Report: Guests in house Pseudo room Rate Check
pyautogui.write("giratecheck", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(3.5)
# Report: Guests in house Pseudo room Rate Check: Config
pyautogui.hotkey("ctrl", "a", interval=.01)

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=7, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Notes
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(15)
# Report: Guests in house Pseudo room Rate Check: Save
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(Endday_before_folder)
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
time.sleep(5)
pyautogui.press("tab", interval=.01)

# Report: Expected Arrival
pyautogui.write("Arrivals: Detailed FO", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(3.5)
# Report: Expected Arrival: Config
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=2, interval=0.01)
time.sleep(1)
pyautogui.write(format2_yesterday(), interval=.01)
pyautogui.press("tab", presses=53, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Expected Arrival: Save
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

def format1_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

Expected_Arrival = f"Expected Arrival {format1_yesterday()}"

pyautogui.write(Expected_Arrival, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
tab_reserve(3)
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
pyautogui.press("right", interval=.01)
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
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=0.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
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
# Report: Out of Order by Reason: config
pyautogui.press("up", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=6, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Out of Order by Reason: Save
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=0.01)
tab_reserve(2)
time.sleep(.01)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
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
time.sleep(5)
pyautogui.press("tab", interval=0.01)

# Report: Credit Limit
pyautogui.write("gi_authlimit", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(2.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1.5)
pyautogui.press("right", interval=.01)
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
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
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
time.sleep(5)
pyautogui.press("tab", interval=0.01)

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
pyautogui.press("enter", interval=0.01)
time.sleep(8.5)
# Report: Rebate and Correction Transactions: Save
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(Endday_before_folder)
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
file_local_Room_Discrepancy = os.path.join(Endday_before_folder, Room_Discrepancy)

file_url_Room_Discrepancy = "file:///" + os.path.abspath(file_local_Room_Discrepancy).replace("\\", "/").__add__(".PDF")

def print_Room_Discrepancy(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Room_Discrepancy = [
        ("tab", 6),
        ("up", 2),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Room_Discrepancy:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Guests_INH_Complimentary_and_Houseuse = os.path.join(Endday_before_folder, Guests_INH_Complimentary_and_Houseuse)

file_url_Guests_INH_Complimentary_and_Houseuse = "file:///" + os.path.abspath(file_local_Guests_INH_Complimentary_and_Houseuse).replace("\\", "/").__add__(".PDF")

def print_Guests_INH_Complimentary_and_Houseuse(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Guests_INH_Complimentary_and_Houseuse = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Guests_INH_Complimentary_and_Houseuse:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Guests_in_house_Pseudo_room_Rate_Check = os.path.join(Endday_before_folder, Guests_in_house_Pseudo_room_Rate_Check)

file_url_Guests_in_house_Pseudo_room_Rate_Check = "file:///" + os.path.abspath(file_local_Guests_in_house_Pseudo_room_Rate_Check).replace("\\", "/").__add__(".PDF")

def print_Guests_in_house_Pseudo_room_Rate_Check(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Guests_in_house_Pseudo_room_Rate_Check = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Guests_in_house_Pseudo_room_Rate_Check:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Expected_Arrival = os.path.join(Endday_before_folder, Expected_Arrival)

file_url_Expected_Arrival = "file:///" + os.path.abspath(file_local_Expected_Arrival).replace("\\", "/").__add__(".PDF")

def print_Expected_Arrival(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Expected_Arrival = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Expected_Arrival:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Out_of_Service_by_Reason = os.path.join(Endday_before_folder, Out_of_Service_by_Reason)

file_url_Out_of_Service_by_Reason = "file:///" + os.path.abspath(file_local_Out_of_Service_by_Reason).replace("\\", "/").__add__(".PDF")

def print_Out_of_Service_by_Reason(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Out_of_Service_by_Reason = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Out_of_Service_by_Reason:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Out_of_Order_by_Reason = os.path.join(Endday_before_folder, Out_of_Order_by_Reason)

file_url_Out_of_Order_by_Reason = "file:///" + os.path.abspath(file_local_Out_of_Order_by_Reason).replace("\\", "/").__add__(".PDF")

def print_Out_of_Order_by_Reason(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Out_of_Order_by_Reason = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Out_of_Order_by_Reason:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Credit_Limit = os.path.join(Endday_before_folder, Credit_Limit)

file_url_Credit_Limit = "file:///" + os.path.abspath(file_local_Credit_Limit).replace("\\", "/").__add__(".PDF")

def print_Credit_Limit(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Credit_Limit = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Credit_Limit:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

file_local_Rebate_and_Correction_Transactions = os.path.join(Endday_before_folder, Rebate_and_Correction_Transactions)

file_url_Rebate_and_Correction_Transactions = "file:///" + os.path.abspath(file_local_Rebate_and_Correction_Transactions).replace("\\", "/").__add__(".PDF")

def print_Rebate_and_Correction_Transactions(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    driver.execute_script("setTimeout(function() { window.print(); }, 0);") # Trigger print asynchronously so Python doesn't freeze

    time.sleep(1)

    config_print_Rebate_and_Correction_Transactions = [
        ("tab", 6),
        ("up", 2),
        ("down", 1),
        ("tab", 1),
        ("enter", 1),
        ("tab", 3),
        ("up", 2),
        ("down", 1),
        ("tab", 3),
        ("enter", 1)
    ]

    for key, presses in config_print_Rebate_and_Correction_Transactions:
        pyautogui.press(key, presses=presses)

    time.sleep(.1)

print_Room_Discrepancy(file_url_Room_Discrepancy)
print_Guests_INH_Complimentary_and_Houseuse(file_url_Guests_INH_Complimentary_and_Houseuse)
print_Guests_in_house_Pseudo_room_Rate_Check(file_url_Guests_in_house_Pseudo_room_Rate_Check)
# print_Expected_Arrival(file_url_Expected_Arrival)
print_Out_of_Service_by_Reason(file_url_Out_of_Service_by_Reason)
print_Out_of_Order_by_Reason(file_url_Out_of_Order_by_Reason)
print_Credit_Limit(file_url_Credit_Limit)
print_Rebate_and_Correction_Transactions(file_url_Rebate_and_Correction_Transactions)

# Open Room Discrepancy
pyautogui.press("win", interval=.01)
pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before\Room Discrepancy.PDF")
time.sleep(1)
pyautogui.press("enter", interval=.01)