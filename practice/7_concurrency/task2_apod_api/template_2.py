import concurrent.futures
import os
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json

API_KEY = "snnjwniYYvaFLEdW4arW9WanSQZNAHtagl1LQv0D"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def request_page(url: str) -> BeautifulSoup:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as r:
        page = r.read().decode('utf-8')
    return BeautifulSoup(page, 'html.parser')


def get_images_urls(start_date: str, end_date: str, api_key: str) -> list:
    url = APOD_ENDPOINT + '?api_key=' + api_key + '&start_date=' + start_date + '&end_date=' + end_date
    soup = request_page(url)
    data = json.loads(soup.get_text())
    results = []
    for item in data:
        if item['media_type'] == 'image':
            results.append(item['url'])
    return results


def download_image(url: str, number: int) -> None:
    path = OUTPUT_IMAGES + '/' + str(number) + '.jpg'
    urllib.request.urlretrieve(url, path)


def download_all_images(metadata: list) -> None:
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, os.cpu_count() + 4)) as executor:
        executor.map(download_image, metadata, range(len(metadata)))


def main():
    data = get_images_urls(start_date='2021-08-01', end_date='2021-09-30', api_key=API_KEY)
    download_all_images(data)


if __name__ == '__main__':
    main()
