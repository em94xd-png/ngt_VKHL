import customtkinter
from tkinter import *
import subprocess
import threading

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window_main = customtkinter.CTk()
window_main.title("ngt")

# Locked_x = 2300
# Locked_y = 100
# window_main.geometry("")

window_main.attributes("-topmost", True)
window_main.resizable(False, False)

running_endday_before = None
running_endday_after = None
running_FB_print = None

def button_toggle(state):
    button_1.configure(state=state)
    button_2.configure(state=state)
    button_3.configure(state=state)

def monitor_process():
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

frame_1 = customtkinter.CTkFrame(master=window_main, width=200, height=325)
frame_1.pack()

label_1 = customtkinter.CTkLabel(master=frame_1, text="OI", font=("Sans-serif", 20))
label_1.place(relx=.5, rely=.13, anchor=CENTER)

button_1 = customtkinter.CTkButton(master=frame_1, text="Before", command=report_endday_before)
button_1.place(relx=.5, rely=.3, anchor=CENTER)

button_2 = customtkinter.CTkButton(master=frame_1, text="After", command=report_endday_after)
button_2.place(relx=.5, rely=.415, anchor=CENTER)

button_3 = customtkinter.CTkButton(master=frame_1, text="FB Print", command=FB_print)
button_3.place(relx=.5, rely=.53, anchor=CENTER)

button_stop = customtkinter.CTkButton(master=frame_1, text="Stop", fg_color="#428475", hover_color="#E05454", command=stop_all)
button_stop.place(relx=.5, rely=.885, anchor=CENTER)

window_main.mainloop()