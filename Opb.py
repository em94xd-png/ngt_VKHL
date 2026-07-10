from openpyxl import load_workbook
import xml.etree.ElementTree

excel_file = "Oo.xlsx"
new_sheet = "Sheet2"

tree = xml.etree.ElementTree.parse("immigration_report_140258562.XML")
root = tree.getroot()

wb = load_workbook(excel_file)
ws = wb.create_sheet(title=new_sheet)

ws.append(["FN", "LN", "GD", "NT", "PN", "BD", "ARR", "DEP"])

for _ in root.findall(".//G_IMMIGRATION"):
    row_data = [
        _.find("FIRST_NAME").text 
        if _.find("FIRST_NAME") is not None else "",
        _.find("LAST_NAME").text 
        if _.find("LAST_NAME") is not None else "",
        _.find("SEX").text 
        if _.find("SEX") is not None else "",
        _.find("NATIONALITY").text 
        if _.find("NATIONALITY") is not None else "",
        _.find("PASSPORT").text 
        if _.find("PASSPORT") is not None else "",
        _.find("DATE_OF_BIRTH").text 
        if _.find("DATE_OF_BIRTH") is not None else "",
        _.find("ARRIVAL_DATE").text 
        if _.find("ARRIVAL_DATE") is not None else "",
        _.find("DEPARTURE_DATE").text 
        if _.find("DEPARTURE_DATE") is not None else ""
    ]
    ws.append(row_data)

wb.save(excel_file)