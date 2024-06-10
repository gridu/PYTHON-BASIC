from argparse import ArgumentParser, Namespace
import json
from lxml import etree
from pathlib import Path
from statistics import mean


def define_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', help='specify the directory containing folders for cities, if not specified the current working directory is used')
    parser.add_argument('-o', '--output', help='specify the path and filename of the output file, if not specified the result is written to stdout')
    parser.add_argument('-c', '--country', help='specify the country name, "Spain" by default', default='Spain')
    parser.add_argument('-d', '--date', help='specify the date (format: YYYY-MM-DD), 2021-09-25 by default', default='2021-09-25')
    return parser


def parse_args(namespace: Namespace) -> tuple[Path, Path | None]:
    input_dir = Path.cwd()
    if namespace.input is not None:
        input_dir = Path(namespace.input)
    output_file = None
    if namespace.output is not None:
        output_file = Path(namespace.output)
    return input_dir, output_file


def read_cities_data(cities_dir: Path) -> dict:
    data = {}
    for city_folder in cities_dir.iterdir():
        if not city_folder.is_dir():
            continue
        file_iter = city_folder.iterdir()
        file = next(file_iter) # assume there is just one file
        data[city_folder.name] = json.loads(file.read_text())
    return data


def parse_city(city_raw_dict: dict) -> dict:
    temps = []
    wind_speeds = []
    for hour in city_raw_dict['hourly']:
        temp = float(hour['temp'])
        wind_speed = float(hour['wind_speed'])
        temps.append(temp)
        wind_speeds.append(wind_speed)
    city_parsed_data = {
        'mean_temp': round(mean(temps), 2),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'mean_wind_speed': round(mean(wind_speeds), 2),
        'max_wind_speed': max(wind_speeds),
        'min_wind_speed': min(wind_speeds)
    }
    return city_parsed_data


def parse_cities(cities_raw_dict: dict) -> dict:
    cities_parsed_data = {}
    for city_name, city_dict in cities_raw_dict.items():
        cities_parsed_data[city_name] = parse_city(city_dict)
    return {
        'mean_temp': round(mean([data['mean_temp'] for _, data in cities_parsed_data.items()]), 2),
        'mean_wind_speed': round(mean([data['mean_wind_speed'] for _, data in cities_parsed_data.items()]), 2),
        'coldest_city': min(cities_parsed_data.items(), key=lambda entry: entry[1]['mean_temp'])[0],
        'warmest_city': max(cities_parsed_data.items(), key=lambda entry: entry[1]['mean_temp'])[0],
        'windiest_city': max(cities_parsed_data.items(), key=lambda entry: entry[1]['mean_wind_speed'])[0],
        'cities': cities_parsed_data
    }


def render_xml(country_data: dict) -> str:
    weather = etree.Element(
        'weather',
        country=country_data['country'],
        date=country_data['date']
    )
    etree.SubElement(
        weather,
        'summary',
        mean_temp=str(country_data['mean_temp']),
        mean_wind_speed=str(country_data['mean_wind_speed']),
        coldest_place=country_data['coldest_city'],
        warmest_place=country_data['warmest_city'],
        windiest_place=country_data['windiest_city']
    )
    cities = etree.SubElement(weather, 'cities')
    for city_name, city_data in country_data['cities'].items():
        etree.SubElement(
            cities,
            city_name.replace(' ', '_'),
            mean_temp=str(city_data['mean_temp']),
            mean_wind_speed=str(city_data['mean_wind_speed']),
            min_temp=str(city_data['min_temp']),
            min_wind_speed=str(city_data['min_wind_speed']),
            max_temp=str(city_data['max_temp']),
            max_wind_speed=str(city_data['max_wind_speed'])
        )
    return etree.tostring(weather, pretty_print=True)


def print_output(xml: str, output_path: Path | None) -> None:
    output_file = open(output_path, 'w') if output_path is not None else None
    print(xml, file=output_file, end='')
    if output_file is not None:
        output_file.close()


def main() -> None:
    parser = define_parser()
    namespace = parser.parse_args()
    input_dir, output_file = parse_args(namespace)
    cities_raw_dict = read_cities_data(input_dir)
    country_data = parse_cities(cities_raw_dict)
    country_data['country'] = namespace.country
    country_data['date'] = namespace.date
    xml = render_xml(country_data).decode()
    print_output(xml, output_file)


if __name__ == '__main__':
    main()
