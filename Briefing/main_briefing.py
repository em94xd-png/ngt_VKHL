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

history_forecast = "history_forecast_142244492.XML"
path_history_forecast = os.path.join(current_path, history_forecast)

tree = xml.etree.ElementTree.parse(path_history_forecast)
root = tree.getroot()

for _ in root.findall(".//G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE"):
    cmp = _.find("COMPLIMENTARY_ROOMS").text if _.find("COMPLIMENTARY_ROOMS").text is not None else "N/A"
    hu = _.find("HOUSE_USE_ROOMS").text if _.find("HOUSE_USE_ROOMS").text is not None else "N/A"
    ns = _.find("NO_SHOW_ROOMS").text if _.find("NO_SHOW_ROOMS").text is not None else "N/A"
    adr = round(float(_.find("CF_AVERAGE_ROOM_RATE").text), 2) if _.find("CF_AVERAGE_ROOM_RATE").text is not None else "N/A"
    oc = round(float(_.find("CF_OCCUPANCY").text), 2) if _.find("CF_OCCUPANCY").text is not None else "N/A"
    arr = _.find("ARRIVAL_ROOMS").text if _.find("ARRIVAL_ROOMS").text is not None else "-"
    dep = _.find("DEPARTURE_ROOMS").text if _.find("DEPARTURE_ROOMS").text is not None else "-"
    rm = _.find("NO_ROOMS").text if _.find("NO_ROOMS").text is not None else "-"
    ppl = _.find("NO_PERSONS").text if _.find("NO_PERSONS").text is not None else "-"
    if _.find("CONSIDERED_DATE").text == "21-JUL-26":
        ws["E5"] = arr
        ws["E7"] = dep
        ws["F12"] = ppl
    if _.find("CONSIDERED_DATE").text == "22-JUL-26":
        ws["M5"] = arr
        ws["M7"] = dep
    if _.find("CONSIDERED_DATE").text == "23-JUL-26":
        ws["O5"] = arr
        ws["O7"] = dep
    if _.find("CONSIDERED_DATE").text == "24-JUL-26":
        ws["Q5"] = arr
        ws["Q7"] = dep
    if _.find("CONSIDERED_DATE").text == "25-JUL-26":
        ws["S5"] = arr
        ws["S7"] = dep
    if _.find("CONSIDERED_DATE").text == "26-JUL-26":
        ws["U5"] = arr
        ws["U7"] = dep

history_forecast_AVC = "history_forecast_142243840.XML"
path_history_forecast_AVC = os.path.join(current_path, history_forecast_AVC)

tree = xml.etree.ElementTree.parse(path_history_forecast_AVC)
root = tree.getroot()

for _ in root.findall(".//G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE"):
    cmp = _.find("COMPLIMENTARY_ROOMS").text if _.find("COMPLIMENTARY_ROOMS").text is not None else "N/A"
    hu = _.find("HOUSE_USE_ROOMS").text if _.find("HOUSE_USE_ROOMS").text is not None else "N/A"
    ns = _.find("NO_SHOW_ROOMS").text if _.find("NO_SHOW_ROOMS").text is not None else "N/A"
    adr = round(float(_.find("CF_AVERAGE_ROOM_RATE").text), 2) if _.find("CF_AVERAGE_ROOM_RATE").text is not None else "N/A"
    oc = round(float(_.find("CF_OCCUPANCY").text), 2) if _.find("CF_OCCUPANCY").text is not None else "N/A"
    arr = _.find("ARRIVAL_ROOMS").text if _.find("ARRIVAL_ROOMS").text is not None else "-"
    dep = _.find("DEPARTURE_ROOMS").text if _.find("DEPARTURE_ROOMS").text is not None else "-"
    rm = _.find("NO_ROOMS").text if _.find("NO_ROOMS").text is not None else "-"
    ppl = _.find("NO_PERSONS").text if _.find("NO_PERSONS").text is not None else "-"
    if _.find("CONSIDERED_DATE").text == "20-JUL-26":
        ws["B5"] = cmp
        ws["B7"] = hu
        ws["B9"] = ns
        ws["B11"] = adr
        ws["B11"].number_format = "#,###.##"
        ws["B12"] = oc
        ws["B12"].number_format = "#.##\"%\""
    if _.find("CONSIDERED_DATE").text == "21-JUL-26":
        ws["D4"] = script_config.td_hp_dd_mm
        ws["F5"] = arr
        ws["F7"] = dep
        ws["E9"] = rm
        ws["E11"] = oc
        ws["E11"].number_format = "#.##\"%\""
        ws["G12"] = ppl
    if _.find("CONSIDERED_DATE").text == "22-JUL-26":
        ws["N5"] = arr
        ws["N7"] = dep
        ws["M9"] = rm
        ws["M11"] = oc
        ws["M11"].number_format = "#.##\"%\""
        ws["M12"] = ppl
    if _.find("CONSIDERED_DATE").text == "23-JUL-26":
        ws["P5"] = arr
        ws["P7"] = dep
        ws["O9"] = rm
        ws["O11"] = oc
        ws["O11"].number_format = "#.##\"%\""
        ws["O12"] = ppl
    if _.find("CONSIDERED_DATE").text == "24-JUL-26":
        ws["R5"] = arr
        ws["R7"] = dep
        ws["Q9"] = rm
        ws["Q11"] = oc
        ws["Q11"].number_format = "#.##\"%\""
        ws["Q12"] = ppl
    if _.find("CONSIDERED_DATE").text == "25-JUL-26":
        ws["T5"] = arr
        ws["T7"] = dep
        ws["S9"] = rm
        ws["S11"] = oc
        ws["S11"].number_format = "#.##\"%\""
        ws["S12"] = ppl
    if _.find("CONSIDERED_DATE").text == "26-JUL-26":
        ws["V5"] = arr
        ws["V7"] = dep
        ws["U9"] = rm
        ws["U11"] = oc
        ws["U11"].number_format = "#.##\"%\""
        ws["U12"] = ppl

wb.save(path_excel)