import pygetwindow
import pyautogui
import pyperclip
from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options


# all_wion = pygetwindow.getAllWindows()

# for _ in all_wion:
#     print(_.title)  # Print the title of each window

target_title = "Guest information panel"

# old_title = ""

while True:

    try:

        find_title = pygetwindow.getWindowsWithTitle(target_title)

        if find_title:
            found_title = find_title[0]

            if not found_title.isMinimized:
                # current_title = found_title.title

                # if current_title != old_title:
                found_title.activate()
                time.sleep(1)

                pyautogui.press('tab', presses=3)
                # time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                
                last = pyperclip.paste()

                # time.sleep(0.1)
                pyautogui.press('tab', presses=4)
                # time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                
                first = pyperclip.paste()

                # time.sleep(0.1)
                pyautogui.press('tab', presses=9)
                # time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                
                bd = pyperclip.paste()

                # time.sleep(0.1)
                pyautogui.press('tab', presses=5)
                # time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                
                ct = pyperclip.paste()

                # time.sleep(0.1)
                pyautogui.press('tab', presses=6)
                # time.sleep(0.1)
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.1)
                
                pn = pyperclip.paste()

                print(f"Last Name: {last}, First Name: {first}, Birth Date: {bd}, Country: {ct}, Pass Number: {pn}")

                time.sleep(5)

    except Exception as error:
        pass