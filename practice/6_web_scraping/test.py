import pytest
from scraper import get_country, get_employees
from stock_info import Table
from unittest.mock import patch


def test_Table(capfd):
    table = Table(
        'title',
        ['Name', 'Value'],
        [
            ['AAPL', '10.0'],
            ['TSLA', '8.8']
        ]
    )
    print(table)
    out, err = capfd.readouterr()
    assert out.strip() == """
==== title =====
| Name | Value |
----------------
| AAPL | 10.0  |
----------------
| TSLA | 8.8   |
----------------
""".strip()
    assert err == ''


def test_scraper_get_country():
    with patch('scraper.request') as mock, open('practice/6_web_scraping/view-source_https___finance.yahoo.com_quote_TSLA_profile_.html') as file:
        mock.return_value = file.read()
        assert get_country('TSLA') == 'United States'
        assert get_employees('TSLA') == 140473


if __name__ == '__main__':
    pytest.main([__file__])
