import os
import queue
import threading
import urllib.request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from queue import Queue
import json

API_KEY = "snnjwniYYvaFLEdW4arW9WanSQZNAHtagl1LQv0D"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def request_page(url: str) -> BeautifulSoup:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as r:
        page = r.read().decode('utf-8')
    return BeautifulSoup(page, 'html.parser')


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> Queue:
    task_queue = Queue()
    url = APOD_ENDPOINT + '?api_key=' + api_key + '&start_date=' + start_date + '&end_date=' + end_date
    soup = request_page(url)
    data = json.loads(soup.get_text())
    for item in data:
        if item['media_type'] == 'image':
            task_queue.put(item['url'])
    return task_queue


def download_apod_images(task_queue: Queue, output_dir='./output') -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def worker():
        counter = 0
        while True:
            try:
                url = task_queue.get(block=False)
            except queue.Empty:
                return
            urllib.request.urlretrieve(url, output_dir + '/' + str(counter) + '.jpg')
            counter += 1
            task_queue.task_done()

    threads = [threading.Thread(target=worker) for _ in range(min(os.cpu_count() + 4, 32))]
    [t.start() for t in threads]
    task_queue.join()


def main():
    tasks = get_apod_metadata(start_date='2021-08-01', end_date='2021-09-30', api_key=API_KEY)
    download_apod_images(tasks)


if __name__ == '__main__':
    main()
