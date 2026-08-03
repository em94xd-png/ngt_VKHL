import tkinter, threading, os, sys, pygetwindow, pyautogui, pyperclip, time, openpyxl, shutil
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

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

wd = tkinter.Tk()
wd.title("")

wd.attributes("-topmost", True)
wd.resizable(False, False)

wd_width = 150
wd_height = 200

screen_width = wd.winfo_screenwidth()
screen_height = wd.winfo_screenheight()

center_x = int(screen_width / 2 - wd_width / 2)
center_y = int(screen_height / 2 - wd_height / 2)

wd.geometry(f"{wd_width}x{wd_height}+{center_x}+{center_y}")

tray_icon = None
is_tray_running = False

def create_image():
    image = Image.new("RGB", (64, 64), color="white")
    dc = ImageDraw.Draw(image)
    dc.ellipse([(16, 16), (48, 48)], fill="green")
    return image

def show_window(icon=None, item=None):
    global tray_icon, is_tray_running
    if tray_icon:
        tray_icon.stop()
        is_tray_running = False
    wd.after(0, wd.deiconify)
    wd.after(0, lambda: wd.state("normal"))

def hide_window():
    global tray_icon, is_tray_running
    wd.withdraw()
    menu = Menu(
        MenuItem("Open", show_window, default=True, visible=False),
        MenuItem("Close", exit_it)
    )
    tray_icon = Icon("", create_image(), "", menu)
    is_tray_running = True
    threading.Thread(target=tray_icon.run, daemon=True).start()

def on_minimize(event):
    if wd.state() == "iconic":
        hide_window()

def exit_it(icon=None, item=None):
    stop_it()
    global tray_icon
    if tray_icon:
        tray_icon.stop()
    wd.destroy()

wd.bind("<Unmap>", on_minimize)
wd.protocol("WM_DELETE_WINDOW", exit_it)

snf = False

def get_data():
    global snf
    if not snf:
        snf = True
        block_button(state="disabled")
        threading.Thread(target=run_script, daemon=True).start()

def stop_it():
    global snf
    if snf:
        snf = False
        block_button(state="normal")

def run_script():
    global snf
    while snf:
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
                    wb.close()
                    while True:
                        pygetwindow.getWindowsWithTitle(main_panel)
                        if not pygetwindow.getWindowsWithTitle(main_panel):
                            pygetwindow.getWindowsWithTitle(sub_panel)
                            if not pygetwindow.getWindowsWithTitle(sub_panel):
                                break
            if not os.path.exists(path_td_snf_excel):
                if not os.path.exists(fr"{script_config.path_share}\OTH"):
                    sys.exit()
                shutil.copy(os.path.join(os.path.dirname(os.path.abspath("get_data.xlsx"))), path_td_snf_excel)
                if os.path.exists(path_td_snf_excel):
                    continue
        time.sleep(1)

def block_button(state):
    for _ in [btn1]:
        _.configure(state=state)

btn1 = tkinter.Button(master=wd, text="run_it", width=15, command=get_data)
btn1.pack(pady=30)

btn2 = tkinter.Button(master=wd, text="stop_it", width=15, command=stop_it)
btn2.pack(pady=0)

wd.mainloop()