import os
from datetime import datetime
import json

from lxml import etree


def fun(date: datetime.date):
    scores = []
    date = date.strftime("%Y_%m_%d")
    for city in os.listdir("source_data"):
        file = open("source_data/" + str(city) + '/' + str(date) + ".json")

        scores.append({"city": str(city), "mean_temp": 0., "mean_wind_speed": 0.})
        dic = json.load(file)
        hours = dic['hourly']

        for hour in hours:
            scores[-1]['mean_temp'] += float(hour['temp'])

            if "min_temp" in scores[-1].keys():
                if float(scores[-1]['min_temp']) > float(hour['temp']):
                    scores[-1]['min_temp'] = float(hour['temp'])
            else:
                scores[-1]['min_temp'] = float(hour['temp'])

            if "max_temp" in scores[-1].keys():
                if float(scores[-1]['max_temp']) < float(hour['temp']):
                    scores[-1]['max_temp'] = float(hour['temp'])
            else:
                scores[-1]['max_temp'] = float(hour['temp'])

            scores[-1]['mean_wind_speed'] += float(hour['wind_speed'])

            if "min_wind_speed" in scores[-1].keys():
                if float(scores[-1]['min_wind_speed']) > float(hour['wind_speed']):
                    scores[-1]['min_wind_speed'] = float(hour['wind_speed'])
            else:
                scores[-1]['min_wind_speed'] = float(hour['wind_speed'])

            if "max_wind_speed" in scores[len(scores) - 1].keys():
                if float(scores[-1]['max_wind_speed']) < float(hour['wind_speed']):
                    scores[-1]['max_wind_speed'] = float(hour['wind_speed'])
            else:
                scores[-1]['max_wind_speed'] = float(hour['wind_speed'])

        scores[-1]['mean_temp'] /= len(hours)
        scores[-1]['mean_wind_speed'] /= len(hours)

    scores.append({"mean_temp": 0., "mean_wind_speed": 0.,
                   "coldest_place": None, "coldest_place_temp": None,
                   "warmest_place": None, "warmest_place_temp": None,
                   "windiest_place": None, "windiest_place_wind_speed": None})
    for city_data in scores[0:-1]:
        scores[-1]['mean_temp'] += city_data['mean_temp']
        scores[-1]['mean_wind_speed'] += city_data['mean_wind_speed']
        if city_data == scores[0]:
            scores[-1]['coldest_place_temp'] = city_data['mean_temp']
            scores[-1]['coldest_place'] = city_data['city']
            scores[-1]['warmest_place_temp'] = city_data['mean_temp']
            scores[-1]['warmest_place'] = city_data['city']
            scores[-1]['windiest_place_wind_speed'] = city_data['mean_wind_speed']
            scores[-1]['windiest_place'] = city_data['city']
        else:
            if city_data['mean_temp'] < scores[-1]['coldest_place_temp']:
                scores[-1]['coldest_place_temp'] = city_data['mean_temp']
                scores[-1]['coldest_place'] = city_data['city']
            if city_data['mean_temp'] > scores[-1]['warmest_place_temp']:
                scores[-1]['warmest_place_temp'] = city_data['mean_temp']
                scores[-1]['warmest_place'] = city_data['city']
            if city_data['mean_wind_speed'] > scores[-1]['windiest_place_wind_speed']:
                scores[-1]['windiest_place_wind_speed'] = city_data['mean_wind_speed']
                scores[-1]['windiest_place'] = city_data['city']

    num_of_cities = len(scores) - 1
    scores[-1]['mean_temp'] /= num_of_cities
    scores[-1]['mean_wind_speed'] /= num_of_cities

    final_score = scores[-1]

    weather = etree.Element("weather", country="Spain", date=date.replace("_", "-"))

    summary = etree.SubElement(weather, "summary",
                               attrib={"mean_temp": str(round(final_score['mean_temp'], 2)),
                                       "mean_wind_speed": str(round(final_score['mean_wind_speed'], 2)),
                                       "coldest_place": str(final_score['coldest_place']),
                                       "warmest_place": str(final_score['warmest_place']),
                                       "windiest_place": str(final_score['windiest_place'])}
                               )

    cities = etree.SubElement(weather, "cities")
    for city in os.listdir("source_data"):
        city_tag = etree.SubElement(cities, str(city).replace(" ", "_"))
        city_score = {}
        for score in scores:
            if score["city"] == str(city):
                city_score = score
                break
        city_tag.set("mean_temp", str(round(city_score["mean_temp"], 2)))
        city_tag.set("mean_wind_speed", str(round(city_score["mean_wind_speed"], 2)))
        city_tag.set("min_temp", str(round(city_score["min_temp"], 2)))
        city_tag.set("min_wind_speed", str(round(city_score["min_wind_speed"], 2)))
        city_tag.set("max_temp", str(round(city_score["max_temp"], 2)))
        city_tag.set("max_wind_speed", str(round(city_score["max_wind_speed"], 2)))

    file = open("Spain_weather_" + date + ".xml", 'w')
    file.write(etree.tostring(weather, pretty_print=True).decode())


fun(datetime.strptime("2021-09-25", "%Y-%m-%d"))
