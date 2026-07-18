import customtkinter
from tkinter import *
import subprocess
import threading
import os
import json

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")

window_main = customtkinter.CTk()
window_main.title("ngt")
# window_main.overrideredirect(True)
window_main.geometry("1650+30")

# customtkinter.set_widget_scaling(.9)
# customtkinter.set_window_scaling(.9)

window_main.attributes("-topmost", True)
window_main.resizable(False, False)

switch_mode = StringVar()

def mode_show():
    mode_get = switch_mode.get()

    if mode_get == "on":
        customtkinter.set_appearance_mode("dark")
    
    else:
        customtkinter.set_appearance_mode("light")

drop_1_store = StringVar()
drop_1_path = {}

def theme_path():
    path_1 = os.path.dirname(os.path.abspath(__file__))
    path_2 = os.path.join(path_1, "themes")
    
    for _ in os.listdir(path_2):
        if _.endswith(".json"):
            theme_key = os.path.splitext(_)[0]
            theme_key_path = os.path.join(path_2, _)
            drop_1_path[theme_key] = theme_key_path

theme_path()
drop_1_items = list(drop_1_path.keys())

def theme_use(_=None):
    drop_1_get = drop_1_store.get()
    
    if drop_1_get in drop_1_path:
        to_json = drop_1_path[drop_1_get]

        with open(to_json, "r", encoding="utf-8") as file:
            from_json = json.load(file)

        drop_1_json = from_json.get("CTkButton", {})
        fg_color = drop_1_json.get("fg_color")
        hover_color = drop_1_json.get("hover_color")

        if fg_color and hover_color:
            for _ in [button_1, button_2, button_3]:
                _.configure(fg_color=fg_color, hover_color=hover_color)

running_endday_before = None
running_endday_after = None
running_FB_print = None

def button_toggle(state):
    button_1.configure(state=state)
    button_2.configure(state=state)
    button_3.configure(state=state)

def monitor_process(process):
    process.wait()
    window_main.after(0, lambda: button_toggle("normal"))

def script_run(script_path, process_var):
    global running_endday_before, running_endday_after, running_FB_print

    process_current = globals()[process_var]

    if process_current and process_current.poll() is None:
        return
    
    button_toggle("disabled")

    file_run = subprocess.Popen(["python", script_path])
    globals()[process_var] = file_run

    threading.Thread(target=monitor_process, args=(file_run,), daemon=True).start()

def report_endday_before():
    script_run(r"report\end-day_before\Main_End-day_before.py", "running_endday_before")

def report_endday_after():
    script_run(r"report\end-day_after\Main_End-day_after.py", "running_endday_after")

def FB_print():
    script_run(r"fb print\Main_FB_Print.py", "running_FB_print")

def stop_all():
    global running_endday_before, running_endday_after, running_FB_print
    
    running_active = [running_endday_before, running_endday_after, running_FB_print]

    for _ in running_active:
        if _ and _.poll() is None:
            _.terminate()

    button_toggle("normal")

frame_1 = customtkinter.CTkFrame(master=window_main)
frame_1.pack(padx=2.5, pady=2.5, fill="both", expand=True)

switch = customtkinter.CTkSwitch(master=frame_1, variable=switch_mode, onvalue="on", offvalue="off", width=1, text="", command=mode_show)
switch.pack(anchor=E)

label_1 = customtkinter.CTkLabel(master=frame_1, text="OI", font=("Sans-serif", 20))
label_1.pack(pady=25)

button_1 = customtkinter.CTkButton(master=frame_1, text="Before", command=report_endday_before)
button_1.pack(pady=0)

button_2 = customtkinter.CTkButton(master=frame_1, text="After", command=report_endday_after)
button_2.pack(pady=(7.5, 0))

button_3 = customtkinter.CTkButton(master=frame_1, text="FB Print", command=FB_print)
button_3.pack(pady=(7.5, 0))

button_stop = customtkinter.CTkButton(master=frame_1, text="Stop", fg_color=["#BEC7C9", "#495054"], hover_color="#E05454", command=stop_all)
button_stop.pack(padx=5, pady=(55, 5))

# button_exit = customtkinter.CTkButton(master=frame_1, width=10, height=30, text="x", font=("Sans-serif", 10), fg_color="transparent", hover=False, corner_radius=30, command=window_main.quit)
# button_exit.pack(padx=5, pady=(55, 15))

drop_1 = customtkinter.CTkComboBox(master=frame_1, variable=drop_1_store, values=drop_1_items, command=theme_use)
drop_1.pack()

window_main.mainloop()