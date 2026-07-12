import openpyxl

excel_file = "get_data.xlsx"
ws2 = "Sheet2"

wb = openpyxl.load_workbook(excel_file)
ws2 = wb[ws2]
for _ in range(ws2.max_row, 0, -1):
    ws2.delete_rows(_, amount=1)

wb.save(excel_file)

# print(ws2)