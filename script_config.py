import pyautogui, os, subprocess, time, calendar, pygetwindow
from datetime import date, timedelta, datetime
from urllib.parse import urlparse, parse_qs

path_device = "LMPC202507256L"
path_share = fr"\\{path_device}\Storage"
path_ = os.environ.get("USERPROFILE")

site_OPERA = "https://mtca2.oraclehospitality.ap-singapore-1.ocs.oraclecloud.com/MINOR/operacloud/faces/opera-cloud-index/OperaCloud"

Room_Type = "1H2XK,1H2XT,1H3XK,1H4XK,1H4XT,2U1XKT,2U2XKT,2U3XKT,1V1XK,1V2XK,3U1CKT,2V1C2K,1H1VK,1U1VK,1U2VK,2U1VKT,2U2VKT,2U3VKT,3U2VKT,1H2VK,2U4XKT,3U1C2K"

Room_Class = "HRA,HRB,HRC,HRD,HSA,HSB,HSC,HSD,HSE,HVA,HVB,HVC"

td = date.today()
td_short_date = td.strftime("%#d")
td_full_d = td.strftime("%A")
td_full_m = td.strftime("%B")
td_yyyy = td.strftime("%Y")
td_dd_mm = td.strftime("%d%m")
td_hp_dd_mm = td.strftime("%d-%b")
td_dot_dd_mm_yy = td.strftime("%d.%m.%y")
td_hp_dd_mm_yy = td.strftime("%d-%b-%y")

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
ytd_hp_dd_mm_yy = ytd.strftime("%d-%b-%y")
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

daily_report_path = fr"{path_share}\Daily's Report\Report {ytd_yyyy}\{ytd_order_m} - {ytd_short_m} {ytd_yyyy}\{ytd_short_date} {ytd_full_m}"

def first_OPERA_open():
    while True:
        if pyautogui.pixelMatchesColor(7, 391, (251, 249, 248), tolerance=0):
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
        if pyautogui.pixelMatchesColor(139, 129, (48,  54,  76), tolerance=0):
            break

def search_reports():
    while True:
        if pyautogui.pixelMatchesColor(320, 275, (60,  66,  91), tolerance=10):
            break

def search_enter_step1():
    while True:
        if pyautogui.pixelMatchesColor(1853, 361, (246, 246, 246), tolerance=10):
            break

def search_enter_step2():
    while True:
        if pyautogui.pixelMatchesColor(1853, 361, (49,  45,  42), tolerance=10):
            break

def search_enter_step3():
    while True:
        if pyautogui.pixelMatchesColor(1712, 554, (49,  45,  42), tolerance=10):
            break

def config_report():
    while True:
        if pyautogui.pixelMatchesColor(320, 275, (255, 255, 255), tolerance=10):
            break

def wait_report():
    while True:
        if pyautogui.pixelMatchesColor(1866, 975, (213, 163, 160), tolerance=10):
            break

def tab_reserve(times):
    pyautogui.PAUSE = 0.01
    for _ in range(times):
        pyautogui.hotkey("shift", "tab")

def download_as():
    while True:
        if pyautogui.pixelMatchesColor(985, 512, (60,  66,  91), tolerance=10):
            break

def download_as_2():
    while True:
        if pyautogui.pixelMatchesColor(988, 498, (60,  66,  91), tolerance=10):
            break
          
def download_page():
    while True:
        if pyautogui.pixelMatchesColor(1508, 52, (39, 35, 32), tolerance=10):
            time.sleep(.5)
            break

def not_download_page():
    while True:
        if not pyautogui.pixelMatchesColor(1508, 52, (39, 35, 32), tolerance=10):
            time.sleep(.5)
            break

def stay_excel():
    while True:
        if pyautogui.pixelMatchesColor(1894, 56, (16, 124, 65), tolerance=10):
            break

