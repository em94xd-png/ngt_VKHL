import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
ytd_date = yesterday.strftime("%#d")
ytd_month_number = yesterday.strftime("%#m")
ytd_month_short = yesterday.strftime("%b")
ytd_month_full = yesterday.strftime("%B")
ytd_year = yesterday.strftime("%y")
ytd_year_full = yesterday.strftime("%Y")

path = fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month_number} - {ytd_month_short} {ytd_year_full}\{ytd_date} {ytd_month_full}\Before Closeday"

# path = os.environ.get("USERPROFILE").__add__(r"\Documents").__add__(r"\D\AAA\F")

path_to = os.path.exists(path)

os.makedirs(path, exist_ok=True)

# print(path)