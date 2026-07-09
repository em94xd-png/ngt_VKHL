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

    pyautogui.PAUSE = 0.001

    for _ in range(times):
        pyautogui.press("tab")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)

    return pyperclip.paste().strip()

while True:

    try:

        find_title = pygetwindow.getWindowsWithTitle(target_title)[0]

        if not find_title.isMinimized:

            find_title.activate()
            time.sleep(1)

            last_name = running_set(3)

            first_name = running_set(4)

            birth_day = running_set(9)

            country = running_set(5)

            passport_number = running_set(6)

            wb = openpyxl.load_workbook("Oo.xlsx")
            sheet = wb.active
            sheet.append([last_name, first_name, birth_day, country, passport_number])
            wb.save("Oo.xlsx")
            
            # print(f"Last Name: {last_name}, First Name: {first_name}, Birth Date: {birth_day}, Country: {country}, Pass Number: {passport_number}")

            time.sleep(15)

    except Exception as error:
        pass