def not_stay_excel():
    while True:
        if not pyautogui.pixelMatchesColor(1894, 56, (16, 124, 65), tolerance=10):
            break

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
    pyautogui.hotkey("ctrl", "shift", "p", interval=.01)
    while True:
        if pyautogui.pixelMatchesColor(562, 575, (111, 145, 192), tolerance=10):
            break
    time.sleep(.25)
    pyautogui.press("tab", presses=5, interval=.01)
    pyautogui.press("enter", interval=.01)
    while True:
        if pyautogui.pixelMatchesColor(771, 707, (47, 55, 248), tolerance=10):
            break
    time.sleep(.25)
    pyautogui.press("tab", presses=18, interval=.01)
    pyautogui.press("up", presses=3, interval=.01)
    pyautogui.press("down", presses=(set_segment), interval=.01)
    if set_segment == 0:
        pyautogui.press("tab", presses=2, interval=.01)
        pyautogui.press("up", presses=3, interval=.01)
        pyautogui.press("down", presses=(set_both), interval=.01)
    if set_segment == 1:
        pyautogui.press("tab", presses=3, interval=.01)
        pyautogui.press("up", presses=3, interval=.01)
        pyautogui.press("down", presses=(set_both), interval=.01)
    pyautogui.press("tab", presses=2, interval=.01)
    pyautogui.write(f"{set_copy}", interval=.01)
    pyautogui.press("tab", interval=.01)
    pyautogui.press("enter", interval=.01)
    while True:
        if not pyautogui.pixelMatchesColor(771, 707, (47, 55, 248), tolerance=10):
            break
    time.sleep(.25)
    pyautogui.press("tab", interval=.01)
    pyautogui.press("enter", interval=.01)
    while True:
        if not pyautogui.pixelMatchesColor(1362, 150, (31, 121, 199), tolerance=10):
            break
    time.sleep(1.5)
    pyautogui.hotkey("ctrl", "w", interval=.01)
    time.sleep(.5)

def remove_file(path):
    for _ in os.listdir(path):
        to_file = os.path.join(path, _)
        if os.path.isfile(to_file):
            os.remove(to_file)

def return_print_default():
    printer = "VKHL_RICOHP502_GSA02"
    command = f'rundll32.exe printui.dll,PrintUIEntry /e /n "{printer}"'
    subprocess.Popen(command, shell=True)
    if pygetwindow.getWindowsWithTitle("Printing Preferences"):
        pygetwindow.getWindowsWithTitle("Printing Preferences")[0].activate()
    time.sleep(.5)
    pyautogui.press("tab", presses=18, interval=.01)
    pyautogui.press("up", presses=3, interval=.01)
    pyautogui.press("tab", presses=2, interval=.01)
    pyautogui.press("up", presses=3, interval=.01)
    pyautogui.press("tab", presses=3, interval=.01)
    pyautogui.press("enter", interval=.01)

def num_row(num):
    vba = ""
    for _ in range(num):
        vba += "    Application.CutCopyMode = False\n"
        vba += "    Selection.Copy\n"
        vba += "    Selection.Insert Shift:=xlDown\n"
    return vba

# path_OTH = path_share.__add__(r"\OTH")

# ori_excel_file = "02.10.26.xlsm"
# path_ori_excel = os.path.join(path_OTH, ori_excel_file)

# from openpyxl import load_workbook

# wb = load_workbook(path_ori_excel, keep_vba=True)

# ws = "02.10.26"
# ws = wb[ws]



# import xml.etree.ElementTree

# arr = "res_detail_155360773.XML"
# arrival = os.path.join(path_.__add__(r"\Downloads"), arr)

# tree = xml.etree.ElementTree.parse(arrival)
# root = tree.getroot()

# arr = root.findall(".//G_RESERVATION")
# arr_row = 1 + len(arr)

# dep = "departure_all_155360472.XML"
# departure = os.path.join(path_.__add__(r"\Downloads"), dep)

# tree = xml.etree.ElementTree.parse(departure)
# root = tree.getroot()

# dep = root.findall(".//G_ROOM")
# dep_row = 1 + len(dep)

# vac_file = "hkvacroom_155355874.XML"
# vac = os.path.join(path_.__add__(r"\Downloads"), vac_file)

# tree = xml.etree.ElementTree.parse(vac)
# root = tree.getroot()

# rm_collect = []

# for _ in root.findall(".//G_ROOM"):
#     rm = _.find("ROOM").text
#     if _.find("RESV_STATUS").text == "Not Reserved":
#         rm_collect.append(str(int(rm)))

# under_100 = [x for x in rm_collect if int(x) <= 100]
# over_100 = [x for x in rm_collect if int(x) > 100]
# under_100_value = ", ".join(under_100)
# over_100_value = ", ".join(over_100)
# ws[f"G{arr_row + dep_row + 38}"] = under_100_value
# ws[f"G{arr_row + dep_row + 39}"] = over_100_value

# ws[f"P{arr_row + dep_row + 38}"] = len(under_100)
# ws[f"P{arr_row + dep_row + 39}"] = len(over_100)

# wb.save(path_ori_excel)
# wb.close()