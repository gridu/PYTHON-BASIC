import time
import datetime
import requests
import os
import concurrent.futures
import multiprocessing


API_KEY = "JCJEgrmz1zGyZPnOw5p19Xv4hfm7gy9aNVdkPabP"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def get_single_day_response(date: datetime):

    url = "https://api.nasa.gov/planetary/apod?api_key=" + API_KEY + \
          "&date=" + datetime.datetime.strftime(date, "%Y-%m-%d")
    return requests.get(url).content.decode()[2:-3]


def get_apod_metadata(start_date: str, end_date: str, api_key: str, multiprocess=False) -> list:

    if multiprocess:

        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        dates = []

        while start_date <= end_date:
            dates.append(start_date)
            start_date += datetime.timedelta(days=1)

        st = time.time()

        with multiprocessing.Pool() as pool:
            str_response = pool.map(get_single_day_response, dates)

        end = time.time()
        print("Time it took to get responses one date by one:", end-st)

        return str_response

    else:

        st = time.time()

        url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key + \
              "&start_date=" + start_date + "&end_date=" + end_date
        str_response = requests.get(url).content.decode()

        end = time.time()
        print("Time it took to get response with all dates at once:", end-st)

        # cutting out the [{ and }]
        list_response = str_response[2:-3].split("},{")

        return list_response


def download_img_write_file(day: dict):
    if day['media_type'] == "image":
        img = requests.get(day['url']).content
        img_name = day['url'].split("/")[-1]
        file = open(OUTPUT_IMAGES + "/" + img_name, 'wb')
        file.write(img)


def download_apod_images(metadata: list):

    for i in range(len(metadata)):
        keys_values = metadata[i].split("\",\"")

        metadata[i] = {}

        for key_val in keys_values:
            key, val = key_val.split("\":\"")
            if key[0] == "\"":
                key = key[1:]
            if val[-1] == "\"":
                val = val[:-1]

            metadata[i][str(key)] = str(val)

    days_with_images = [day for day in metadata if day["media_type"] == "image"]

    st = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(download_img_write_file, days_with_images)
    end = time.time()
    print("Time it took to download:", end-st)


def main():
    metadata = get_apod_metadata(
        start_date='2021-09-20',
        end_date='2021-09-30',
        api_key=API_KEY, #multiprocess=True
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    for i in range(3):
        if not os.path.exists(OUTPUT_IMAGES):
            os.makedirs(OUTPUT_IMAGES)
        for file in os.listdir(OUTPUT_IMAGES):
            os.remove(os.path.join(OUTPUT_IMAGES, file))
        st = time.time()
        main()
        end = time.time()
        print("All the time needed for the program:", end - st)
        print()
