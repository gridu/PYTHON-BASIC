# Weather data processing

## Overview
In this task, you will process real hourly weather data collected 
by [OpenWeather API](https://openweathermap.org/history) in multiple JSON files. 
The goal is to build one XML file with the weather summary from [our dataset](./source_data). 

For this task we have collected historical data for each of Spain's autonomous communities capitals (17 cities). 
One day of weather observations for each location is described by one JSON file. 
In this task we have only one observation day - September 25, 2021. 

For this task, you should write a script that will build the XML file which describes the weather in Spain 
for September 25, 2021 with set of parameters: mean, minimum, maximum temperature and mean, minimum, maximum wind speed. 
Besides, you need to find the warmest, the coldest and the windiest city in Spain for that date 
and include them in the XML file.

## [Dataset](./source_data)

Our dataset has a simple structure. 
There are 17 folders with names of Spain’s cities. 
Each folder contains one JSON file with hourly weather data for September 25, 2021. 

Each JSON file has the same structure. 
You can find full information about existing fields [here](https://openweathermap.org/history#parameter).

- General:
    - Field **hourly**: a list of dictionaries with weather data for each hour.
    - Field **temp** in dictionary of hour weather data: temperature. 
    - Field **wind_speed** in dictionary of hour weather data: wind speed.

## Steps

1. Parse hourly data from JSON files for each city. Don’t forget to remember names of cities.
2. Calculate mean, maximum, minimum temperature and wind speed for each city. 
3. Calculate mean temperature and wind speed  for the whole country by using produced data before. Find the coldest, the warmest and the windiest cities in Spain (you must use mean values from step 2 to do that).
4. Create an XML file with a specific structure and write calculated values in it.

## Output XML file structure

- Root element **weather**
  - attribute **country**: country name
  - attribute **date**: date of observation (ex. “2021-09-25”).
  

  - Child element **summary** (parent: **weather**)
    - attribute **mean_temp**: country’s mean temperature
    - attribute **mean_wind_speed**: country’s mean wind speed
    - attribute **coldest_place**: name of the city with the lowest mean temperature value
    - attribute **warmest_place**: name of the city with the highest mean temperature value
    - attribute **windiest_place**: name of the city with the highest mean wind speed value
    

  - Child element **cities** (parent: **weather**)
    - collection of child elements with city name as tag (parent: **cities**):
      - attribute **mean_temp**: city’s mean temperature
      - attribute **max_temp**: city’s max temperature
      - attribute **min_temp**: city’s min temperature
      - attribute **mean_wind_speed**: city’s mean wind speed
      - attribute **max_wind_speed**: city’s max wind speed
      - attribute **min_wind_speed**: city’s min wind speed

All decimal values must be rounded to 2 decimal places.

### Output XML example

[example](./tests/example_result.xml)

### Validation
You could use [check_result function](./tests/validate_xml.py) to validate your output XML. 
Also, you could use the dataset with example data to compare your result with our XML example.
