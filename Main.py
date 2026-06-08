import pyautogui
import time

# Open Opera
pyautogui.press("win")
pyautogui.write(
    "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"
)
time.sleep(.5)
pyautogui.press("enter")

# In Opera
time.sleep(1)
pyautogui.hotkey("win", "up")
# Zoom out
pyautogui.hotkey("ctrl", "-", interval=.01)
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
pyautogui.hotkey("ctrl", "-")
# Zoom in
pyautogui.hotkey("ctrl", "=")
pyautogui.hotkey("ctrl", "=")
pyautogui.hotkey("ctrl", "=")
time.sleep(3)

# Report: Room Discrepancy
pyautogui.press("tab", interval=.01)
pyautogui.write("hkroomdiscrepancy", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=9, interval=.01)
pyautogui.press("down", presses=2, interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=14, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(10)
# Report: Room Discrepancy: Save
pyautogui.press("tab", presses=20, interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=6, interval=.01)
pyautogui.press("enter", interval=.01)
pyautogui.write(r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before")
pyautogui.press("enter", interval=.01)
time.sleep(1)
pyautogui.press("tab", presses=4, interval=.01)
pyautogui.press("down", presses=7, interval=.01)
pyautogui.press("enter", interval=.01)
pyautogui.press("left", interval=.01)
pyautogui.press("enter", interval=.01)
time.sleep(.5)
pyautogui.hotkey("ctrl", "w")
time.sleep(.5)
pyautogui.press("tab", presses=29, interval=.01)