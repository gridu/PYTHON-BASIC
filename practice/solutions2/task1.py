"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
import os
import queue
import sys
import time
from queue import Queue
from threading import Thread
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import csv
from typing import List, Tuple, Union, Any, Type
import pandas
from pandas import DataFrame


def get_urls_about_companies(soup: BeautifulSoup) -> list:
    results = soup.find(id='scr-res-table')
    company = results.find_all('a')
    return ['https://finance.yahoo.com' + element['href'] for element in company]


def get_specific_urls_about_companies(soup: BeautifulSoup, specification: str) -> str:
    results = soup.find(id='quote-nav')
    profiles = results.find_all('a')
    return \
        ['https://finance.yahoo.com' + profile['href'] for profile in profiles if specification in profile['href']][0]


def request_page(url: str) -> BeautifulSoup:
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read().decode('utf-8')
    return BeautifulSoup(page, 'html.parser')


def get_company_name_and_code(soup: BeautifulSoup) -> tuple:
    lst = soup.get_text().rstrip(')').split('(')
    return lst[0], lst[1]


def get_data_from_profile(soup: BeautifulSoup) -> tuple:
    company_name, company_code = get_company_name_and_code(soup.find('h1', 'D(ib) Fz(18px)'))
    company_location = str(soup.find('p', 'D(ib) W(47.727%) Pend(40px)')).split('<br/>')[2]
    current = soup.find('p', 'D(ib) Va(t)')
    lst = current.find_all('span', 'Fw(600)')
    employees = lst[2].get_text()
    current = soup.find('tbody')
    ceo_info = current.select_one(':nth-child(1)')
    ceo_name = ceo_info.select_one(':nth-child(1)').get_text()
    ceo_born = ceo_info.select_one(':nth-child(5)').get_text()
    return company_name, company_code, company_location, employees, ceo_name, ceo_born


def get_data_from_statistics(soup: BeautifulSoup) -> tuple:
    company_name, company_code = get_company_name_and_code(soup.find('h1', 'D(ib) Fz(18px)'))
    current = soup.find('div', 'Fl(end) W(50%) smartphone_W(100%)').find_all('div', 'Pos(r) Mt(10px)')[0]
    week_change = current.find('tbody').find_all('td', "Fw(500) Ta(end) Pstart(10px) Miw(60px)")[1].get_text()
    current = soup.find('div', 'Fl(start) W(50%) smartphone_W(100%)').find_all('div', 'Pos(r) Mt(10px)')[-2]
    total_cash = current.find('tbody').find_all('td', 'Fw(500) Ta(end) Pstart(10px) Miw(60px)')[0].get_text()
    return company_name, company_code, week_change, total_cash


def get_data_from_holders(soup: BeautifulSoup) -> tuple:
    def find_blackrock(lst):
        for element in lst:
            if 'Blackrock' in str(element):
                return element
        return None

    company_name, company_code = get_company_name_and_code(soup.find('h1', 'D(ib) Fz(18px)'))
    try:
        current = soup.find('table', 'W(100%) BdB Bdc($seperatorColor)').find('tbody').find_all('tr')
    except AttributeError:
        return company_name, company_code, '-', '-', '-', '-'
    try:
        shares, date_reported, out, value = find_blackrock(current).find_all('td', 'Ta(end) Pstart(10px)')
    except AttributeError:
        return company_name, company_code, '-', '-', '-', '-'
    return company_name, company_code, shares.get_text(), date_reported.get_text(), out.get_text(), value.get_text()


def create_queue(company_urls: list) -> Queue:
    q = Queue()
    for company_url in company_urls:
        q.put(company_url)
    return q


