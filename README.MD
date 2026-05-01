# Book Data Scraper

A Python-based web scraping project that extracts book data from BooksToScrape and stores it in multiple formats including CSV, JSON, and SQLite database.

## Features

* Multi-page web scraping
* CSV export
* JSON export
* SQLite database integration
* Dynamic timestamped files
* Rating-based filtering
* Structured project architecture

## Technologies Used

* Python
* BeautifulSoup
* Requests
* SQLite3
* JSON
* CSV

## How to Run

Install dependencies:

```bash
pip install requests beautifulsoup4
```

Run the project:

```bash
python main.py
```

## Project Structure

```text
data/
│
├── books.db
├── books_*.csv
└── books_*.json

main.py
README.md
```
