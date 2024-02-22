
import json
import csv
from Evtx.Evtx import FileHeader
from Evtx.Views import evtx_file_xml_view
import xml.etree.ElementTree as ET

def evtx_to_json(evtx_path, output_path):
    records = []
    # Lire le contenu du fichier EVTX en mémoire
    with open(evtx_path, 'rb') as evtx_file:
        evtx_data = evtx_file.read()
    # Utiliser les données binaires directement
    for xml, _ in evtx_file_xml_view(FileHeader(evtx_data, 0x0)):
        try:
            records.append(ET.tostring(ET.fromstring(xml), encoding='unicode'))
        except ET.ParseError:
            continue
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(records, json_file, ensure_ascii=False, indent=4)

def evtx_to_csv(evtx_path, output_path):
    records = []
    with open(evtx_path, 'rb') as evtx_file:  # Ouvrir le fichier en mode binaire
        for xml, _ in evtx_file_xml_view(FileHeader(evtx_file.read(), 0x0)):  # Lire le contenu du fichier en tant qu'objet bytes
            try:
                records.append(ET.tostring(ET.fromstring(xml), encoding='unicode'))
            except ET.ParseError:
                continue
    with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Event'])
        for record in records:
            writer.writerow([record])
            
            
def evtx_to_xml(evtx_path, output_path):
    with open(evtx_path, 'rb') as evtx_file:  # Ouvrir le fichier en mode binaire
        evtx_data = evtx_file.read()  # Lire le contenu du fichier en tant qu'objet bytes
    with open(output_path, 'w') as xml_file:
        xml_file.write("<Events>")
        for xml, _ in evtx_file_xml_view(FileHeader(evtx_data, 0x0)):  # Utiliser les données binaires directement
            xml_file.write(xml)
        xml_file.write("</Events>")
