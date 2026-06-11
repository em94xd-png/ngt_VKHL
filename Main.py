import pyautogui
import time

# Open Opera
pyautogui.press("win")
pyautogui.write(
    "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"
)
time.sleep(0.5)
pyautogui.press("enter")

# In Opera
time.sleep(1)
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

# # Report: Room Discrepancy
# pyautogui.write("hkroomdiscrepancy", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(2.5)
# pyautogui.press("tab", presses=9, interval=.01)
# pyautogui.press("down", presses=2, interval=.01)
# time.sleep(1.5)
# pyautogui.click(x=748, y=520, interval=.01)
# pyautogui.press("tab", presses=4, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(8.5)
# # Report: Room Discrepancy: Save
# pyautogui.click(600,84, interval=.01)
# pyautogui.press("tab", presses=17, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "f", interval=.01)

def find_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

# find_reserve(2)
# time.sleep(0.1)

# pyautogui.press("enter", interval=.01)
# pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=4, interval=.01)
# pyautogui.press("down", presses=7, interval=.01) # Report position
# pyautogui.press("enter", interval=.01)
# pyautogui.press("left", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.hotkey("ctrl", "w")
# time.sleep(.5)
# pyautogui.press("tab", presses=29, interval=.01)

# # Report: Guests INH Complimentary and Houseuse
# pyautogui.write("gi_c_h", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(2.5)
# pyautogui.press("tab", presses=9, interval=.01)
# pyautogui.press("down", presses=2, interval=.01)
# time.sleep(1.5)
# pyautogui.click(x=748, y=520, interval=.01)
# pyautogui.press("tab", presses=4, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(8.5)
# # Report: Guests INH Complimentary and Houseuse: Save
# pyautogui.click(600,84, interval=.01)
# pyautogui.press("tab", presses=17, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "f", interval=.01)
# find_reserve(2)
# time.sleep(0.1)
# pyautogui.press("enter", interval=.01)
# pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=4, interval=.01)
# pyautogui.press("down", presses=6, interval=.01) # Report position
# pyautogui.press("enter", interval=.01)
# pyautogui.press("left", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.hotkey("ctrl", "w")
# time.sleep(.5)
# pyautogui.press("tab", presses=29, interval=.01)

# # Report: Guests in house Pseudo room Rate Check
# pyautogui.write("giratecheck", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(2.5)
# pyautogui.press("tab", presses=9, interval=.01)
# pyautogui.press("down", presses=2, interval=.01)
# time.sleep(1.5)
# pyautogui.click(x=748, y=520, interval=.01)
# pyautogui.press("tab", presses=3, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(3.5)
# # Report: Guests in house Pseudo room Rate Check: Config
# pyautogui.click(125,303, interval=.01)
# pyautogui.click(119,523, interval=.5)
# pyautogui.press("tab", presses=7, interval=.01)
# pyautogui.press("space", interval=.01) # Pseudo Rooms
# pyautogui.press("tab", presses=10, interval=.01)
# pyautogui.press("space", interval=.01) # Notes
# time.sleep(.5)
# pyautogui.press("tab", presses=9, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(15)
# # Report: Guests in house Pseudo room Rate Check: Save
# pyautogui.click(600,84, interval=.01)
# pyautogui.press("tab", presses=18, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "f", interval=.01)
# find_reserve(2)
# time.sleep(0.1)
# pyautogui.press("enter", interval=.01)
# pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=5, interval=.01)
# pyautogui.press("down", presses=5, interval=.01) # Report position
# pyautogui.press("enter", interval=.01)
# pyautogui.press("left", interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(.5)
# pyautogui.hotkey("ctrl", "w")
# time.sleep(.5)
# pyautogui.press("tab", presses=25, interval=.01)
# pyautogui.press("enter", interval=.01)
# time.sleep(5)
# pyautogui.press("tab", interval=.01)

# # Report: Expected Arrival
# pyautogui.write("Arrivals: Detailed FO", interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(2.5)
# pyautogui.press("tab", presses=9, interval=0.01)
# pyautogui.press("down", presses=2, interval=0.01)
# time.sleep(1.5)
# pyautogui.click(x=748, y=520, interval=.01)
# pyautogui.press("tab", presses=3, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(3.5)
# # Report: Expected Arrival: Config
# pyautogui.click(123, 302, interval=0.01)
# pyautogui.click(123, 520, interval=0.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "c", interval=0.01)
# pyautogui.press("tab", presses=2, interval=0.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "v", interval=0.01)
# pyautogui.press("tab", presses=53, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(8.5)
# # Report: Expected Arrival: Save
# pyautogui.click(600, 84, interval=0.01)
# pyautogui.press("tab", presses=18, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(1)
# pyautogui.hotkey("ctrl", "f", interval=.01)
# find_reserve(2)
# time.sleep(0.1)
# pyautogui.press("enter", interval=0.01)
# pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
# pyautogui.press("enter", interval=0.01)
# time.sleep(.5)
# pyautogui.press("tab", presses=4, interval=0.01)
# pyautogui.press("down", presses=4, interval=0.01)  # Report position
# pyautogui.press("enter", interval=0.01)
# pyautogui.press("left", interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(0.5)
# pyautogui.hotkey("ctrl", "w")
# time.sleep(0.5)
# pyautogui.press("tab", presses=25, interval=0.01)
# pyautogui.press("enter", interval=0.01)
# time.sleep(5)
# pyautogui.press("tab", interval=0.01)

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
pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=4, interval=0.01)
pyautogui.press("down", presses=3, interval=0.01)  # Report position
pyautogui.press("enter", interval=0.01)
pyautogui.press("left", interval=0.01)
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
pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
pyautogui.press("enter", interval=0.01)
time.sleep(.5)
pyautogui.press("tab", presses=4, interval=0.01)
pyautogui.press("down", presses=2, interval=0.01)  # Report position
pyautogui.press("enter", interval=0.01)
pyautogui.press("left", interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(0.5)
pyautogui.press("tab", presses=25, interval=0.01)
pyautogui.press("enter", interval=0.01)
time.sleep(5)
pyautogui.press("tab", interval=0.01)
