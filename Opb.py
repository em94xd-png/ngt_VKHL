from openpyxl import load_workbook
import xml.etree.ElementTree
from datetime import datetime
import json

excel_file = "get_data.xlsx"
create_sheet = "Sheet3"

tree = xml.etree.ElementTree.parse("immigration_report_140258562.XML")
root = tree.getroot()

wb = load_workbook(excel_file)

if create_sheet in wb.sheetnames:
     del wb[create_sheet]

ws3 = wb.create_sheet(title=create_sheet)
# ws3 = wb.active

with open("ct.json", "r", encoding="utf-8") as file:
     ct_json = json.load(file)

ws3.append(["FN", None, "LN", "GD", "PN", "NT", "BD", "DEP"])

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
        bd = _.find("DATE_OF_BIRTH").text if _.find("DATE_OF_BIRTH") is not None else ""
        bd_sw = sw_date_format(bd)
        dep = _.find("DEPARTURE_DATE").text if _.find("DEPARTURE_DATE") is not None else ""
        dep_sw = sw_date_format(dep)
        all_data = [fn, None, ln, gd, pn, nt, bd_sw, dep_sw]
        ws3.append(all_data)

ws2 = wb["Sheet2"]
# wb["Sheet2"] = wb.active

ws2_fn_ln_pn = {}
ws2_fn_ln_ct = {}
for _ in ws2.iter_rows(values_only=True, min_row=2):
    ws2_fn = _[1]
    ws2_ln = _[0]    
    ws2_pn = _[4]     
    ws2_ct = _[3]
    if ws2_fn and ws2_ln and ws2_pn != "":
        ws2_key = f"{str(ws2_fn).strip()}_{str(ws2_ln).strip()}"
        ws2_fn_ln_pn[ws2_key] = str(ws2_pn).strip()
        ws2_fn_ln_ct[ws2_key] = str(ws2_ct).strip()

for _ in range(2, ws3.max_row + 1):
    ws3_fn = ws3.cell(row=_, column=1).value
    ws3_ln = ws3.cell(row=_, column=3).value
    ws3_pn = ws3.cell(row=_, column=5).value
    ws3_nt = ws3.cell(row=_, column=6).value
    if ws3_fn and ws3_ln != "":
          ws3_key = f"{str(ws3_fn).strip()}_{str(ws3_ln).strip()}"
          if ws3_key in ws2_fn_ln_pn:
               for_empty_passport = ws2_fn_ln_pn[ws3_key]
               if ws3_pn is None or str(ws3_pn).strip() == "":
                    ws3.cell(row=_, column=5, value=for_empty_passport)
    if ws3_nt == "Thailand":
          ws3_key = f"{str(ws2_fn).strip()}_{str(ws2_ln).strip()}"
          if ws3_key in ws2_fn_ln_ct:
               for_THA_passport = ws2_fn_ln_ct[ws3_key]  
               ws3.cell(row=_, column=6, value=for_THA_passport)

for _ in range(ws3.max_row, 1, -1):
     nt = ws3.cell(row=_, column=6).value
     if nt in ct_json:
          nt_match = ct_json[nt]
          ws3.cell(row=_, column=6, value=nt_match)

for _ in range(ws3.max_row, 1 ,-1):
     pn = ws3.cell(row=_, column=5).value
     if pn is None or pn == "":
          ws3.delete_rows(_, amount=1)

duplicated_pn = set()
for _ in range(ws3.max_row, 1, -1):
    pn = ws3.cell(row=_, column=5).value
    if pn in duplicated_pn:
          ws3.delete_rows(_, amount=1)
    else:
         duplicated_pn.add(pn)
         
for _ in wb.worksheets:
     _.views.sheetView[0].tabSelected = False
         
wb.active = wb["Sheet"]
wb.save(excel_file)