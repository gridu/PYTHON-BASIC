from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

API_KEY = "snnjwniYYvaFLEdW4arW9WanSQZNAHtagl1LQv0D"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'


def request_page(url: str) -> BeautifulSoup:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as r:
        page = r.read().decode('utf-8')
    return BeautifulSoup(page, 'html.parser')


if __name__ == '__main__':
    start_date, end_date = '2020-07-06', '2020-08-06'
    api_key = API_KEY
    url = APOD_ENDPOINT + '?api_key=' + api_key + '&start_date=' + start_date + '&end_date=' + end_date
    soup = request_page(url)
    soup.get_text()
