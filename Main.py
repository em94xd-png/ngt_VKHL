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