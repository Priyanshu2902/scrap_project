# Book Data Scraper

A full-stack Python web scraping and data management project built using Flask, SQLite, BeautifulSoup, and Requests. This application extracts book data, stores it in a database, and displays it through a searchable and filterable web interface.

## Features

* Multi-page web scraping
* SQLite database integration
* Flask web application
* Search books by title
* Filter books by rating
* Structured backend architecture
* Dynamic HTML rendering
* Modular project structure
* Deployed web application

---

## Technologies Used

* Python
* Flask
* BeautifulSoup4
* Requests
* SQLite3
* HTML/CSS

---

## Project Structure

```text
book-data-scraper/
│
├── data/
│   └── books.db
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── database.py
├── scraper.py
├── requirements.txt
├── render.yaml
├── README.md
└── .gitignore
```

---

## How It Works

### 1. Web Scraping

The scraper extracts:

* Book titles
* Prices
* Ratings
* Product links

from multiple pages using BeautifulSoup.

### 2. Database Storage

Scraped data is stored inside a SQLite database using SQL queries.

### 3. Flask Web App

The Flask application retrieves database records and displays them in a browser-based interface.

### 4. Filtering & Search

Users can:

* Search books by title
* Filter books by rating
* Dynamically view matching results

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/book-data-scraper.git
```

Move into project directory:

```bash
cd book-data-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Scraper

```bash
python scraper.py
```

This will:

* Scrape book data
* Store records in SQLite database

---

## Running the Flask App

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Deployment

The project is deployed using Render.

Live Demo:

```text
https://book-data-scraper.onrender.com
```

---

## Key Concepts Learned

* Web scraping
* HTML parsing
* SQL database operations
* Flask backend development
* Dynamic query filtering
* Modular application structure
* Deployment workflow
* Backend/frontend integration

---

## Future Improvements

* REST API support
* Pagination
* Sorting functionality
* Charts & analytics dashboard
* PostgreSQL integration
* Real-world book APIs
* User authentication

---

## Author

Priyanshu Singh
