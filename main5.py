import pygetwindow
import subprocess
import pyautogui
import time

# for _ in pygetwindow.getAllWindows():
#     print(_.title)

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

# Open Opera
subprocess.run(["cmd", "/c", "start", "msedge", site_OPERA])

pygetwindow.getWindowsWithTitle("Opera Cloud")[0].maximize()

# In Opera  
time.sleep(2.5)
pyautogui.hotkey("ctrl", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-",)
pyautogui.hotkey("ctrl", "=", "=", "=",)
time.sleep(5)