from openpyxl import *
import os, xml.etree.ElementTree, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import script_config

current_path = os.path.dirname(os.path.abspath(__file__))

excel_file = "Briefing.xlsx"
path_to_excel = os.path.join(current_path, excel_file)

wb = load_workbook(path_to_excel)

ws = "Ori Format"
ws = wb[ws]

xml_file = "history_forecast_142243840.XML"
path_to_xml = os.path.join(current_path, xml_file)

tree = xml.etree.ElementTree.parse(path_to_xml)
root = tree.getroot()

for _ in root.findall(".//G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE"):
    ytd_cmp = _.find("COMPLIMENTARY_ROOMS").text if _.find("COMPLIMENTARY_ROOMS").text is not None else "N/A"
    ytd_hu = _.find("HOUSE_USE_ROOMS").text if _.find("HOUSE_USE_ROOMS").text is not None else "N/A"
    ytd_ns = _.find("NO_SHOW_ROOMS").text if _.find("NO_SHOW_ROOMS").text is not None else "N/A"
    ytd_adr = round(float(_.find("CF_AVERAGE_ROOM_RATE").text), 2) if _.find("CF_AVERAGE_ROOM_RATE").text is not None else "N/A"
    ytd_oc = round(float(_.find("CF_OCCUPANCY").text), 2) if _.find("CF_OCCUPANCY").text is not None else "N/A"
    if _.find("CONSIDERED_DATE").text == script_config.ytd_hp_dd_mm_yy.upper():
        ws["B5"] = ytd_cmp
        ws["B7"] = ytd_hu
        ws["B9"] = ytd_ns
        ws["B11"] = ytd_adr
        ws["B11"].number_format = "#,###.##"
        ws["B12"] = ytd_oc
        ws["B12"].number_format = "#.##\"%\""

wb.save(path_to_excel)