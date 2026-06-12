from datetime import date, timedelta
import pyautogui


def yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

# print(f"IS {yesterday()}")
pyautogui.write(f"IS: {yesterday()}")