import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet["A1"] = "LN"
sheet["B1"] = "FN"
sheet["C1"] = "BD"
sheet["D1"] = "CT"
sheet["E1"] = "PN"

wb.save("Oo.xlsx")