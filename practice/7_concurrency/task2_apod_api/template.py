import requests
import json
from os import path
import os
import threading
import concurrent.futures


API_KEY = "API_KEY"  # GET YOUR OWN API KEY
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'

thread_local = threading.local()


def get_session() -> requests.Session:
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    response = requests.get(APOD_ENDPOINT, params={'start_date': start_date,
                                                   'end_date': end_date,
                                                   'api_key': api_key})
    metadata = json.loads(response.text)
    return metadata


def download_apod_images(metadata: list) -> None:
    if not os.path.exists(OUTPUT_IMAGES):
        os.mkdir(OUTPUT_IMAGES)
    images_urls = [item['url'] for item in metadata
                   if item['media_type'] != 'video']
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, images_urls)


def download_image(url: str) -> None:
    filename = url.split('/')[-1]
    filepath = path.join(OUTPUT_IMAGES, filename)
    s = get_session()
    with s.get(url, stream=True) as response:
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response:
                    f.write(chunk)


def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()
