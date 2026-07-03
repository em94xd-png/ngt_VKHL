import pygetwindow
import pyautogui
import pyperclip
from selenium import webdriver
import time
from selenium.webdriver.edge.options import Options


# all_wion = pygetwindow.getAllWindows()

# for _ in all_wion:
#     print(_.title)  # Print the title of each window

target_title = "Edge"

old_title = ""

while True:

    try:

        find_title = pygetwindow.getWindowsWithTitle(target_title)

        if find_title:
            found_title = find_title[0]

            if not found_title.isMinimized:
                current_title = found_title.title

                if current_title != old_title:
                    found_title.activate()

                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(0.1)  # Small delay to ensure the select all command is processed
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(0.1)  # Small delay to ensure the copy command is processed
                    
                    current_data = pyperclip.paste()

                    old_title = current_title

                    print(f"Current Title: {current_title}")
                
                    print(f"Current Data: {current_data}")

    except Exception as e:
        pass
