import pandas as pd
import ast
from collections import defaultdict
import os
import csv
from xml.etree.ElementTree import parse, Element, SubElement, ElementTree
import xml.etree.ElementTree as ET
save_root2 = "stupa_screenshots-20210611T203018Z-001\\annotations"

if not os.path.exists(save_root2):
    os.mkdir(save_root2)


def write_xml(folder, filename, bbox_list):
    root = Element('annotation')
    SubElement(root, 'folder').text = "stupa_screenshots-20210611T203018Z-001"
    SubElement(root, 'filename').text = filename
    SubElement(root, 'path').text = './stupa_screenshots-20210611T203018Z-001/images/' +  filename
    source = SubElement(root, 'source')
    SubElement(source, 'database').text = 'Unknown'


    # Details from first entry
    e_filename,e_xmin, e_ymin, e_width, e_height , e_xmax, e_ymax,e_class_name = bbox_list[0]
    
    size = SubElement(root, 'size')
    SubElement(size, 'width').text = e_width
    SubElement(size, 'height').text = e_height
    SubElement(size, 'depth').text = '3'

    SubElement(root, 'segmented').text = '0'

    for entry in bbox_list:
        e_filename,e_xmin, e_ymin, e_width, e_height , e_xmax, e_ymax,e_class_name = entry
        
        obj = SubElement(root, 'object')
        SubElement(obj, 'name').text = e_class_name
        SubElement(obj, 'pose').text = 'Unspecified'
        SubElement(obj, 'truncated').text = '0'
        SubElement(obj, 'difficult').text = '0'

        bbox = SubElement(obj, 'bndbox')
        SubElement(bbox, 'xmin').text = e_xmin
        SubElement(bbox, 'ymin').text = e_ymin
        SubElement(bbox, 'xmax').text = e_xmax
        SubElement(bbox, 'ymax').text = e_ymax

    #indent(root)
    tree = ElementTree(root)
    
    xml_filename = os.path.join('.', folder, os.path.splitext(filename)[0] + '.xml')
    tree.write(xml_filename)
    

entries_by_filename = defaultdict(list)

with open('annotation-cleaned.csv', 'r', encoding='utf-8') as f_input_csv:
    csv_input = csv.reader(f_input_csv)
    header = next(csv_input)

    for row in csv_input:
        print(row)
        filename, xmin,ymin,width, height, xmax, ymax ,class_name= row
        entries_by_filename[filename].append([filename, xmin,ymin,width, height, xmax, ymax ,class_name])


print(entries_by_filename)
for filename, entries in entries_by_filename.items():
    print(filename, len(entries))
    write_xml(save_root2, filename, entries)





