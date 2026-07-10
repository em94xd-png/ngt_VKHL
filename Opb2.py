import openpyxl

wb = openpyxl.load_workbook("Oo.xlsx")
ws = wb.active
ws2 = wb["Sheet2"]
ws3 = wb["Sheet3"]

ws3.append([])

for _ in ws2.iter_rows(values_only=True, min_row=2):
    c1 = [None] + [_[0]]
    ws3.append(c1)

wb.save("Oo.xlsx")