from unittest.mock import MagicMock, patch

import pytest
import requests

from practice.m6_web_scraping.book_scraper import (
    BookScraper,
)
from practice.m6_web_scraping.model import Book, BookRaw
from practice.m6_web_scraping.pipeline import standardize_books


@patch("practice.m6_web_scraping.book_scraper.requests.get")
def test_scrap_invalid_catalog_page(mock_get):
    mock_req = MagicMock()
    mock_req.status_code = 404
    mock_req.text = "<html>404 Not Found</html>"
    mock_req.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Client Error", response=mock_req
    )

    mock_get.return_value = mock_req
    scraper = BookScraper()
    with pytest.raises(requests.exceptions.HTTPError):
        scraper.scrap_multiple_catalog_pages(999, 1000)


@patch("practice.m6_web_scraping.book_scraper.requests.get")
def test_scrap_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")
    scraper = BookScraper()
    with pytest.raises(requests.exceptions.RequestException):
        scraper.scrap_multiple_catalog_pages(999, 1000)


def test_standardize_books():
    books_raw = [BookRaw("Mock Book", "£13.99", "Two")]
    books_standardized = standardize_books(books_raw)
    assert isinstance(books_standardized[0], Book)
    assert books_standardized[0].title == "Mock Book"
    assert books_standardized[0].price == 13.99
    assert isinstance(books_standardized[0].price, float)
    assert books_standardized[0].rating == 2
    assert isinstance(books_standardized[0].rating, int)
