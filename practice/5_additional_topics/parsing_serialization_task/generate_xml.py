from lxml import etree
from os import walk
import os
import pandas as pd
import json

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
summary_mean_temp = summary_mean_wind_speed = summary_max_temp = summary_max_wind = 0
summary_min_temp  = 9999999
summary_coldest_place = summary_warmest_place = summary_windiest_place = ""
    
for dir in d:
    file = os.path.join(*[source_data_path, dir, '2021_09_25.json'])
    with open(file, "r", encoding="utf-8") as user_file:
        contents = user_file.read()
    new_tag = etree.SubElement(cities, dir.replace(" ", "-"), attrib=dict.fromkeys(city_attrs, ""))
    data = json.loads(contents)
    hourly_data = data['hourly']
    hourly_df = pd.DataFrame(hourly_data)
    mean_temp = round(hourly_df['temp'].mean(), 2)
    mean_wind_speed = round(hourly_df['wind_speed'].mean(), 2)
    min_temp = round(hourly_df['temp'].min(), 2)
    max_temp = round(hourly_df['temp'].max(), 2)
    max_wind_speed = round(hourly_df['wind_speed'].max(), 2)
    min_wind_speed = round(hourly_df['wind_speed'].min(), 2)
    new_tag.attrib['mean_temp'] = str(mean_temp)
    new_tag.attrib['mean_wind_speed'] = str(mean_wind_speed)
    new_tag.attrib['min_temp'] = str(min_temp)
    new_tag.attrib['min_wind_speed'] = str(min_wind_speed)
    new_tag.attrib['max_temp'] = str(max_temp)
    new_tag.attrib['max_wind_speed'] = str(max_wind_speed)

    summary_mean_temp += mean_temp
    summary_mean_wind_speed += mean_wind_speed

    if min_temp < summary_min_temp:
        summary_min_temp = min_temp 
        summary_coldest_place = dir

    if max_temp > summary_max_temp:
        summary_max_temp = max_temp 
        summary_warmest_place = dir

    if max_wind_speed > summary_max_wind:
        summary_max_wind = max_wind_speed 
        summary_windiest_place = dir

summary_mean_temp = round(summary_mean_temp/len(d), 2)
summary.attrib['mean_temp'] = str(summary_mean_temp)
summary_mean_wind_speed = round(summary_mean_wind_speed/len(d), 2)
summary.attrib['mean_wind_speed'] = str(summary_mean_wind_speed)
summary.attrib['coldest_place'] = summary_coldest_place
summary.attrib['warmest_place'] = summary_warmest_place
summary.attrib['windiest_place'] = summary_windiest_place

et = etree.ElementTree(root)
et.write('spain-cities.xml', pretty_print=True)