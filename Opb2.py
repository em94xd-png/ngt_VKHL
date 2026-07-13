import openpyxl
import json

excel_file = "rr_ct_code.xlsm"

wb = openpyxl.load_workbook(excel_file, data_only=True)
ws1 = wb["Sheet1"]

json_data = {}
for _ in ws1.iter_rows(values_only=True):
    ct = _[0]
    code = _[1]
    json_data[ct] = code

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

# wb.save(excel_file)
