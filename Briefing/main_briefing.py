from openpyxl import *
import os, xml.etree.ElementTree, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import script_config

current_path = os.path.dirname(os.path.abspath(__file__))

excel_file = "Briefing.xlsx"
path_excel = os.path.join(current_path, excel_file)

wb = load_workbook(path_excel)

ws = "Ori Format"
ws = wb[ws]

history_forecast = "history_forecast_142784233.XML"
path_history_forecast = os.path.join(current_path, history_forecast)

tree = xml.etree.ElementTree.parse(path_history_forecast)
root = tree.getroot()

for _ in root.findall(".//G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE"):
    hu = _.find("HOUSE_USE_ROOMS").text if _.find("HOUSE_USE_ROOMS").text is not None else "N/A"
    oc = round(float(_.find("CF_OCCUPANCY").text), 2) if _.find("CF_OCCUPANCY").text is not None else "N/A"
    arr = _.find("ARRIVAL_ROOMS").text if _.find("ARRIVAL_ROOMS").text is not None else "-"
    dep = _.find("DEPARTURE_ROOMS").text if _.find("DEPARTURE_ROOMS").text is not None else "-"
    ppl = _.find("NO_PERSONS").text if _.find("NO_PERSONS").text is not None else "-"
    if _.find("CONSIDERED_DATE").text == "24-JUL-26":
        ws["E5"] = arr
        ws["E7"] = dep
        ws["F12"] = ppl
    if _.find("CONSIDERED_DATE").text == "25-JUL-26":
        ws["M5"] = arr
        ws["M7"] = dep
    if _.find("CONSIDERED_DATE").text == "26-JUL-26":
        ws["O5"] = arr
        ws["O7"] = dep
    if _.find("CONSIDERED_DATE").text == "27-JUL-26":
        ws["Q5"] = arr
        ws["Q7"] = dep
    if _.find("CONSIDERED_DATE").text == "28-JUL-26":
        ws["S5"] = arr
        ws["S7"] = dep
    if _.find("CONSIDERED_DATE").text == "29-JUL-26":
        ws["U5"] = arr
        ws["U7"] = dep

history_forecast_AVC = "history_forecast_142784728.XML"
path_history_forecast_AVC = os.path.join(current_path, history_forecast_AVC)

tree = xml.etree.ElementTree.parse(path_history_forecast_AVC)
root = tree.getroot()

for _ in root.findall(".//G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE"):
    cmp = int(_.find("COMPLIMENTARY_ROOMS").text) if _.find("COMPLIMENTARY_ROOMS").text is not None else "N/A"
    hu = int(_.find("HOUSE_USE_ROOMS").text) if _.find("HOUSE_USE_ROOMS").text is not None else "N/A"
    if hu == "0":
        hu = "N/A"
    ns = _.find("NO_SHOW_ROOMS").text if _.find("NO_SHOW_ROOMS").text is not None else "N/A"
    if ns == "0":
        ns = "N/A"
    adr = round(float(_.find("CF_AVERAGE_ROOM_RATE").text), 2) if _.find("CF_AVERAGE_ROOM_RATE").text is not None else "N/A"
    arr = _.find("ARRIVAL_ROOMS").text if _.find("ARRIVAL_ROOMS").text is not None else "-"
    dep = _.find("DEPARTURE_ROOMS").text if _.find("DEPARTURE_ROOMS").text is not None else "-"
    rm = _.find("NO_ROOMS").text if _.find("NO_ROOMS").text is not None else "-"
    ppl = _.find("NO_PERSONS").text if _.find("NO_PERSONS").text is not None else "-"
    if _.find("CONSIDERED_DATE").text == "23-JUL-26":
        ws["B5"] = cmp
        ws["B7"] = hu
        ws["B9"] = ns
        ws["B11"] = adr
        ws["B11"].number_format = "#,###.##"
        ws["B12"] = oc
        ws["B12"].number_format = "#.##\"%\""
    if _.find("CONSIDERED_DATE").text == "24-JUL-26":
        ws["D4"] = script_config.td_hp_dd_mm
        ws["F5"] = arr
        ws["F7"] = dep
        ws["E9"] = rm
        ws["G12"] = ppl
    if _.find("CONSIDERED_DATE").text == "25-JUL-26":
        ws["N5"] = arr
        ws["N7"] = dep
        ws["M9"] = rm
        ws["M11"] = oc
        ws["M11"].number_format = "#.##\"%\""
        ws["M12"] = ppl
    if _.find("CONSIDERED_DATE").text == "26-JUL-26":
        ws["P5"] = arr
        ws["P7"] = dep
        ws["O9"] = rm
        ws["O11"] = oc
        ws["O11"].number_format = "#.##\"%\""
        ws["O12"] = ppl
    if _.find("CONSIDERED_DATE").text == "27-JUL-26":
        ws["R5"] = arr
        ws["R7"] = dep
        ws["Q9"] = rm
        ws["Q11"] = oc
        ws["Q11"].number_format = "#.##\"%\""
        ws["Q12"] = ppl
    if _.find("CONSIDERED_DATE").text == "28-JUL-26":
        ws["T5"] = arr
        ws["T7"] = dep
        ws["S9"] = rm
        ws["S11"] = oc
        ws["S11"].number_format = "#.##\"%\""
        ws["S12"] = ppl
    if _.find("CONSIDERED_DATE").text == "29-JUL-26":
        ws["V5"] = arr
        ws["V7"] = dep
        ws["U9"] = rm
        ws["U11"] = oc
        ws["U11"].number_format = "#.##\"%\""
        ws["U12"] = ppl

