import customtkinter, subprocess, threading, os, json
from tkinter import *

window_main = customtkinter.CTk()
window_main.title("ngt")
window_main.geometry("1650+30")

window_main.attributes("-topmost", True)
window_main.resizable(False, False)

mode = StringVar()

def show_mode():
    get_mode = mode.get()
    if get_mode == "on":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")

theme = StringVar()
theme_dict = {}

def link_theme():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "themes")
    for _ in os.listdir(path):
        if _.endswith(".json"):
            key_theme = os.path.splitext(_)[0]
            path_key_theme = os.path.join(path, _)
            theme_dict[key_theme] = path_key_theme

link_theme()
theme_list = list(theme_dict.keys())

def use_theme(_=None):
    get_theme = theme.get()
    if get_theme in theme_dict:
        json_file = theme_dict[get_theme]
        with open(json_file, "r", encoding="utf-8") as file:
            theme_json = json.load(file)
        fg_color = theme_json.get("CTkButton", {}).get("fg_color")
        hover_color = theme_json.get("CTkButton", {}).get("hover_color")
        if fg_color and hover_color:
            for _ in [button_endday_before, button_endday_after, button_tm_rr4, button_briefing, button_fb_print]:
                _.configure(fg_color=fg_color, hover_color=hover_color)

main_file = {"endday_before": None, "endday_after": None, "tm_rr4": None, "briefing": None, "fb_print": None}

def block_button(state):
    for _ in [button_endday_before, button_endday_after, button_tm_rr4, button_briefing, button_fb_print]:
        _.configure(state=state)

def monitor_process(_):
    _.wait()
    window_main.after(0, lambda: block_button("normal"))

def run_script(path, key):
    global main_file
    if main_file[key] and main_file[key].poll() is None:
        return
    block_button("disabled")
    run_file = subprocess.Popen(["python", path])
    main_file[key] = run_file
    threading.Thread(target=monitor_process, args=(run_file,), daemon=True).start()

def endday_before():
    run_script(r"Report\End-day_before\main_end-day_before.py", "endday_before")

def endday_after():
    run_script(r"Report\End-day_after\main_end-day_after.py", "endday_after")

def tm_rr4():
    run_script(r"TM, RR4\main_tm_rr4.py", "tm_rr4")

def briefing():
    run_script(r"Briefing\main_briefing.py", "briefing")

def fb_print():
    run_script(r"FB Print\main_fb_print.py", "fb_print")

def stop_all():
    global main_file
    for _ in main_file.values():
        if _ and _.poll() is None:
            _.terminate()
    block_button("normal")

frame_main = customtkinter.CTkFrame(master=window_main)
frame_main.pack(padx=2.5, pady=2.5, fill="both", expand=True)

switch_mode = customtkinter.CTkSwitch(master=frame_main, variable=mode, onvalue="on", offvalue="off", width=1, text="", command=show_mode)
switch_mode.pack(anchor=E)

label_title = customtkinter.CTkLabel(master=frame_main, text="OI", font=("Sans-serif", 20))
label_title.pack(pady=(10, 25))

button_endday_before = customtkinter.CTkButton(master=frame_main, text="Before", command=endday_before)
button_endday_before.pack(pady=0)

button_endday_after = customtkinter.CTkButton(master=frame_main, text="After", command=endday_after)
button_endday_after.pack(pady=(7.5, 0))

button_tm_rr4 = customtkinter.CTkButton(master=frame_main, text="TM, RR4", command=tm_rr4)
button_tm_rr4.pack(pady=(7.5, 0))

button_briefing = customtkinter.CTkButton(master=frame_main, text="Briefing", command=briefing)
button_briefing.pack(pady=(7.5, 0))

button_fb_print = customtkinter.CTkButton(master=frame_main, text="FB Print", command=fb_print)
button_fb_print.pack(pady=(7.5, 0))

button_stop_all = customtkinter.CTkButton(master=frame_main, text="Stop", fg_color=["#BEC7C9", "#495054"], hover_color="#E05454", command=stop_all)
button_stop_all.pack(padx=5, pady=(55, 5))

combobox_theme = customtkinter.CTkComboBox(master=frame_main, variable=theme, values=theme_list, command=use_theme)
combobox_theme.pack()

window_main.mainloop()