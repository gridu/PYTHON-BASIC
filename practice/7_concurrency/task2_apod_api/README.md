## Task 2. Collect NASA’s astronomical pictures of the day via API

[![241-lorand-fenyes-bubble-m52.jpg](https://i.postimg.cc/1Xt6NBRF/241-lorand-fenyes-bubble-m52.jpg)](https://postimg.cc/34sWsgvr)

NASA provides a long list of public services and some of them have its own public API. 
One of the most popular websites at NASA is 
the [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html). 
In fact, this website is one of the most popular websites across all US federal agencies. 
You can access imagery and associated metadata from this website via API.

In this task, you will write a script for bulk imagery download. 
Firstly, you need to get your API key for NASA APIs.
It can be done easily here: https://api.nasa.gov/

After getting the API key, you can find the **APOD** API description at this page. 
To access data you need to know the endpoint and query parameters.

Examples:

1. Get metadata for date 2020-07-06:

   
    https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY&date=2020-07-06

2. Get metadata for dates between 2020-07-06 and 2020-08-06:

   
    https://api.nasa.gov/planetary/apod?api_key=YOUR_KEY&start_date=2020-07-06&end_date=2020-08-06

Your script must take **start_date** (2021-08-01), **end_date** (2021-09-30) parameters 
and download all images for this time period to one folder. 
Some dates have videos instead of images. 
You can miss these dates by checking the media_type key in the API response.

Use your knowledge about parallelism/concurrency in Python to speed up images downloading 
and do not forget about the API limitation - 1,000 requests per hour.
