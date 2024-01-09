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

import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_stock_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_ceo_data(html):
    soup = BeautifulSoup(html, 'html.parser')


def parse_52_week_change_data(html):
    soup = BeautifulSoup(html, 'html.parser')


def parse_blackrock_holds_data(html):
    soup = BeautifulSoup(html, 'html.parser')

url = 'https://finance.yahoo.com/most-active'
html_data = fetch_stock_data(url)

if html_data:
    ceo_sheet_data = parse_ceo_data(html_data)
    print(ceo_sheet_data)

    change_sheet_data = parse_52_week_change_data(html_data)
    print(change_sheet_data)

    blackrock_sheet_data = parse_blackrock_holds_data(html_data)
    print(blackrock_sheet_data)


def test_ceo_and_change_sheets():
    url = 'https://finance.yahoo.com/most-active'
    html_data = fetch_stock_data(url)

    assert html_data is not None

    ceo_sheet_data = parse_ceo_data(html_data)
    assert len(ceo_sheet_data) == 5

    change_sheet_data = parse_52_week_change_data(html_data)
    assert len(change_sheet_data) == 10
