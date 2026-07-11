from openpyxl import load_workbook
import xml.etree.ElementTree
from datetime import datetime
import json
import openpyxl

excel_file = "Oo.xlsx"
new_sheet = "Sheet2"

tree = xml.etree.ElementTree.parse("immigration_report_140258562.XML")
root = tree.getroot()

wb = load_workbook(excel_file)

if new_sheet in wb.sheetnames:
     del wb[new_sheet]
ws2 = wb.create_sheet(title=new_sheet)

with open("ct.json", "r", encoding="utf-8") as file:
     ct_json = json.load(file)

ws2.append(["FN", None, "LN", "GD", "PN", "NT", "BD", "DEP"])

def sw_date_format(_):
    if _ and _.strip() != "":
        try:
            _ = datetime.strptime(_.strip(), "%m/%d/%Y")
            return _.strftime("%d/%m/%Y")
        except ValueError:
            return _

for _ in root.findall(".//G_IMMIGRATION"):
        fn = _.find("FIRST_NAME").text if _.find("FIRST_NAME") is not None else ""
        ln = _.find("LAST_NAME").text if _.find("LAST_NAME") is not None else ""
        gd = _.find("SEX").text if _.find("SEX") is not None else ""
        pn = _.find("PASSPORT").text if _.find("PASSPORT") is not None else ""
        nt = _.find("NATIONALITY").text if _.find("NATIONALITY") is not None else ""
        if nt in ct_json:
             nt_match = ct_json[nt]
        else:
             nt_match = nt
        bd = _.find("DATE_OF_BIRTH").text if _.find("DATE_OF_BIRTH") is not None else ""
        bd_sw = sw_date_format(bd)
        dep = _.find("DEPARTURE_DATE").text if _.find("DEPARTURE_DATE") is not None else ""
        dep_sw = sw_date_format(dep)
        all_data = [fn, None, ln, gd, pn, nt_match, bd_sw, dep_sw]
        ws2.append(all_data)

# ws2 = wb.active
ws1 = wb["Sheet"]
wb.active = ws1

ws1_fn_ln_pn = {}
for _ in ws1.iter_rows(values_only=True, min_row=2):
    ws1_fn = _[1]
    ws1_ln = _[0]    
    ws1_pn = _[4]     
    if ws1_fn and ws1_ln and ws1_pn != "":
        ws1_key = f"{str(ws1_fn).strip()}_{str(ws1_ln).strip()}"
        ws1_fn_ln_pn[ws1_key] = str(ws1_pn).strip()

for _ in range(2, ws2.max_row + 1):
    ws2_fn = ws2.cell(row=_, column=1).value
    ws2_ln = ws2.cell(row=_, column=3).value
    if ws2_fn and ws2_ln != "":
         ws2_key = f"{str(ws2_fn).strip()}_{str(ws2_ln).strip()}"
         if ws2_key in ws1_fn_ln_pn:
              for_empty_passport = ws1_fn_ln_pn[ws2_key]
              ws2.cell(row=_, column=5, value=for_empty_passport)

for _ in range(ws2.max_row, 1 ,-1):
     pn = ws2.cell(row=_, column=5).value
     if pn is None:
          ws2.delete_rows(_, amount=1)

# for _ in ws2.iter_rows(values_only=True):
#      print(_[4])

wb.active = ws2
wb.save(excel_file)