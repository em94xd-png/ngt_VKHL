import pygetwindow, pyautogui, pyperclip, time, openpyxl, os
from datetime import date, timedelta

td = date.today()
td_date = td.strftime("%d.%m.%y")
ytd = date.today() - timedelta(days=1)
ytd_date = ytd.strftime("%d.%m.%y")

data_path = r"\\LMPC202507256L\Keeper\OTH"
os.makedirs(data_path, exist_ok=True)

new_data_excel = f"get_{td_date}.xlsx"
path_new_data_excel = os.path.join(data_path, new_data_excel)

ytd_data_excel = f"get_{ytd_date}.xlsx"
path_ytd_data_excel = os.path.join(data_path, ytd_data_excel)

target_title = "Guest information panel"

def get_it(times):
    pyautogui.PAUSE = 0.01
    for _ in range(times):
        pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "c")
    return pyperclip.paste().strip()

while True:
    try:
        find_title = pygetwindow.getWindowsWithTitle(target_title)[0]
        if not find_title.isMinimized:
            find_title.activate()
            time.sleep(.5)
            ln = get_it(3)
            fn = get_it(4)
            bd = get_it(9)
            ct = get_it(5)
            pn = get_it(6)
            if path_new_data_excel:
                wb = openpyxl.load_workbook(path_new_data_excel)
                ws3 = wb["Sheet3"]
                ws3.append([ln, fn, bd, ct, pn])
                wb.save(path_new_data_excel)
            else:
                wb = openpyxl.load_workbook(path_ytd_data_excel)
                ws3 = wb["Sheet3"]
                ws3.append([ln, fn, bd, ct, pn])
                wb.save(path_ytd_data_excel)
            time.sleep(15)
    except Exception as error:
        pass