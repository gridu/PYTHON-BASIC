import json
import os
from lxml import etree

def analyse_city_data(path):
    with open(path, "r") as file:
        data = json.load(file)
    return {
        'mean_temp': round(sum(hour["temp"] for hour in data['hourly']) / len(data['hourly']), 2),
        'mean_wind_speed': round(sum(hour["wind_speed"] for hour in data['hourly']) / len(data['hourly']), 2),
        'min_temp': min((hour["temp"] for hour in data['hourly'])),
        'min_wind_speed': min((hour["wind_speed"] for hour in data['hourly'])),
        'max_temp': max((hour["temp"] for hour in data['hourly'])),
        'max_wind_speed': max((hour["wind_speed"] for hour in data['hourly']))
    }

def analyse_country_data(input_path, output_path, date, country_name):
    inner_folder_names = []
    for root, dirs, files in os.walk(input_path):
        for directory in dirs:
            inner_folder_names.append(directory)
    inner_folder_names.sort()
    cities = {}
    for folder_name in inner_folder_names:
        cities[folder_name] = analyse_city_data(input_path + '/' + folder_name + '/' + date.replace('-', '_') + '.json')
    summary = {
        'mean_temp' : round(sum(city['mean_temp'] for city in cities.values()) / len(cities), 2),
        'mean_wind_speed' : round(sum(city['mean_wind_speed'] for city in cities.values()) / len(cities), 2),
        'coldest_place' : min(cities, key=lambda city: cities[city]['mean_temp']),
        'warmest_place' : max(cities, key=lambda city: cities[city]['mean_temp']),
        'windiest_place' : max(cities, key=lambda city: cities[city]['mean_wind_speed'])
    }
    root = etree.Element('weather')
    root.set('country', country_name)
    root.set('date', date)
    summary_child = etree.SubElement(root, 'summary')
    cities_child = etree.SubElement(root, 'cities')
    for key, value in summary.items():
        summary_child.set(key, str(value))
    for city, city_data in cities.items():
        city_child = etree.SubElement(cities_child, city.replace(' ', '_'))
        for key, value in city_data.items():
            city_child.set(key, str(value))
    etree.ElementTree(root).write(output_path, pretty_print=True, encoding="UTF-8")



analyse_country_data('source_data', 'output.xml', '2021-09-25', 'Spain')

