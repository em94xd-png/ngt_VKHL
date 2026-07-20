import pygetwindow, pyautogui, pyperclip, time, openpyxl, os
from datetime import date

td = date.today()
td_date = td.strftime("%d.%m.%y")

data_path = r"\\LMPC202507256L\Keeper\OTH"
new_data_excel = f"get_{td_date}.xlsx"
path_new_data_excel = os.path.join(data_path, new_data_excel)

main_panel = "Guest information panel"
sub_panel = "Scanning manager"

def get_it(times):
    pyautogui.PAUSE = 0.01
    for _ in range(times):
        pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "c")
    return pyperclip.paste().strip()

while True:
    try:
        if not os.path.exists(path_new_data_excel):
            while not os.path.exists(path_new_data_excel):
                continue
        main_title = pygetwindow.getWindowsWithTitle(main_panel)[0]
        if not main_title.isMinimized:
            main_title.activate()
            time.sleep(.5)
            ln = get_it(3)
            fn = get_it(4)
            bd = get_it(9)
            ct = get_it(5)
            pn = get_it(6)
            wb = openpyxl.load_workbook(path_new_data_excel)
            ws3 = wb["Sheet3"]
            ws3.append([ln, fn, bd, ct, pn])
            wb.save(path_new_data_excel)
            while True:
                main_title = pygetwindow.getWindowsWithTitle(main_panel)[0]
                if not main_title:
                    sub_title = pygetwindow.getWindowsWithTitle(sub_panel)[0]
                    if not sub_title:
                        break
    except Exception as error:
        pass