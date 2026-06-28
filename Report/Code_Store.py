import pyautogui
from datetime import date, timedelta
import calendar
import os
import subprocess
import time

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_before")

Endday_after_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_after")

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

def format1_today():
    today = date.today()
    return today.strftime("%d%m")

def format1_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d.%m")

def format2_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%d%m")

def date_first():
    today = date.today()
    today_1 = today.replace(day=1)
    return today_1.strftime("%d%m")

def date_end():
    today = date.today()

    _, last_day = calendar.monthrange(today.year, today.month)
    month_end = today.replace(day=last_day)
    return month_end.strftime("%d%m")

def report_path():
    yesterday = date.today() - timedelta(days=1)
    ytd_date = yesterday.strftime("%#d")
    ytd_month_number = yesterday.strftime("%#m")
    ytd_month_short = yesterday.strftime("%b")
    ytd_month_full = yesterday.strftime("%B")
    ytd_year_full = yesterday.strftime("%Y")

    return fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}"

def tab_reserve(times):
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def report_print(report_name):

    Endday_before_folder = os.environ.get("USERPROFILE").__add__(r"..")

    folder_report = os.path.join(Endday_before_folder, report_name).__add__(".PDF")

    print_url_add = "file:///" + folder_report.replace("\\", "/")

    subprocess.run(["cmd", "/c", "start", "msedge", print_url_add])

def page_print(set_copy, set_both, set_page):
    pyautogui.hotkey("ctrl", "p", interval=.01)
    time.sleep(1)
    pyautogui.press("tab", presses=(set_copy), interval=.01)

    if set_copy == 1:
        pyautogui.press("tab", presses=5, interval=.01)
    elif set_copy == 2:
        pyautogui.press("tab", interval=.01)
        pyautogui.write("2", interval=.01)
        pyautogui.press("tab", presses=4, interval=.01)

    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(set_both), interval=.01)
    pyautogui.press("tab", interval=.01)
    pyautogui.press("enter", interval=.01)
    time.sleep(.01)
    pyautogui.press("tab", presses=3, interval=.01)
    pyautogui.press("up", presses=2, interval=.01)
    pyautogui.press("down", presses=(set_page), interval=.01)
    pyautogui.press("tab", presses=3, interval=.01)
    time.sleep(.5)
    # pyautogui.press("enter", interval=.01)
    # pyautogui.hotkey("ctrl", "w", interval=.01)

def file_remove(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)