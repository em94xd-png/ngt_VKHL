import openpyxl
import json

excel_file = "ct.xlsx"

wb = openpyxl.load_workbook(excel_file)
ws1 = wb["Sheet1"]

ct = {}

for _ in ws1.iter_rows(values_only=True, min_row=2):
    ct_full = _[0]
    ct_code = _[1]
    if ct_full and ct_code:
        ct[ct_full] = ct_code

with open ("ct.json", "w", encoding="utf-8") as file:
    json.dump(ct, file, ensure_ascii=False, indent=4)