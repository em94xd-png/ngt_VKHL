import pygetwindow, pyautogui, pyperclip, time, openpyxl, os, shutil, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import script_config

td_snf_excel = f"get_{script_config.td_dot_dd_mm_yy}.xlsx"
path_td_snf_excel = os.path.join(fr"{script_config.path_share}\OTH", td_snf_excel)

main_panel = "Guest information panel"
sub_panel = "Scanning manager"

def step_copy(times):
    pyautogui.PAUSE = 0.01
    for _ in range(times):
        pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "c")
    return pyperclip.paste().strip()

def path_to_file(_):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, _)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), _)

while True:
    if pygetwindow.getWindowsWithTitle(main_panel):
        main_title = pygetwindow.getWindowsWithTitle(main_panel)[0]
        if os.path.exists(path_td_snf_excel):
            if not main_title.isMinimized:
                main_title.activate()
                time.sleep(.5)
                ln = step_copy(3)
                fn = step_copy(4)
                bd = step_copy(9)
                ct = step_copy(5)
                pn = step_copy(6)
                wb = openpyxl.load_workbook(path_td_snf_excel)
                ws3 = wb["Sheet3"]
                ws3.append([ln, fn, bd, ct, pn])
                wb.save(path_td_snf_excel)
                while True:
                    pygetwindow.getWindowsWithTitle(main_panel)
                    if not pygetwindow.getWindowsWithTitle(main_panel):
                        pygetwindow.getWindowsWithTitle(sub_panel)
                        if not pygetwindow.getWindowsWithTitle(sub_panel):
                            break
        if not os.path.exists(path_td_snf_excel):
            if not os.path.exists(fr"{script_config.path_share}\OTH"):
                sys.exit()
            shutil.copy(path_to_file("get_data.xlsx"), path_td_snf_excel)
            if os.path.exists(path_td_snf_excel):
                continue