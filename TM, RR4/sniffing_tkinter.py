import tkinter, subprocess, threading, os, sys
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

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

put_data = {"get_data": None}

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

def get_data():
    run_script("get_data.py", "get_data")

def path_to_file(_):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, _)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), _)

def run_script(path, key):
    global put_data
    if put_data[key] and put_data[key].poll() is None:
        return
    block_button(state="disabled")
    run_file = subprocess.Popen(["pythonw", path_to_file(path)])
    put_data[key] = run_file
    threading.Thread(target=monitor_it, args=(run_file,), daemon=True).start()

def monitor_it(_):
    _.wait()
    wd.after(0, lambda: block_button(state="normal"))

def block_button(state):
    for _ in [btn1]:
        _.configure(state=state)

def stop_it():
    global put_data
    for _ in put_data.values():
        if _ and _.poll() is None:
            _.terminate()
    block_button(state="normal")

btn1 = tkinter.Button(master=wd, text="run_it", width=15, command=get_data)
btn1.pack(pady=30)

btn2 = tkinter.Button(master=wd, text="stop_it", width=15, command=stop_it)
btn2.pack(pady=0)

wd.mainloop()