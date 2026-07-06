import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

CURR_DIR = Path(__file__).parent
DATA_DIR = CURR_DIR / "source_data"
RES_FILE = CURR_DIR / "result.xml"


def process_city(data: str) -> str:
    """
    Function to calculate min, mean, max temp and wind for given city JSON data.

    returns JSON obect
    """

    hourly_list = data["hourly"]

    temp_list = []
    wind_list = []

    for entry in hourly_list:
        temp_list.append(entry["temp"])
        wind_list.append(entry["wind_speed"])

    min_temp = min(temp_list)
    max_temp = max(temp_list)
    mean_temp = sum(temp_list) / len(temp_list)

    min_wind = min(wind_list)
    max_wind = max(wind_list)
    mean_wind = sum(wind_list) / len(wind_list)

    result = {
        "min_temp": min_temp,
        "max_temp": max_temp,
        "mean_temp": mean_temp,
        "min_wind": min_wind,
        "max_wind": max_wind,
        "mean_wind": mean_wind,
    }

    return result


def create_xml(
    mean_temp,
    mean_wind_speed,
    coldest_place,
    warmest_place,
    windiest_place,
    cities_data,
    result_path,
):
    root = ET.Element("weather", country="Spain", date="2021-09-25")

    ET.SubElement(
        root,
        "summary",
        mean_temp=str(round(mean_temp, 2)),
        mean_wind_speed=str(round(mean_wind_speed, 2)),
        coldest_place=str(coldest_place),
        warmest_place=str(warmest_place),
        windiest_place=str(windiest_place),
    )

    cities_node = ET.SubElement(root, "cities")

    for city_name, city_data in cities_data:
        ET.SubElement(
            cities_node,
            city_name,
            mean_temp=str(round(city_data["mean_temp"], 2)),
            mean_wind_speed=str(round(city_data["mean_wind"], 2)),
            min_temp=str(round(city_data["min_temp"], 2)),
            min_wind_speed=str(round(city_data["min_wind"], 2)),
            max_temp=str(round(city_data["max_temp"], 2)),
            max_wind_speed=str(round(city_data["max_wind"], 2)),
        )

    tree = ET.ElementTree(root)

    ET.indent(tree, space="  ")
    with open(result_path, "wb") as f:
        tree.write(f, encoding="utf-8")


if __name__ == "__main__":
    cities_data = []

    max_avg_temp = -math.inf
    max_avg_temp_city = ""
    min_avg_temp = math.inf
    min_avg_temp_city = ""
    max_avg_wind = -math.inf
    max_avg_wind_city = ""

    mean_temps = []
    mean_winds = []

    for file in DATA_DIR.iterdir():
        with open(file / "2021_09_25.json") as f:
            city_name = "_".join(file.name.split())
            data = json.load(f)
        city_json = process_city(data)
        if city_json["mean_temp"] > max_avg_temp:
            max_avg_temp = city_json["mean_temp"]
            max_avg_temp_city = city_name
        if city_json["mean_temp"] < min_avg_temp:
            min_avg_temp = city_json["mean_temp"]
            min_avg_temp_city = city_name
        if city_json["mean_wind"] > max_avg_wind:
            max_avg_wind = city_json["mean_wind"]
            max_avg_wind_city = city_name
        mean_temps.append(city_json["mean_temp"])
        mean_winds.append(city_json["mean_wind"])
        cities_data.append((city_name, city_json))

    great_avg_temp = sum(mean_temps) / len(mean_temps)
    great_avg_wind = sum(mean_winds) / len(mean_winds)

    create_xml(
        great_avg_temp,
        great_avg_wind,
        min_avg_temp_city,
        max_avg_temp_city,
        max_avg_wind_city,
        cities_data,
        RES_FILE,
    )
