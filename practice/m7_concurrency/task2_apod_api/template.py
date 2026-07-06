import json
import os
from pathlib import Path
from queue import Empty, Queue
from threading import Thread

import keyring
import requests

# API_KEY = "YOUR_KEY" # quite funny
APOD_ENDPOINT = "https://api.nasa.gov/planetary/apod"
CURR_DIR = Path(__file__).parent
OUTPUT_DIR = CURR_DIR / "output"
NUM_WORKERS = 11


def get_apod_metadata_one_day(date: str, api_key: str):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

    response = requests.get(url=url)

    return [response]


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> list:
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}"

    response = requests.get(url=url)

    if response.status_code != 200:
        raise Exception(
            f"Connection error while calling API. Staus code: {response.status_code}"
        )

    response = json.loads(response.content)
    return response


def worker_downloader(task_q: Queue):
    while True:
        try:
            meta = task_q.get(block=False)
        except Empty:
            return
        date = meta["date"]
        if meta["media_type"] != "image":
            print(f"There is no photo for {date}. Skipping")
            task_q.task_done()
            continue
        image_url = meta["url"]

        r = requests.get(image_url)
        if r.status_code == 200:
            with open(OUTPUT_DIR / f"{date}.jpg", "wb") as f:
                f.write(r.content)
        else:
            print(
                f"Problem with downloading photo for {date}. Status code: {r.status_code}"
            )
        task_q.task_done()


def download_apod_images(metadata: list):
    tasks_q = Queue()
    for meta in metadata:
        tasks_q.put(meta)

    threads = [
        Thread(target=worker_downloader, args=(tasks_q,)) for _ in range(NUM_WORKERS)
    ]

    [t.start() for t in threads]

    tasks_q.join()


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    api_key = keyring.get_password("nasa_concurrent_task", "NASA_API_KEY")

    # metadata = get_apod_metadata_one_day(date="2021-08-01", api_key=api_key)

    # download_apod_images(metadata)

    metadata = get_apod_metadata(
        start_date="2021-08-01",
        end_date="2021-09-30",
        api_key=api_key,
    )
    download_apod_images(metadata=metadata)


if __name__ == "__main__":
    main()
