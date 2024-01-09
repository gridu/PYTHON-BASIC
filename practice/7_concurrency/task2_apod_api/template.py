import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta

API_KEY = 'YOUR_API_KEY'  # Replace with your NASA API key
BASE_URL = 'https://api.nasa.gov/planetary/apod'

def download_image(date):
    params = {'api_key': API_KEY, 'date': date}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        media_type = data.get('media_type')
        if media_type == 'image':
            image_url = data.get('url')
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                save_image(data['date'], image_response.content)
            else:
                print(f"Failed to download image for date {date}")
        else:
            print(f"No image available for date {date}")

def save_image(date, content):
    folder_path = 'apod_images'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f'{date}.jpg')
    with open(file_path, 'wb') as file:
        file.write(content)
    print(f"Image saved for date {date}")

def get_date_range(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    date_generated = [start + timedelta(days=x) for x in range((end - start).days + 1)]
    return [date.strftime('%Y-%m-%d') for date in date_generated]

def main():
    start_date = '2021-08-01'
    end_date = '2021-09-30'

    dates = get_date_range(start_date, end_date)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_image, date) for date in dates]

        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