def get_required_data_from_page(company_urls: List[str]) -> Tuple[List[Tuple], List[Tuple], List[Tuple]]:
    profile, statistics, holders = [], [], []
    task_queue = create_queue(company_urls)

    def worker():
        while True:
            try:
                company_url = task_queue.get(block=False)
            except queue.Empty:
                return
            comp_soup = request_page(company_url)
            profile.append(
                get_data_from_profile(
                    request_page(
                        get_specific_urls_about_companies(comp_soup, 'profile'))))
            statistics.append(
                get_data_from_statistics(
                    request_page(get_specific_urls_about_companies(comp_soup, 'statistics'))))
            holders.append(
                get_data_from_holders(
                    request_page(
                        get_specific_urls_about_companies(comp_soup, 'holders'))))
            task_queue.task_done()

    threads = [Thread(target=worker) for _ in range(min(os.cpu_count() + 4, 32))]
    [t.start() for t in threads]
    task_queue.join()
    return profile, statistics, holders


def sort_datastructures(profile: List[Tuple], statistics: List[Tuple], holders: List[Tuple]) \
        -> Tuple[List[Tuple], List[Tuple], List[Tuple]]:
    def convert_percentage_to_float(item: str) -> float:
        try:
            return float(item.strip('%'))
        except ValueError:
            return -sys.float_info.max

    def convert_year_to_int(item: str) -> int:
        try:
            return int(item)
        except ValueError:
            return -1

    def convert_value_to_int(item: str) -> int:
        try:
            return int(''.join(item.split(',')))
        except ValueError:
            return 0

    return sorted(profile, key=lambda item: convert_year_to_int(item[-1]), reverse=True), \
           sorted(statistics, key=lambda item: convert_percentage_to_float(item[-2]), reverse=True), \
           sorted(holders, key=lambda item: convert_value_to_int(item[-1]), reverse=True)


def create_csv_profile(profile: list) -> None:
    with open('profile.csv', mode='w') as profile_file:
        profile_file = csv.writer(profile_file, delimiter=',')
        profile_file.writerow(['Name', 'Code', 'Country', 'Employees', 'CEO Name', 'CEO Born'])
        profile_file.writerows(profile[:5])


def create_csv_statistics(statistics: list) -> None:
    with open('statistics.csv', mode='w') as statistics_file:
        statistics_file = csv.writer(statistics_file, delimiter=',')
        statistics_file.writerow(['Name', 'Code', 'Week Change', 'Total Cash'])
        statistics_file.writerows(statistics[:10])


def create_csv_holder(holder: list) -> None:
    with open('holders.csv', mode='w') as holder_file:
        holder_file = csv.writer(holder_file, delimiter=',')
        holder_file.writerow(['Name', 'Code', 'Shares', 'Date reported', '% Out', 'Value'])
        holder_file.writerows(holder[:10])


def create_pandas() -> tuple[Union[DataFrame, Any], Union[DataFrame, Any], Union[DataFrame, Any]]:
    return pandas.read_csv('holders.csv', index_col='Name'), \
           pandas.read_csv('profile.csv', index_col='Name'), \
           pandas.read_csv('statistics.csv', index_col='Name')


def create_sheets(profile: pandas.DataFrame, statistics: pandas.DataFrame, holders: pandas.DataFrame) -> None:
    profile.to_excel('data.xlsx', sheet_name='Profile')
    statistics.to_excel('data.xlsx', sheet_name='Statistics')
    holders.to_excel('data.xlsx', sheet_name='Holders')


def pprint(profile: pandas.DataFrame, statistics: pandas.DataFrame, holders: pandas.DataFrame) -> None:
    print(profile, '\n', statistics, '\n', holders)


def main(url):
    start = time.time()
    soup = request_page(url)
    urls = get_urls_about_companies(soup)
    profile, statistics, holders = get_required_data_from_page(urls)
    profile, statistics, holders = sort_datastructures(profile, statistics, holders)
    create_csv_profile(profile)
    create_csv_statistics(statistics)
    create_csv_holder(holders)
    holders, profile, statistics = create_pandas()
    create_sheets(profile, statistics, holders)
    pprint(profile, statistics, holders)
    print(time.time() - start)


if __name__ == '__main__':
    main('https://finance.yahoo.com/most-active')
