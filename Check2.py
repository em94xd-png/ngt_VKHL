import pygetwindow
import pyautogui
import pyperclip
import time
import openpyxl


# all_wion = pygetwindow.getAllWindows()

# for _ in all_wion:
#     print(_.title)  # Print the title of each window

target_title = "Guest information panel"

def running_set(times):

    # pyautogui.PAUSE = 0.01

    for _ in range(times):
        pyautogui.press("tab")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)

    return pyperclip.paste().strip()

while True:

    try:

        find_title = pygetwindow.getWindowsWithTitle(target_title)

        if not find_title and find_title[0] and find_title[0].title.isMinimized:

            find_title[0].activate()
            time.sleep(1)

            LN = running_set(3)

            FN = running_set(4)

            BD = running_set(9)

            CT = running_set(5)

            PN = running_set(6)

            # tm = openpyxl.load_workbook("tm.xlsx")
            # sheet = tm.active
            # sheet.append([LN, FN, BD, CT, PN])
            # tm.save("tm.xlsx")
            
            time.sleep(5)

    except Exception as error:
        pass