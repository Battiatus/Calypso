# src/converter.py

import json
import pandas as pd
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
import xml.etree.ElementTree as ET

def evtx_to_json(evtx_path, output_path):
    records = []
    with open(evtx_path, 'rb') as evtx_file:
        for xml, _ in evtx_file_xml_view(FileHeader(evtx_file, 0x0)):
            try:
                records.append(ET.fromstring(xml))
            except ET.ParseError:
                continue
    with open(output_path, 'w') as json_file:
        json.dump([ET.tostring(record, encoding='unicode') for record in records], json_file)

def evtx_to_csv(evtx_path, output_path):
    records = []
    with open(evtx_path, 'rb') as evtx_file:
        for xml, _ in evtx_file_xml_view(FileHeader(evtx_file, 0x0)):
            try:
                records.append(ET.fromstring(xml))
            except ET.ParseError:
                continue
    df = pd.DataFrame([{'Event': ET.tostring(record, encoding='unicode')} for record in records])
    df.to_csv(output_path, index=False)

def evtx_to_xml(evtx_path, output_path):
    with open(evtx_path, 'rb') as evtx_file, open(output_path, 'w') as xml_file:
        xml_file.write("<Events>")
        for xml, _ in evtx_file_xml_view(FileHeader(evtx_file, 0x0)):
            xml_file.write(xml)
        xml_file.write("</Events>")
