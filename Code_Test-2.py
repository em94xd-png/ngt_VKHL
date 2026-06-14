import pyautogui

config_print_Room_Discrepancy = [
    ("tab", 6, .01),
    ("up", 2, .01),
    ("tab", 1, .01),
    ("enter", 1, .01),
    ("tab", 3, .01),
    ("up", 2, .01),
    ("tab", 3, .01),
    ("enter", 1, .01)
]

for key, presses, interval in config_print_Room_Discrepancy:
    pyautogui.press(key, presses=presses, interval=interval)

