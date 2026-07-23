import pyautogui, time, os, subprocess, pygetwindow, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import script_config

pyautogui.FAILSAFE = True

if not os.path.exists(f"{script_config.path_share}"):
     sys.exit()

# Create folder
os.makedirs(script_config.daily_report_path.__add__(r"\Before Closeday"), exist_ok=True)

# Delete files
daily_report_before = script_config.daily_report_path + r"\Before Closeday"
script_config.remove_file(daily_report_before)

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", script_config.site_OPERA])
pygetwindow.getWindowsWithTitle("Opera Cloud")[0].maximize()

# In Opera
script_config.first_OPERA_open()
script_config.zoom_out(10)
script_config.zoom_in(3)
script_config.main_OPERA_menu()

# To report search
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("right", presses=6, interval=0.01)
pyautogui.press("down", interval=0.01)
pyautogui.press("enter", interval=0.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Room Discrepancy
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
# Room Discrepancy: Save
script_config.wait_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "f", interval=.01)
pyautogui.press("tab", presses=5, interval=.01)

Room_Discrepancy = "Room Discrepancy"

pyautogui.write(Room_Discrepancy, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
script_config.tab_reserve(13)

# Guests INH Complimentary and Houseuse
pyautogui.write("gi_c_h", interval=.01)
pyautogui.press("enter", interval=.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
# Guests INH Complimentary and Houseuse: Save
script_config.wait_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
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
script_config.tab_reserve(13)

# Guests in house Pseudo room Rate Check
pyautogui.write("giratecheck", interval=.01)
pyautogui.press("enter", interval=.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=.01)
pyautogui.press("enter", interval=.01)
# Guests in house Pseudo room Rate Check: Config
script_config.config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(script_config.ytd_dd_mm, interval=.01)
pyautogui.press("tab", presses=7, interval=.01)
pyautogui.press("space", interval=.01) # Pseudo Rooms
time.sleep(.5)
pyautogui.press("tab", presses=10, interval=.01)
pyautogui.press("space", interval=.01) # Notes
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("enter", interval=.01)
# Guests in house Pseudo room Rate Check: Save
script_config.wait_report()
pyautogui.click(600,84, interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
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
script_config.tab_reserve(3)
pyautogui.press("enter", interval=.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=.01)

# Expected Arrival
pyautogui.write("Arrivals: Detailed FO", interval=0.01)
pyautogui.press("enter", interval=0.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Expected Arrival: Config
script_config.config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(script_config.ytd_dd_mm, interval=.01)
pyautogui.press("tab", presses=2, interval=0.01)
time.sleep(1)
pyautogui.write(script_config.ytd_dd_mm, interval=.01)
pyautogui.press("tab", presses=53, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Expected Arrival: Save
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Expected_Arrival = f"Expected Arrival {script_config.ytd_dot_dd_mm}"

pyautogui.write(Expected_Arrival, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
script_config.tab_reserve(3)
pyautogui.press("enter", interval=0.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Out of Service by Reason
pyautogui.write("ooo", interval=0.01)
pyautogui.press("enter", interval=0.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Out of Service by Reason: Config
script_config.config_report()
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
# Out of Service by Reason: Save
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=0.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Service_by_Reason = f"17. Out of Service by Reason {script_config.ytd_dot_dd_mm}"

pyautogui.write(Out_of_Service_by_Reason, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")

# Out of Order by Reason
time.sleep(0.1)
script_config.tab_reserve(6)
time.sleep(0.5)
# Out of Order by Reason: Config
pyautogui.press("up", interval=0.01)
time.sleep(0.5)
pyautogui.press("tab", presses=6, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Out of Order by Reason: Save
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=0.01)
script_config.tab_reserve(2)
time.sleep(.01)
pyautogui.press("enter", interval=0.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Out_of_Order_by_Reason = f"17. Out of Order by Reason {script_config.ytd_dot_dd_mm}"

pyautogui.write(Out_of_Order_by_Reason, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
script_config.tab_reserve(3)
pyautogui.press("enter", interval=0.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Credit Limit
pyautogui.write("gi_authlimit", interval=0.01)
pyautogui.press("enter", interval=0.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Credit Limit: Config
script_config.config_report()
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
# Credit Limit: Save
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=6, interval=.01)

Credit_Limit = f"15. Credit Limit {script_config.ytd_dot_dd_mm}"

pyautogui.write(Credit_Limit, interval=.01)
pyautogui.press("tab", presses=3, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
script_config.tab_reserve(3)
pyautogui.press("enter", interval=0.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# Rebate and Correction Transactions
pyautogui.write("Journal by Cashier and Transaction Code", interval=0.01)
pyautogui.press("enter", interval=0.01)
script_config.search_enter_step1()
script_config.search_enter_step2()
time.sleep(.5)
pyautogui.press("tab", presses=9, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)
time.sleep(1)
pyautogui.press("right", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Rebate and Correction Transactions: Config
script_config.config_report()
time.sleep(1)
pyautogui.hotkey("ctrl", "a", interval=.01)
pyautogui.write(script_config.ytd_dd_mm, interval=.01)
pyautogui.press("tab", interval=0.01)
time.sleep(1)
pyautogui.write(script_config.ytd_dd_mm, interval=.01)
pyautogui.press("tab", presses=5, interval=0.01)
pyautogui.press("space", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Rebate and Correction Transactions: Save
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "s", interval=.01)
time.sleep(1)
pyautogui.hotkey("ctrl", "f", interval=.01)
script_config.tab_reserve(2)
time.sleep(0.1)
pyautogui.press("enter", interval=0.01)
pyautogui.write(script_config.daily_report_path.__add__(r"\Before Closeday"))
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
script_config.print_report_before(Room_Discrepancy)
time.sleep(.5)
script_config.print_page_config(1, 1, 0)

script_config.print_report_before(Guests_INH_Complimentary_and_Houseuse)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

script_config.print_report_before(Guests_in_house_Pseudo_room_Rate_Check)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

script_config.print_report_before(Out_of_Service_by_Reason)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

script_config.print_report_before(Out_of_Order_by_Reason)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

script_config.print_report_before(Credit_Limit)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

script_config.print_report_before(Rebate_and_Correction_Transactions)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

# Open Room Discrepancy
script_config.print_report_before(Room_Discrepancy)