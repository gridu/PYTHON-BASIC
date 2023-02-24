import json
import os
import xml.etree.ElementTree as ET

BASEPATH = os.getcwd()
SOURCE_DATA = BASEPATH + "/source_data"


class WeatherParser:

    def __init__(self):
        self.country_dict = None
        self.date = None
        self.city_values = None
        self.all_cities_values = None

    @staticmethod
    def open_json(file_path: str) -> dict:
        """Opens .json file from filepath and returns a dictionary """

        with open(file_path) as f:
            data = json.load(f)
            return data

    def go_through_cities(self) -> list[dict]:
        """Opens directory for every city and calls methods for value extraction"""

        self.all_cities_values = []
        for city_name in os.listdir(SOURCE_DATA):
            c = os.path.join(SOURCE_DATA, city_name)
            for file in os.listdir(c):
                file_path = os.path.join(c, file)
                data = self.open_json(file_path)
                city_data = self.fill_dict(city_name.replace(" ", "_"), data)
                self.all_cities_values.append(city_data)

        self.date = file.replace('_', '-').split(".")[0]
        return self.all_cities_values

    @staticmethod
    def fill_dict(city_name: str, data: dict) -> dict:
        """Calculates weather values for a city and returns them as a dictionary"""

        temp = [hour['temp'] for hour in data['hourly']]
        wind = [hour['wind_speed'] for hour in data['hourly']]
        city_values = {"city_name": city_name,
                       "mean_temp": round(sum(temp) / len(temp), 2),
                       "max_temp": max(temp),
                       "min_temp": min(temp),
                       "mean_wind_speed": round(sum(wind) / len(wind), 2),
                       "min_wind_speed": min(wind),
                       "max_wind_speed": max(wind)
                       }
        return city_values

    def get_extreme_value(self, key: str, is_max=True) -> str:
        """Gets max or min value of a key from a list of dictionaries"""

        extreme_val = max(self.all_cities_values, key=lambda d: d[key]) if is_max else \
            min(self.all_cities_values, key=lambda d: d[key])
        return extreme_val['city_name']

    def find_places(self) -> tuple[tuple[str, str], ...]:
        """Finds cities that have extreme values for specified keys"""

        warmest_place = ("warmest_place", self.get_extreme_value('mean_temp'))
        coldest_place = ("coldest_place", self.get_extreme_value('mean_temp', is_max=False))
        windiest_place = ("windiest_place", self.get_extreme_value('mean_wind_speed'))
        return warmest_place, coldest_place, windiest_place

    def spain_mean(self) -> tuple[tuple[str, float], ...]:
        """Gets mean values for temperature and wind speed from all cities"""

        num_cities = len(self.all_cities_values)
        spain_mean_temp = (
            "mean_temp",
            round((sum([city['mean_temp'] for city in self.all_cities_values])/num_cities), 2))
        spain_mean_wind = (
            "mean_wind_speed",
            round((sum([city['mean_wind_speed'] for city in self.all_cities_values])/num_cities), 2))
        return spain_mean_temp, spain_mean_wind

    def country_values(self) -> dict:
        """Returns country weather summary as a dictionary"""

        country_dict = dict(self.find_places() + self.spain_mean())
        return country_dict

    def create_xml(self) -> None:
        root = ET.Element("weather", country="Spain", date=self.date)
        summary = ET.SubElement(root, "summary")
        for val in self.country_values():
            summary.set(val, str(self.country_values()[val]))

        cities = ET.SubElement(root, "cities")
        for city in self.all_cities_values:
            city_summary = ET.SubElement(cities, city["city_name"])
            for key in city:
                if key != list(city.keys())[0]:
                    city_summary.set(key, str(city[key]))
        tree = ET.ElementTree(root)
        tree.write('weather.xml')


if __name__ == "__main__":
    parser = WeatherParser()
    parser.go_through_cities()
    parser.country_values()
    parser.create_xml()
