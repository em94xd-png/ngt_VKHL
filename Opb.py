from openpyxl import load_workbook
import xml.etree.ElementTree

excel_file = "Oo.xlsx"
new_sheet = "Sheet2"

tree = xml.etree.ElementTree.parse("immigration_report_140258562.XML")
root = tree.getroot()

wb = load_workbook(excel_file)
ws = wb.create_sheet(title=new_sheet)

ws.append(["FN", None, "LN", "GD", "PN", "NT", "BD", "DEP"])

for _ in root.findall(".//G_IMMIGRATION"):
        fn = _.find("FIRST_NAME").text if _.find("FIRST_NAME") is not None else ""
        ln = _.find("LAST_NAME").text if _.find("LAST_NAME") is not None else ""
        gd = _.find("SEX").text if _.find("SEX") is not None else ""
        pn = _.find("PASSPORT").text if _.find("PASSPORT") is not None else ""
        nt = _.find("NATIONALITY").text if _.find("NATIONALITY") is not None else ""
        bd = _.find("DATE_OF_BIRTH").text if _.find("DATE_OF_BIRTH") is not None else ""
        dep = _.find("DEPARTURE_DATE").text if _.find("DEPARTURE_DATE") is not None else ""
        all_data = [fn, None, ln, gd, pn, nt, bd, dep]
        ws.append(all_data)

wb.save(excel_file)