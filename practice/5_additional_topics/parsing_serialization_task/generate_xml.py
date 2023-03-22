from lxml import etree
from statistics import mean
from os import walk
import os
import pandas as pd

root = etree.Element("weather", attrib={"country": "Spain", "date": "2021-09-25"})
summary_attrs = ["mean_temp", "mean_wind_speed", "coldest_place", "warmest_place", "windiest_place"]
summary = etree.SubElement(root, "summary", attrib=dict.fromkeys(summary_attrs, ""))
cities = etree.SubElement(root, "cities")

source_data_path = '/Users/tiasalmon/Documents/Python_Basics/python_basic/practice/5_additional_topics/parsing_serialization_task/source_data'

f = []
d = []
for (dirpath, dirnames, filenames) in walk(source_data_path):
    f.extend(filenames)
    d.extend(dirnames)

city_attrs = ["mean_temp", "mean_wind_speed", "min_temp", "min_wind_speed", "max_temp", "max_wind_speed"]

for dir in d:
    new_tag = etree.SubElement(cities, dir.replace(" ", "-"), attrib=dict.fromkeys(city_attrs, ""))
    with open(os.path.join(*[source_data_path, dir, '2021_09_25.json'])) as user_file:
        df = pd.read_json(os.path.join(*[source_data_path, dir, '2021_09_25.json']))
        file_contents = user_file.read()
        # print(file_contents)
  
print(etree.tostring(root, pretty_print=True).decode())
