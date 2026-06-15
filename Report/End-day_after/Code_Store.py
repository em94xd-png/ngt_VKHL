import pyautogui

Endday_before_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before"

Endday_after_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_after"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")