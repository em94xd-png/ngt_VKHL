import pygetwindow, pyautogui, pyperclip, time, openpyxl, os
from datetime import date

td = date.today()
td_date = td.strftime("%d.%m.%y")

data_path = r"\\LMPC202507256L\Keeper\OTH"
new_data_excel = f"get_{td_date}.xlsx"
path_new_data_excel = os.path.join(data_path, new_data_excel)

target_title = "Guest information panel"

def get_it(times):
    pyautogui.PAUSE = 0.001
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
            last_name = get_it(3)
            first_name = get_it(4)
            birth_day = get_it(9)
            country = get_it(5)
            passport_number = get_it(6)
            wb = openpyxl.load_workbook(path_new_data_excel)
            ws3 = wb["Sheet3"]
            ws3.append([last_name, first_name, birth_day, country, passport_number])
            wb.save(path_new_data_excel)
            time.sleep(15)
    except Exception as error:
        pass