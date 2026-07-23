import customtkinter, subprocess, threading, os, json
from tkinter import *

window_main = customtkinter.CTk()
window_main.title("ngt")
window_main.geometry("1650+30")

window_main.attributes("-topmost", True)
window_main.resizable(False, False)

switch_mode = StringVar()

def mode_show():
    get_mode = switch_mode.get()
    if get_mode == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

drop_1_select = StringVar()
drop_1_link = {}

def link_theme():
    path_1 = os.path.dirname(os.path.abspath(__file__))
    path_2 = os.path.join(path_1, "themes")
    for _ in os.listdir(path_2):
        if _.endswith(".json"):
            key_theme = os.path.splitext(_)[0]
            key_theme_link = os.path.join(path_2, _)
            drop_1_link[key_theme] = key_theme_link

link_theme()
drop_1_list = list(drop_1_link.keys())

def use_theme(_=None):
    drop_1_get = drop_1_select.get()
    if drop_1_get in drop_1_link:
        to_json = drop_1_link[drop_1_get]
        with open(to_json, "r", encoding="utf-8") as file:
            json_file = json.load(file)
        to_CTkButton = json_file.get("CTkButton", {})
        fg_color = to_CTkButton.get("fg_color")
        hover_color = to_CTkButton.get("hover_color")
        if fg_color and hover_color:
            for _ in [button_1, button_2, button_3]:
                _.configure(fg_color=fg_color, hover_color=hover_color)

link_file_process = {"endday_before": None, "endday_after": None, "FB_print": None}

def block_button(state):
    for _ in [button_1, button_2, button_3]:
        _.configure(state=state)

def monitor_process(_):
    _.wait()
    window_main.after(0, lambda: block_button("normal"))

def run_script(path, key):
    global link_file_process
    if link_file_process[key] and link_file_process[key].poll() is None:
        return
    block_button("disabled")
    run_file = subprocess.Popen(["python", path])
    link_file_process[key] = run_file
    threading.Thread(target=monitor_process, args=(run_file,), daemon=True).start()

def endday_before():
    run_script(r"report\end-day_before\main_end-day_before.py", "endday_before")

def endday_after():
    run_script(r"report\end-day_after\main_end-day_after.py", "endday_after")

def FB_print():
    run_script(r"fb print\main_FB_print.py", "FB_print")

def stop_all():
    global link_file_process
    for _ in link_file_process.values():
        if _ and _.poll() is None:
            _.terminate()
    block_button("normal")

frame_1 = customtkinter.CTkFrame(master=window_main)
frame_1.pack(padx=2.5, pady=2.5, fill="both", expand=True)

switch = customtkinter.CTkSwitch(master=frame_1, variable=switch_mode, onvalue="on", offvalue="off", width=1, text="", command=mode_show)
switch.pack(anchor=E)

label_1 = customtkinter.CTkLabel(master=frame_1, text="OI", font=("Sans-serif", 20))
label_1.pack(pady=(10, 25))

button_1 = customtkinter.CTkButton(master=frame_1, text="Before", command=endday_before)
button_1.pack(pady=0)

button_2 = customtkinter.CTkButton(master=frame_1, text="After", command=endday_after)
button_2.pack(pady=(7.5, 0))

button_3 = customtkinter.CTkButton(master=frame_1, text="FB Print", command=FB_print)
button_3.pack(pady=(7.5, 0))

button_stop = customtkinter.CTkButton(master=frame_1, text="Stop", fg_color=["#BEC7C9", "#495054"], hover_color="#E05454", command=stop_all)
button_stop.pack(padx=5, pady=(55, 5))

drop_1 = customtkinter.CTkComboBox(master=frame_1, variable=drop_1_select, values=drop_1_list, command=use_theme)
drop_1.pack()

window_main.mainloop()