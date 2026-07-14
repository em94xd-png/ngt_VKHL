import openpyxl
import os
from datetime import date, timedelta

ytd = date.today() - timedelta(days=1)
ytd_y = ytd.strftime("%Y")
ytd_m = ytd.strftime("%B")
tm_date = ytd.strftime("%d.%m.%Y")

tm_path = fr"\\LMPC202507256L\Keeper\TM\{ytd_y}\{ytd_m}"
save_tm_excel = os.path.join(tm_path, tm_date)

print(save_tm_excel)

# tm_path = fr"\\LMPC202507256L\Keeper\TM\{ytd_y}\{ytd_m}"

# os.makedirs(tm_path, exist_ok=True)

# wb = openpyxl.Workbook()
# excel_file = "test.xlsx"
# path_excel = os.path.join(tm_path, excel_file)
# wb.save(path_excel)