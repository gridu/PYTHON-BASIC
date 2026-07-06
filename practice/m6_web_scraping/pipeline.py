import json
import os
from dataclasses import asdict
from typing import NamedTuple

from practice.m6_web_scraping.model import Book, BookRaw


class BookStats(NamedTuple):
    total_count: int
    average_price: float
    min_price: float
    max_price: float


RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def standardize_books(books_raw: list[BookRaw]) -> list[Book]:
    books_standardized = []
    for item_raw in books_raw:
        price = float(item_raw.price_raw[1:])
        rating = RATING_MAP[item_raw.rating_raw]
        books_standardized.append(
            Book(title=item_raw.title, price=price, rating=rating)
        )
    return books_standardized


def filter_by_rating(books: list[Book], rating: int) -> list[Book]:
    return [book for book in books if book.rating == rating]


def sort_by_price_asc(books: list[Book]) -> list[Book]:
    return sorted(books, key=lambda book: book.price)  # asc


def calculate_agg_statistics(books: list[Book]) -> BookStats:
    if not books:
        return BookStats(0, 0.0, 0.0, 0.0)

    prices = [book.price for book in books]
    total_count = len(books)

    return BookStats(
        total_count=total_count,
        average_price=sum(prices) / total_count,
        min_price=min(prices),
        max_price=max(prices),
    )


def write_books_to_file(books: list[Book], output_dir: str, output_file: str) -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    books_dict = [asdict(book) for book in books]

    with open(output_file, "w") as f:
        json.dump(books_dict, f, ensure_ascii=False, indent=4)


def write_stats_formatted(stats: BookStats) -> None:
    # 1. Define strict column widths for left-alignment
    col1_width = 30
    col2_width = 15

    # Calculate the exact width of the table grid:
    # |  (2 chars) + col1 +  |  (3 chars) + col2 +  | (2 chars) = col1 + col2 + 7
    table_width = col1_width + col2_width + 7

    # 2. Print perfectly centered title bar matching the table width
    title_text = " Global Catalog Pricing Summary "
    print(title_text.center(table_width, "="))

    # 3. Print Headers (Cleanly text-aligned to the left)
    print(f"| {'Metric':<{col1_width}} | {'Value':<{col2_width}} |")
    print("-" * table_width)

    # 4. Print Data Rows (All strings and numbers cleanly text-aligned to the left)
    print(
        f"| {'Total Books Processed':<{col1_width}} | {stats.total_count:<{col2_width}} |"
    )
    print(
        f"| {'Average Book Price (£)':<{col1_width}} | {f'{stats.average_price:.2f}':<{col2_width}} |"
    )
    print(
        f"| {'Max Price (£)':<{col1_width}} | {f'{stats.max_price:.2f}':<{col2_width}} |"
    )
    print(
        f"| {'Min Price (£)':<{col1_width}} | {f'{stats.min_price:.2f}':<{col2_width}} |"
    )

    # 5. Include exactly one empty line after the report table
    print()


def write_budget_books_formatted(books: list[Book]) -> None:
    # 1. Dynamically find the longest title length
    # We set a baseline minimum of 30 so the table doesn't look too squished if titles are short
    longest_title = max([len(book.title) for book in books]) if books else 0
    col1_width = max(longest_title, 30)

    # Fixed widths for the other columns
    col2_width = 12  # Price (£)
    col3_width = 8  # Rating

    # 2. Recalculate total table width based on the dynamic col1_width
    table_width = col1_width + col2_width + col3_width + 10

    # 3. Print perfectly centered title bar
    title_text = " Top 5 Highest-Rated Budget Books "
    print(title_text.center(table_width, "="))

    # 4. Print Headers (Left-aligned using the dynamic width)
    print(
        f"| {'Title':<{col1_width}} | {'Price (£)':<{col2_width}} | {'Rating':<{col3_width}} |"
    )
    print("-" * table_width)

    # 5. Print Data Rows
    for book in books:
        price_str = f"{book.price:.2f}"
        rating_str = (
            str(int(book.rating)) if book.rating.is_integer() else str(book.rating)
        )

        # The nested curly braces mean: "Left align, padded to the value of col1_width"
        print(
            f"| {book.title:<{col1_width}} | {price_str:<{col2_width}} | {rating_str:<{col3_width}} |"
        )

    # 6. Include exactly one empty line after the report table
    print()
