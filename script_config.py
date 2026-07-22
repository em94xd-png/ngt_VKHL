import pyautogui, os, subprocess, time, calendar
from datetime import date, timedelta, datetime
from urllib.parse import urlparse, parse_qs

device_path = "LMPC202507256L"
snf_path = fr"\\{device_path}\Keeper\OTH"
download_path = os.environ.get("USERPROFILE").__add__(r"\Downloads")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

Room_Class = "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC"

td = date.today()
td_dd_mm = td.strftime("%d%m")
td_dot_dd_mm_yy = td.strftime("%d.%m.%y")

ytd = date.today() - timedelta(days=1)
ytd_y_to_be = ytd.year + 543
ytd_short_date = ytd.strftime("%#d")
ytd_order_m = ytd.strftime("%#m")
ytd_short_m = ytd.strftime("%b")
ytd_full_m = ytd.strftime("%B")
ytd_yyyy = ytd.strftime("%Y")
ytd_dd_mm = ytd.strftime("%d%m")
ytd_dot_dd_mm = ytd.strftime("%d.%m")
ytd_dot_dd_mm_yy = ytd.strftime("%d.%m.%y")
ytd_dot_dd_mm_yyyy = ytd.strftime("%d.%m.%Y")
ytd_to_mm_dd_yyyy = ytd.strftime("%m/%d/%Y")
ytd_dd_mm_yyyy_be = ytd.strftime(f"%d%m{ytd_y_to_be}")

def date_begin():
    td = date.today()
    to_1 = td.replace(day=1)
    return to_1.strftime("%d%m")

def date_end():
    td = date.today()
    _, last_day = calendar.monthrange(td.year, td.month)
    date_end = td.replace(day=last_day)
    return date_end.strftime("%d%m")

daily_report_path = fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_yyyy}\{ytd_order_m} - {ytd_short_m} {ytd_yyyy}\{ytd_short_date} {ytd_full_m}"

def first_OPERA_open():
    while True:
        if pyautogui.pixelMatchesColor(7, 391, (244, 243, 239), tolerance=0):
            break

def zoom_out(_):
    pyautogui.PAUSE = .01
    for _ in range(_):
        pyautogui.hotkey("ctrl", "-")

def zoom_in(_):
    pyautogui.PAUSE = .01
    for _ in range(_):
        pyautogui.hotkey("ctrl", "=")

def main_OPERA_menu():
    while True:
        if pyautogui.pixelMatchesColor(139, 129, ( 70,  70,  68), tolerance=0):
            break

def search_reports():
    while True:
        if pyautogui.pixelMatchesColor(252, 245, (88, 88, 86), tolerance=0):
            break

def search_enter_step1():
    while True:
        if pyautogui.pixelMatchesColor(1854, 337, (204, 204, 204), tolerance=10):
            break

def search_enter_step2():
    while True:
        if pyautogui.pixelMatchesColor(1854, 337, (6, 108, 122), tolerance=10):
            break

def config_report():
    while True:
        if pyautogui.pixelMatchesColor(214, 244, (255, 255, 255), tolerance=0):
            break

def wait_report():
    while True:
        if pyautogui.pixelMatchesColor(1866, 975, (213, 163, 160), tolerance=10):
            break

def tab_reserve(times):
    pyautogui.PAUSE = 0.01
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def save_immigration():
     while True:
          if pyautogui.pixelMatchesColor(982, 514, (88, 88, 86), tolerance=10):
               break
          
def download_page():
     while True:
          if pyautogui.pixelMatchesColor(1508, 53, (39, 35, 32), tolerance=10):
               break
          
def download_id(id):
     parse_url = urlparse(id)
     query_url = parse_qs(parse_url.query)
     if "rep" in query_url:
          rep_id = query_url["rep"][0]
          split_id = rep_id.split("_")[1]
          return split_id
     
def sw_date_format(ad, be, ad2):
     if ad and ad.strip() != "":
          try:
               ad = datetime.strptime(ad.strip(), "%m/%d/%Y")
               return ad.strftime("%d/%m/%Y")
          except ValueError:
               return ad
     if be and be.strip() != "":
          try:
               be = datetime.strptime(be.strip(), "%m/%d/%Y")
               cvt_be = be.year + 543
               return be.strftime(f"%d/%m/{cvt_be}")
          except ValueError:
               return be
     if ad2 and str(ad2).strip() != "":
          try:
               ad2 = datetime.strptime(ad2, "%d-%m-%Y")
               return ad2.strftime("%d/%m/%Y")
          except ValueError:
               return ad2
          
def print_report_after(report_name):                                  
    folder_report_after = daily_report_path
    report_PDF = os.path.join(folder_report_after, report_name).__add__(".PDF")
    report_PDF_to_URL = "file:" + report_PDF.replace("\\", "/")
    subprocess.run(["cmd", "/c", "start", "msedge", report_PDF_to_URL])

def print_report_before(report_name):                                  
    folder_report_before = daily_report_path.__add__(r"\Before Closeday")
    report_PDF = os.path.join(folder_report_before, report_name).__add__(".PDF")
    report_PDF_to_URL = "file:" + report_PDF.replace("\\", "/")
    subprocess.run(["cmd", "/c", "start", "msedge", report_PDF_to_URL])

def print_page_config(set_copy, set_both, set_segment):
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
    pyautogui.press("down", presses=(set_segment), interval=.01)
    pyautogui.press("tab", presses=3, interval=.01)
    time.sleep(.5)
    pyautogui.press("enter", interval=.01)
    pyautogui.hotkey("ctrl", "w", interval=.01)

def remove_file(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)