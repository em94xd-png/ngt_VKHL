import os

Endday_before_folder = r"C:\Users\dutymanager.vkhl\Documents\Runit\Report\End-day_before"

Room_Discrepancy = "Room Discrepancy"

local_file = os.path.join(Endday_before_folder, Room_Discrepancy)
file_url = "file:///" + os.path.abspath(local_file).replace("\\", "/").__add__(".PDF")

print(file_url)