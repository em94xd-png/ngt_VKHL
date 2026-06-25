import customtkinter
from tkinter import *
import subprocess
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

window_main = customtkinter.CTk()
window_main.title("ngt")

# Locked_x = 2300
# Locked_y = 100
# window_main.geometry("")

window_main.attributes("-topmost", True)
window_main.resizable(False, False)  # Disables horizontal and vertical resizing

frame_1 = customtkinter.CTkFrame(master=window_main, width=200, height=325)
frame_1.pack()

label_1 = customtkinter.CTkLabel(master=frame_1, text="OI", font=("Sans-serif", 20) )
label_1.place(relx=.5, rely=.13, anchor=CENTER)

running_endday_before = None

def report_endday_before():
    global running_endday_before
    if running_endday_before and running_endday_before.poll() is None:
        return
    running_endday_before = subprocess.Popen(["python", r"report\end-day_before\Main_End-day_before.py"])

button_1 = customtkinter.CTkButton(master=frame_1, text="Before", command=report_endday_before)
button_1.place(relx=.5, rely=.3, anchor=CENTER)

running_endday_after = None

def report_endday_after():
    global running_endday_after
    if running_endday_after and running_endday_after.poll() is None:
        return
    subprocess.Popen(["python", r"report\end-day_after\Main_End-day_after.py"])

button_2 = customtkinter.CTkButton(master=frame_1, text="After", command=report_endday_after)
button_2.place(relx=.5, rely=.415, anchor=CENTER)

running_FB_print = None

def FB_print():
    global running_FB_print
    if running_FB_print and running_FB_print.poll() is None:
        return 
    subprocess.Popen(["python", r"fb print\Main_FB_Print.py"])

button_3 = customtkinter.CTkButton(master=frame_1, text="FB Print", command=FB_print)
button_3.place(relx=.5, rely=.53, anchor=CENTER)

def stop_all():
    global running_endday_before, running_endday_after, running_FB_print
    running_active = [running_endday_before, running_endday_after, running_FB_print]
    for running in running_active:
        if running and running.poll() is None:
            running.terminate()

button_stop = customtkinter.CTkButton(master=frame_1, text="Stop", fg_color="#428475", hover_color="#E05454", command=stop_all)
button_stop.place(relx=.5, rely=.885, anchor=CENTER)

window_main.mainloop()