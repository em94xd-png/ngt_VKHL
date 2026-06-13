import time
from selenium import webdriver
import pyautogui

def print_it(file_from):
    driver = webdriver.Edge()
    driver.get(file_from)

    # Trigger print asynchronously so Python doesn't freeze
    driver.execute_script("setTimeout(function() { window.print(); }, 0);")

    time.sleep(1)

    pyautogui.press('tab', presses=9, interval=.01)
    # pyautogui.press("enter")
    time.sleep(3)

file_ = r"file:///D:/Users/fo.vkhl/Downloads/ExampleDomain.pdf"
print_it(file_)