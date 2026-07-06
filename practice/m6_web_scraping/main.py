from pathlib import Path

from practice.m6_web_scraping.book_scraper import BookScraper
from practice.m6_web_scraping.pipeline import (
    calculate_agg_statistics,
    filter_by_rating,
    sort_by_price_asc,
    standardize_books,
    write_books_to_file,
    write_budget_books_formatted,
    write_stats_formatted,
)

CURR_DIR = Path(__file__).parent
OUTPUT_DIR = CURR_DIR / "output"
OUTPUT_FILE = OUTPUT_DIR / "books_dataset.json"


def main():
    scraper = BookScraper()
    # Every iteration is reference to previous one so its SharedState
    books_raw = scraper.scrap_multiple_catalog_pages(1, 5)
    books_standardized = standardize_books(books_raw)
    ranked_5_books = filter_by_rating(books_standardized, 5)
    asc_price_ranked_5_books = sort_by_price_asc(ranked_5_books)
    top_5_cheap_books = asc_price_ranked_5_books[:5]
    books_stats = calculate_agg_statistics(books_standardized)

    # Report 1
    write_budget_books_formatted(top_5_cheap_books)

    # Report 2
    write_stats_formatted(books_stats)

    # write to file
    write_books_to_file(books_standardized, OUTPUT_DIR, OUTPUT_FILE)


if __name__ == "__main__":
    main()
