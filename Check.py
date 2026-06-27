import os
from datetime import date, timedelta

def report_path():
    yesterday = date.today() - timedelta(days=1)
    ytd_date = yesterday.strftime("%#d")
    ytd_month_number = yesterday.strftime("%#m")
    ytd_month_short = yesterday.strftime("%b")
    ytd_month_full = yesterday.strftime("%B")
    ytd_year_full = yesterday.strftime("%Y")

    return fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}"

# path = os.environ.get("USERPROFILE").__add__(r"\Documents").__add__(r"\D\AAA\F")

# path_to = os.path.exists(path)

# os.makedirs(path, exist_ok=True)

# Room_Discrepancy = "Room Discrepancy"

# test = os.path.join(report_path().__add__(r"\Before Closeday"), Room_Discrepancy).__add__(".PDF")

# test_2 = "file:" + test.replace("\\", "/")

print(report_path())