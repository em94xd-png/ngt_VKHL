import os
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
ytd_date = yesterday.strftime("%#d")
ytd_month = yesterday.strftime("%#m")
ytd_month_full = yesterday.strftime("%b")
ytd_year = yesterday.strftime("%y")
ytd_year_full = yesterday.strftime("%Y")

path = fr"\\LMPC202507256L\Keeper\Daily's Report\Report {ytd_year_full}\{ytd_month} - {ytd_month_full} {ytd_year}\{ytd_date} {ytd_month_full}\Before Closeday"

path_to = os.path.exists(path)

print(path_to)