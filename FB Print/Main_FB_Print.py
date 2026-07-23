import subprocess, pyautogui, time, os, pygetwindow, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import script_config

pyautogui.FAILSAFE = True

if not os.path.exists(f"{script_config.path_share}"):
     sys.exit()

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", f"{script_config.site_OPERA}"])
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

# Package Forecast
pyautogui.write("Package Forecast - Detailed", interval=.01)
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
# Package Forecast: Config
script_config.config_report()
time.sleep(1)
pyautogui.press("tab", presses=2, interval=0.01)
pyautogui.write(script_config.td_dd_mm, interval=.01)
pyautogui.press("tab", interval=0.01)
time.sleep(1)
pyautogui.write(script_config.td_dd_mm, interval=.01)
pyautogui.press("tab", presses=3, interval=0.01)
time.sleep(.75)
pyautogui.write("BFB01E,BFB01I,BFB02E,BFB02I,BFB03I,BFB04I", interval=.01)
pyautogui.press("tab", presses=13, interval=0.01)
pyautogui.press("enter", interval=0.01)
# Package Forecast: Print
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)
script_config.tab_reserve(3)
pyautogui.press("enter", interval=0.01)
script_config.search_reports()
time.sleep(1)
pyautogui.press("tab", interval=0.01)

# VKHL Guests INH (Full)
pyautogui.write("gibyroom", interval=.01)
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
# VKHL Guests INH (Full): Config
script_config.config_report()
time.sleep(1)
pyautogui.press("tab", interval=.01)
time.sleep(.75)
pyautogui.write(script_config.Room_Type, interval=.01)
pyautogui.press("tab", presses=15, interval=.01)
pyautogui.press("delete", interval=.01)
time.sleep(.5)
pyautogui.press("tab", presses=8, interval=.01)
pyautogui.press("enter", interval=0.01)
# VKHL Guests INH (Full): Print
script_config.wait_report()
pyautogui.click(600, 84, interval=0.01)
time.sleep(.5)
script_config.print_page_config(2, 1, 1)

VKHL_Arrivals = "4. VKHL Arrivals"

script_config.print_report_after(VKHL_Arrivals)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

VKHL_Departures = "5. VKHL Departures"

script_config.print_report_after(VKHL_Departures)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)

VKHL_Guests_INH = "6. VKHL Guests INH"

script_config.print_report_after(VKHL_Guests_INH)
time.sleep(.5)
script_config.print_page_config(1, 1, 1)