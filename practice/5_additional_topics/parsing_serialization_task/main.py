import json
import statistics
from lxml import etree
import os
from typing import Dict, List


def read_json_data(path: str) -> Dict[str, any]:
    with open(path, 'r') as read_file:
        return json.load(read_file)


def compute_city_statistics(city_data: dict) -> dict:
    temp = []
    wind_speed = []

    for date, daily_data in city_data.items():
        for element in daily_data:
            temp.append(element['temp'])
            wind_speed.append(element['wind_speed'])
    return {
        'temp': {
            'min': min(temp),
            'max': max(temp),
            'avg': round(statistics.mean(temp), 2)
        },
        'wind_speed': {
            'min': min(wind_speed),
            'max': max(wind_speed),
            'avg': round(statistics.mean(wind_speed), 2)
        }
    }


def read_all(path: str) -> dict:
    data = {}
    for city_name in os.listdir(path):
        city_data = dict()
        city_data_path = os.path.join(path, city_name)
        for data_json in os.listdir(city_data_path):
            date, _ = os.path.splitext(data_json)
            data_json_path = os.path.join(city_data_path, data_json)
            city_hourly_data = read_json_data(data_json_path)['hourly']
            city_data[date] = city_hourly_data
        data[city_name] = city_data
    return data


def rounded_mean(l: List[float]) -> float:
    return round(statistics.mean(l), 2)


def compute_summary(data: dict) -> dict:
    avg_temps = [d['temp']['avg'] for d in data.values()]
    avg_wind = [d['wind_speed']['avg'] for d in data.values()]
    coldest_place, _ = min(data.items(), key=lambda item: item[1]['temp']['avg'])
    warmest_place, _ = max(data.items(), key=lambda item: item[1]['temp']['avg'])
    windiest_place, _ = max(data.items(), key=lambda item: item[1]['wind_speed']['avg'])
    return dict(
        mean_temp=str(rounded_mean(avg_temps)),
        mean_wind_speed=str(rounded_mean(avg_wind)),
        coldest_place=coldest_place,
        warmest_place=warmest_place,
        windiest_place=windiest_place
    )


def preprocess_city_name(city_name: str) -> str:
    return city_name.replace(' ', '_')


def write_xml(path, summary, data) -> None:
    root = etree.Element('weather', country='Spain', date='2021-09-25')
    etree.SubElement(root, 'summary', **summary)
    city_element = etree.SubElement(root, 'cities')
    for city, city_statistics in sorted(data.items()):
        city_element.append(
            etree.Element(
                preprocess_city_name(city),
                mean_temp=str(city_statistics['temp']['avg']),
                max_temp=str(city_statistics['temp']['max']),
                min_temp=str(city_statistics['temp']['min']),
                mean_wind_speed=str(city_statistics['wind_speed']['avg']),
                max_wind_speed=str(city_statistics['wind_speed']['max']),
                min_wind_speed=str(city_statistics['wind_speed']['min'])))
    tree = etree.ElementTree(root)
    with open(path, 'wb') as f:
        tree.write(f)


def main():
    data = read_all('source_data')
    results = dict()
    for city_name, city_data in data.items():
        results[city_name] = compute_city_statistics(city_data)
    summary = compute_summary(results)
    write_xml('results_to.xml', summary, results)


if __name__ == '__main__':
    main()
