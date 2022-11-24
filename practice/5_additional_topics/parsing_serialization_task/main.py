import json
import statistics
from lxml import etree


def json_reader(path: str) -> list:
    with open(path, 'r') as read_file:
        data_hourly = json.load(read_file)
    return data_hourly['hourly']


def load_required_data(lst: list) -> dict:
    data = {'temp': [], 'wind_speed': []}
    for element in lst:
        data['temp'].append(element['temp'])
        data['wind_speed'].append(element['wind_speed'])
    final_data = {'temp': {'min': min(data['temp']), 'max': max(data['temp']),
                           'avg': round(statistics.mean(data['temp']), 2)}, 'wind_speed':
                      {'min': min(data['wind_speed']), 'max': max(data['wind_speed']),
                       'avg': round(statistics.mean(data['wind_speed']), 2)}}
    return final_data


def read_all() -> dict:
    cities = ['Barcelona', 'Logrono', 'Madrid', 'Merida', 'Murcia', 'Oviedo', 'Palma', 'Pamplona',
              'Santa Cruz de Tenerife', 'Santander', 'Santiago de Compostela', 'Seville', 'Toledo', 'Valencia',
              'Valladolid', 'Vitoria-Gasteiz', 'Zaragoza']
    data = {}
    for city in cities:
        data[city] = load_required_data(json_reader('source_data/' + city + '/2021_09_25.json'))
    return data


def mean_temp_all_country(data: dict) -> float:
    return round(statistics.mean([d['temp']['avg'] for d in data.values()]), 2)


def mean_wind_spead(data: dict) -> float:
    return round(statistics.mean([d['wind_speed']['avg'] for d in data.values()]), 2)


def min_max_temp_all_country(data: dict) -> tuple:
    sort = sorted(data.items(), key=lambda item: item[1]['temp']['avg'])
    return sort[0], sort[-1]


def max_wind_all_country(data: dict) -> iter:
    sort = sorted(data.items(), key=lambda item: item[1]['wind_speed']['avg'])
    return sort[-1]


if __name__ == '__main__':
    cities = ['Barcelona', 'Logrono', 'Madrid', 'Merida', 'Murcia', 'Oviedo', 'Palma', 'Pamplona',
              'Santa Cruz de Tenerife', 'Santander', 'Santiago de Compostela', 'Seville', 'Toledo', 'Valencia',
              'Valladolid', 'Vitoria-Gasteiz', 'Zaragoza']
    data = read_all()
    root = etree.Element('weather', country='Spain', date='2021-09-25')
    child1 = etree.SubElement(root, 'summary', mean_temp=str(mean_temp_all_country(data)),
                              mean_wind_speed=str(mean_wind_spead(data)),
                              coldest_place=str(min_max_temp_all_country(data)[0][0]),
                              warmest_place=str(min_max_temp_all_country(data)[1][0]),
                              windiest_place=str(max_wind_all_country(data)[0]))
    child2 = etree.SubElement(root, 'cities')
    for city in cities:
        if city == 'Santa Cruz de Tenerife':
            child2.append(
                etree.Element('Santa_Cruz_de_Tenerife', mean_temp=str(data[city]['temp']['avg']), max_temp=str(data[city]['temp']['max']),
                              min_temp=str(data[city]['temp']['min']),
                              mean_wind_speed=str(data[city]['wind_speed']['avg']),
                              max_wind_speed=str(data[city]['wind_speed']['max']),
                              min_wind_speed=str(data[city]['wind_speed']['min'])))
        elif city == 'Santiago de Compostela':
            child2.append(
                etree.Element('Santiago_de_Compostela', mean_temp=str(data[city]['temp']['avg']),
                              max_temp=str(data[city]['temp']['max']),
                              min_temp=str(data[city]['temp']['min']),
                              mean_wind_speed=str(data[city]['wind_speed']['avg']),
                              max_wind_speed=str(data[city]['wind_speed']['max']),
                              min_wind_speed=str(data[city]['wind_speed']['min'])))
        else:
            child2.append(
                etree.Element(city, mean_temp=str(data[city]['temp']['avg']), max_temp=str(data[city]['temp']['max']),
                              min_temp=str(data[city]['temp']['min']),
                              mean_wind_speed=str(data[city]['wind_speed']['avg']),
                              max_wind_speed=str(data[city]['wind_speed']['max']),
                              min_wind_speed=str(data[city]['wind_speed']['min'])))
    tree = etree.ElementTree(root)
    with open('results.xml', 'wb') as f:
        tree.write(f)