split_adult_child = "resfutureoccupancy_142784766.XML"
path_split_adult_child = os.path.join(current_path, split_adult_child)

tree = xml.etree.ElementTree.parse(path_split_adult_child)
root = tree.getroot()

for _ in root.findall(".//G_RESV_TYPE"):
    adl = _.find("SUMADULTS").text if _.find("SUMADULTS").text is not None else "-"
    chd = _.find("SUMCHILDREN").text if _.find("SUMCHILDREN").text is not None else "-"
    if _.find(".//D_DATE").text == "24-JUL-26":
        ws["E12"] = adl
        ws["E13"] = chd

room_upgrade = "finjrnlbytrans_142785205.XML"
path_room_upgrade = os.path.join(current_path, room_upgrade)

tree = xml.etree.ElementTree.parse(path_room_upgrade)
root = tree.getroot()

for _ in root:
    if _.tag == "R_DEBIT":
        val = float(_.text)
        if _.text == "0":
            ws["I5"] = "-"
        else:
            if val.is_integer():
                ws["I5"] = int(val)
                ws["I5"].number_format = "#,##0"
            else:
                ws["I5"] = round(val, 2)
                ws["I5"].number_format = "#,##0.00"

late_checkout = "finjrnlbytrans_142784328.XML"
path_late_checkout = os.path.join(current_path, late_checkout)

tree = xml.etree.ElementTree.parse(path_late_checkout)
root = tree.getroot()

for _ in root:
    if _.tag == "R_DEBIT":
        val = float(_.text)
        if _.text == "0":
            ws["I7"] = "-"
        else:
            if val.is_integer():
                ws["I7"] = int(val)
                ws["I7"].number_format = "#,##0"
            else:
                ws["I7"] = round(val, 2)
                ws["I7"].number_format = "#,##0.00"

tour_commission = "finjrnlbytrans_142785024.XML"
path_tour_commission = os.path.join(current_path, tour_commission)

tree = xml.etree.ElementTree.parse(path_tour_commission)
root = tree.getroot()

for _ in root:
    if _.tag == "R_DEBIT":
        val = float(_.text)
        if _.text == "0":
            ws["I9"] = "-"
        else:
            if val.is_integer():
                ws["I9"] = int(val)
                ws["I9"].number_format = "#,##0"
            else:
                ws["I9"] = round(val, 2)
                ws["I9"].number_format = "#,##0.00"

gift_shop = "finjrnlbytrans_142784366.XML"
path_gift_shop = os.path.join(current_path, gift_shop)

tree = xml.etree.ElementTree.parse(path_gift_shop)
root = tree.getroot()

for _ in root:
    if _.tag == "R_DEBIT":
        val = float(_.text)
        if _.text == "0":
            ws["I12"] = "-"
        else:
            if val.is_integer():
                ws["I12"] = int(val)
                ws["I12"].number_format = "#,##0"
            else:
                ws["I12"] = round(val, 2)
                ws["I12"].number_format = "#,##0.00"

ws["E6"] = "=F5-E5"
ws["E8"] = "=F7-E7"
for _ in ["E6", "E8"]:
    if ws[_] == "0":
        ws[_] = "-"

ws["M6"] = "=N5-M5"
ws["M8"] = "=N7-M7"
ws["O6"] = "=P5-O5"
ws["O8"] = "=P7-O7"
ws["Q6"] = "=R5-Q5"
ws["Q8"] = "=R7-Q7"
ws["S6"] = "=T5-S5"
ws["S8"] = "=T7-S7"
ws["U6"] = "=V5-U5"
ws["U8"] = "=V7-U7"
for _ in ["M6", "M8", "O6", "O8", "Q6", "Q8", "S6", "S8", "U6", "U8"]:
    if ws[_] == "0":
        ws[_] = "-"

cmp = ws["B5"].value
hu = ws["B7"].value
rm = ws["E9"].value

ws["E11"] = int(rm - (cmp - hu) / 327 * 100)
ws["E11"].number_format = "#.##\"%\""

ws["F12"] = "=E12+E13"

wb.save(path_excel)