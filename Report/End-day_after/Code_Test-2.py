from datetime import date
import calendar
import os


Endday_after_folder = os.environ.get("USERPROFILE").__add__(r"\Documents\Runit\Report\End-day_after")

print(Endday_after_folder)