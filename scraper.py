import requests
from bs4 import BeautifulSoup
import sqlite3

headers = {
    "User-Agent": "Mozilla/5.0"
}


def create_database():

    conn = sqlite3.connect("data/books.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT,
            link TEXT
        )
    """)

    conn.commit()

    return conn, cursor


def get_soup(url):

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch page")
        return None

    return BeautifulSoup(response.text, "html.parser")


def scrape_page(soup, cursor, conn):

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

        cursor.execute("""
            INSERT INTO books (title, price, rating, link)
            VALUES (?, ?, ?, ?)
        """, (title, price, rating, link))

        conn.commit()


def run_scraper():

    conn, cursor = create_database()

    for page in range(1, 6):

        print(f"Scraping Page {page}...")

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        soup = get_soup(url)

        if soup:

            scrape_page(soup, cursor, conn)

    conn.close()

    print("Scraping completed.")


if __name__ == "__main__":

    run_scraper()