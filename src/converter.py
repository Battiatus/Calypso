import json
import pandas as pd
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view

def evtx_to_json(evtx_path, output_path):
    records = []
    with open(evtx_path, 'r') as evtx_file:
        for xml, record in evtx_file_xml_view(FileHeader(evtx_file, 0x0)):
            records.append(xml)
    with open(output_path, 'w') as json_file:
        json.dump(records, json_file)

def evtx_to_csv(evtx_path, output_path):
    # Cette fonction nécessite une adaptation pour parser le XML et créer un DataFrame
    pass

def evtx_to_xml(evtx_path, output_path):
    with open(evtx_path, 'r') as evtx_file, open(output_path, 'w') as xml_file:
        xml_file.write("<Events>")
        for xml, record in evtx_file_xml_view(FileHeader(evtx_file, 0x0)):
            xml_file.write(xml)
        xml_file.write("</Events>")
