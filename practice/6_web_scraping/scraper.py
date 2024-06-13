from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import diskcache
import json
import requests


USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'
MAX_WORKERS = 64
CACHE_DIR = './.scraper_cache/'
CACHE = diskcache.Cache(directory=CACHE_DIR)
CACHE_TTL = 1 * 60 * 60 # 1 hour


def cached(func):
    def wrapper(*args, **kwargs):
        inputs = {'args': args, 'kwargs': kwargs}
        key = json.dumps(inputs)
        if key not in CACHE:
            CACHE.set(key, func(*args, **kwargs), expire=CACHE_TTL)
        return CACHE[key]
    
    return wrapper


@cached
def request(url: str) -> bytes:
    page = requests.get(url, headers={'User-Agent': USER_AGENT})
    return page.content


def get_main_table() -> list[dict]:
    content = request('https://finance.yahoo.com/most-active')
    soup = BeautifulSoup(content, 'html.parser')
    rows_data = []
    trs = soup.find('table', class_='W(100%)').find('tbody').find_all('tr')
    for tr in trs:
        row_data = {}
        tds = tr.find_all('td')
        for td in tds:
            field_name = td.get('aria-label')
            row_data[field_name] = td.get_text()
        rows_data.append(row_data)
    return rows_data


def get_ceo(symbol: str) -> dict:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/profile/')
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('div', class_='table-container').find('table')
    ths = table.find('thead').find('tr').find_all('th')
    column_names = [th.get_text() for th in ths]
    trs = table.find('tbody').find_all('tr')
    rows_data = []
    for tr in trs:
        tds = tr.find_all('td')
        row_data = {}
        for index, td in enumerate(tds):
            row_data[column_names[index]] = td.get_text()
        rows_data.append(row_data)
    ceos = list(filter(lambda row: 'CEO' in row['Title'], rows_data))
    return ceos[0]


def get_country(symbol: str) -> str:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/profile/')
    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find('div', class_='address').find_all('div')[-1]
    country = div.get_text()
    return country


def get_employees(symbol: str) -> int:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/profile/')
    soup = BeautifulSoup(content, 'html.parser')
    strong = soup.find('dl', class_='company-stats').find('strong')
    if strong is None:
        return 0
    employees = int(strong.get_text().replace(',', ''))
    return employees


def get_sheet1_data() -> list[list[str]]:
    rows = []
    data = get_main_table()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        def fn(company: dict) -> None:
            symbol = company['Symbol']
            ceo = get_ceo(symbol)
            row = [
                company['Name'],
                symbol,
                get_country(symbol),
                str(get_employees(symbol)),
                ceo['Name'],
                ceo['Year Born']
            ]
            rows.append(row)
        executor.map(fn, data)
    return rows


def get_52_week_change(symbol: str) -> str:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/key-statistics/')
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find('h3', text='Trading Information').find_parent().find_next_sibling().find('tbody').find_all('tr')[1].find_all('td')[1].get_text()


def get_total_cash(symbol: str) -> str:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/key-statistics/')
    soup = BeautifulSoup(content, 'html.parser')
    return soup.find(text='Balance Sheet').find_parent().find_parent().find_parent().find_next_sibling().find('tbody').find_all('tr')[0].find_all('td')[1].get_text()


def get_sheet2_data() -> list[list[str]]:
    rows = []
    data = get_main_table()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        def fn(company: dict) -> None:
            symbol = company['Symbol']
            change = get_52_week_change(symbol)
            total_cash = get_total_cash(symbol)
            row = [
                company['Name'],
                symbol,
                change,
                total_cash
            ]
            rows.append(row)
        executor.map(fn, data)
    return rows


def get_top_institutional_holders_table(symbol: str) -> list[dict]:
    content = request(f'https://finance.yahoo.com/quote/{symbol}/holders/')
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('h3', string='Top Institutional Holders').find_parent().find_next_sibling().find('table')
    ths = table.find('thead').find('tr').find_all('th')
    column_names = [th.get_text() for th in ths]
    trs = table.find('tbody').find_all('tr')
    holders = []
    for tr in trs:
        tds = tr.find_all('td')
        row_data = {}
        for index, td in enumerate(tds):
            row_data[column_names[index]] = td.get_text().strip()
        holders.append(row_data)
    return holders


def get_sheet3_data() -> list[list[str]]:
    rows = []
    data = get_main_table()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        def fn(company: dict) -> None:
            symbol = company['Symbol']
            holders = get_top_institutional_holders_table(symbol)
            holder = [h for h in holders if h['Holder'] == 'Blackrock Inc.'][0]
            row = [
                company['Name'],
                symbol,
                holder['Shares'],
                holder['Date Reported'],
                holder['% Out'],
                holder['Value']
            ]
            rows.append(row)
        executor.map(fn, data)
    return rows
