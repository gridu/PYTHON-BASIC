The previous scraping task is quite old and the target page has changed significantly. Therefore, my mentor proposed another task:

# Data Engineering Intern Assignment: Advanced Web Scraping & Data Pipeline

## 1. Objective
The goal of this assignment is to move beyond basic single-page web scraping and build a modular, scalable ETL (Extract, Transform, Load) script. You will deal with real-world engineering constraints: web pagination, data normalization, code reusability, basic rate limiting, and interacting with structured APIs.

You will be working with a legally authorized, unrestricted sandbox environment: http://books.toscrape.com. This environment explicitly allows scraping, meaning you do not have to worry about IP bans or violating Terms of Service.

## 2. Core Technical Constraints (Architecture Requirements)
Before jumping into the tasks, your script must be built following enterprise code modularity standards:

* **Modularity & Reusability:** Do not write one giant, monolithic script. Separate your code into clear functional layers:
    * `scraper.py` (handles HTTP requests, pagination, and HTML traversal)
    * `pipeline.py` (handles data processing, transformation, type casting, and sorting)
    * `main.py` (the orchestration layer that runs the execution workflow)
* **Polite Scraping (Rate Limiting):** Implement a mandatory programmatic delay (e.g., using `time.sleep(1)`) between consecutive page requests. Real pipelines must respect server load.
* **Error Handling:** Your request module must gracefully catch HTTP errors (404, 500, timeouts) using proper try-except blocks instead of letting the entire pipeline crash.

---

## 3. Task-by-Task Implementation Guide

### Milestone 1: Multi-Page Pagination & Data Extraction
Unlike simple tasks that scrape just the homepage, you must scan multiple pages to compile accurate data datasets.

1.  **Objective:** Build a loop that paginates through the first 5 consecutive pages of the website.
2.  **Extraction Target:** From these 5 pages, extract every book's Title, Price, and Star Rating.
3.  **Data Normalization (Crucial Step):** Raw data from the web is messy text. You must convert these text strings into real Python data types before sorting:
    * Convert the price string (e.g., `"£51.77"`) into a Python `float` (e.g., `51.77`).
    * Convert the textual star rating (e.g., `"Five"`, `"Three"`) into a Python `int` (e.g., `5`, `3`).

### Milestone 2: Structured Output Reporting
Using the structured data collected across the 5 pages in Milestone 1, generate and print two distinct text-based reports to stdout.

#### Report 1: Top 5 Highest-Rated Budget Books
* Filter the data to find the 5 cheapest books that have a perfect 5-star rating.
* **Fields:** Title, Price (£), Rating (as integer)

#### Report 2: Global Catalog Pricing Summary
* Calculate and output the aggregate metrics for all books processed across the 5 pages.
* **Fields:** Total Books Processed, Average Book Price (£), Max Price (£), Min Price (£)

**Formatting Rules for Reports:**
* Report titles must be perfectly centered.
* All data rows and headers must be cleanly text-aligned to the left.
* Include exactly one empty line after each printed report table.

Example Format Reference:
============================ Top 5 Highest-Rated Budget Books ============================
| Title                    | Price (£) | Rating |
------------------------------------------------------------------------------------------
| A Light in the Attic     | 51.77     | 5      |

### Milestone 3: File I/O Persistence (Load Phase)
Printing to console isn't persistent. Update your execution pipeline to automatically serialize your processed data.
* Create an `/output` directory via code if it doesn't already exist.
* Save the complete, normalized list of all extracted books from the 5 pages into a cleanly formatted `books_dataset.json` file inside that directory.

### Milestone 4: Side Job - The JSON API Integration
As a modern data engineer, you will often find that web platforms offer direct API backdoors, bypassing the need for HTML scraping altogether.
* **Objective:** Write a standalone mini-module or utility function that shifts focus away from the book sandbox and instead queries a live, open JSON API: `https://openlibrary.org/search.json?q=data+engineering`
* **Task:** Fetch the JSON response directly using `requests`. Do not use BeautifulSoup here. Extract the top 5 book results.
* **Fields to extract:** Title, Author Name, and First Publish Year. Print this as a simple list to console to demonstrate your ability to work with pure JSON API layers.

---

## 4. Automated Test Suite
Write exactly 2 automated unit tests using Python's built-in `unittest` framework or `pytest` to ensure pipeline resilience:

1.  **Test Data Transformation:** Feed an unformatted mock dictionary (e.g., containing raw strings like `"£12.34"` and `"Four"`) into your pipeline's cleaning module. Assert that it successfully returns a `float` of `12.34` and an `int` of `4`.
2.  **Test Pagination Handling:** Mock an invalid page URL (e.g., page 999) or trigger a mock network timeout, and assert that your scraper's error handling safely logs the issue or raises a predictable custom exception instead of crashing the process.
