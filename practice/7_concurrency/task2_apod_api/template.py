from argparse import ArgumentParser, Namespace
from concurrent.futures import ThreadPoolExecutor
import datetime
import json
import os
import requests
import sys


API_KEY = "YOUR_KEY"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument('-k', '--api-key', help='your API key, scipt default used if not specified', default=API_KEY)
    parser.add_argument('-s', '--start-date', help='start of the time period (format: YYYY-MM-DD), today if not specified')
    parser.add_argument('-e', '--end-date', help='end of the time period (format: YYYY-MM-DD), today if not specified')
    return parser


def parse_arguments(parser: ArgumentParser) -> Namespace:
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.start_date is None:
        namespace.start_date = datetime.datetime.today().strftime('%Y-%m-%d')
    if namespace.end_date is None:
        namespace.end_date = datetime.datetime.today().strftime('%Y-%m-%d')
    return namespace


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list[dict]:
    args = {
        'api_key': api_key,
        'start_date': start_date,
        'end_date': end_date
    }
    url = APOD_ENDPOINT + '?' + '&'.join([f'{k}={v}' for k, v in args.items()])
    response = requests.get(url)
    return json.loads(response.content.decode())


def download_image(url: str, filename: str) -> None:
    response = requests.get(url)
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)
    with open(f'{OUTPUT_IMAGES}/{filename}', 'wb') as file:
        file.write(response.content)


def download_apod_images(metadata: list) -> None:
    images_metadata = [m for m in metadata if m['media_type'] == 'image']
    filenames = [
        f'{entry['title']} ({entry['date']}).{entry['url'].split('.')[-1]}'
        for entry in images_metadata
    ]
    urls = [entry['url'] for entry in images_metadata]
    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls, filenames)


def main():
    parser = create_parser()
    namespace = parse_arguments(parser)
    metadata = get_apod_metadata(
        start_date=namespace.start_date,
        end_date=namespace.end_date,
        api_key=namespace.api_key,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()
