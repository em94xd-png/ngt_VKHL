import pyautogui, os
from datetime import date, timedelta, datetime
from urllib.parse import urlparse, parse_qs

device_path = "LMPC202507256L"
snf_path = fr"\\{device_path}\Keeper\OTH"
download_path = os.environ.get("USERPROFILE").__add__(r"\Downloads")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

td = date.today()
td_dot_dd_mm_yy = td.strftime("%d.%m.%y")

ytd = date.today() - timedelta(days=1)
ytd_y_to_be = ytd.year + 543
ytd_full_m = ytd.strftime("%B")
ytd_yyyy = ytd.strftime("%Y")
ytd_dd_mm = ytd.strftime("%d%m")
ytd_dot_dd_mm_yy = ytd.strftime("%d.%m.%y")
ytd_dot_dd_mm_yyyy = ytd.strftime("%d.%m.%Y")
ytd_to_mm_dd_yyyy = ytd.strftime("%m/%d/%Y")
ytd_dd_mm_yyyy_be = ytd.strftime(f"%d%m{ytd_y_to_be}")

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